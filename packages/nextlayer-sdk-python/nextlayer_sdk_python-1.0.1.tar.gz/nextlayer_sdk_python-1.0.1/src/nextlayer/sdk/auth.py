#!/usr/bin/env python3
import datetime
import getpass
import json
import logging
import os
import sys
import time
from typing import Any

import jwt
import yaml
from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakGetError
from pydantic import BaseModel, Field

from . import errors

# Retrieve/Refresh Token on demand from next layer IAM


log = logging.getLogger(__name__)

DEFAULT_KEYCLOAK_URL = "https://login.nextlayer.at/auth/"
DEFAULT_CLIENT_ID = "nextlayer-sdk-python"
DEFAULT_REALM = "nlcustomers"


def _get_current_user_homedir() -> str:
    try:
        # this is the reliable/correct method, that also works in cases
        # where e.g. process-manager like gunicorn changes the efective UID
        # but preserves the environment
        import pwd

        return pwd.getpwuid(os.getuid()).pw_dir
    except Exception:
        # fallback for (non-unix) platforms without `pwd` module
        return os.path.expanduser("~")


def _get_default_config_filename(realm: str) -> str:
    homedir = _get_current_user_homedir()
    default_fn = os.path.join(homedir, ".nextlayer-sdk", f"auth.{realm}.yml")
    if os.path.exists(default_fn):
        return default_fn
    else:
        log.debug(f"no config file found - using {default_fn}")
        os.makedirs(os.path.dirname(default_fn), mode=0o700, exist_ok=True)
        return default_fn


class PersistentConfig(BaseModel):
    server_url: str = DEFAULT_KEYCLOAK_URL
    realm_name: str = DEFAULT_REALM
    client_id: str = DEFAULT_CLIENT_ID
    username: str | None = None
    password: str | None = None

    expires_at: float | None = None
    refresh_expires_at: float | None = None
    tokens: Any | None = None

    extra_params: dict[str, Any] = Field(default_factory=dict)


class FilePerRealmAuthStore:
    def __init__(self, filename: str):
        self.config_filename: str = filename
        self.config = PersistentConfig()
        self.config_read_mtime = 0

        self.read_config()

    @property
    def mtime(self) -> float:
        """last time the store was modified"""
        return os.stat(self.config_filename).st_mtime

    def reload_if_modified(self):
        if self.mtime > self.config_read_mtime:
            log.debug(f"config {self.config_filename} changed since we last read it")
            self.read_config()

    def read_config(self):
        if not os.path.isfile(self.config_filename):
            self.config = PersistentConfig()
            return
        log.debug(f"reading config from {self.config_filename}")
        self.config_read_mtime = self.mtime
        with open(self.config_filename) as fil:
            self.config = PersistentConfig.model_validate(yaml.safe_load(fil) or {})

    def write_config(self):
        log.debug(f"writing config to {self.config_filename}")
        # in the yaml we only want to store keys that have been explicitly
        # set to some (non-default) value
        data = self.config.model_dump(
            exclude_none=True, exclude_unset=True, exclude_defaults=True
        )
        data["_note"] = (
            "file updated by nextlayer-sdk-python at "
            + datetime.datetime.now().astimezone().isoformat()
        )
        with open(self.config_filename, "w") as fil:
            yaml.safe_dump(data, fil)

    def set_extra_param(
        self, param: str, value: str | int | float | bool | None = None
    ):
        if value is None:
            # remove it
            self.config.extra_params.pop(param, None)
        else:
            self.config.extra_params[param] = value
        self.write_config()


class NlAuth(object):
    def __init__(
        self,
        config_filename=None,
        server_url=None,
        realm_name=None,
        client_id=None,
        username=None,
    ):
        self.config_filename = config_filename or _get_default_config_filename(
            realm_name or DEFAULT_REALM
        )
        self.store = FilePerRealmAuthStore(self.config_filename)

        new_server_url = (server_url or self.store.config.server_url).rstrip("/") + "/"
        new_realm_name = realm_name or self.store.config.realm_name
        new_client_id = client_id or self.store.config.client_id
        self.username = (
            username
            or os.environ.get("NEXTLAYERSDK_USERNAME")
            or self.store.config.username
        )

        self.store.config.server_url = new_server_url
        self.store.config.realm_name = new_realm_name
        self.store.config.client_id = new_client_id

        if self.username:
            self.store.config.username = self.username

        # Configure client
        self.keycloak_openid = KeycloakOpenID(
            server_url=new_server_url,
            client_id=new_client_id,
            realm_name=new_realm_name,
            verify=True,
        )

    def token_expired(self) -> bool:
        now = int(time.time())
        exp_at = self.store.config.expires_at
        is_expired = not exp_at or exp_at <= now
        if is_expired and exp_at:
            log.debug(f"access_token is expired {exp_at!r}")
        return is_expired

    def refresh_expired(self) -> bool:
        now = int(time.time())
        exp_at = self.store.config.refresh_expires_at
        is_expired = not exp_at or exp_at <= now
        if is_expired and exp_at:
            log.debug(f"refresh_token is expired {exp_at!r}")
        return is_expired

    def set_extra_param(
        self, param: str, value: str | int | float | bool | None = None
    ):
        self.store.set_extra_param(param, value)

    def clear_tokens(self):
        log.debug("clearing tokens")
        self.store.config.expires_at = None
        self.store.config.refresh_expires_at = None
        self.store.config.tokens = None
        self.store.write_config()

    def update_tokens(self, tokens: dict[str, Any]) -> str:
        log.debug(
            f"update_tokens: expires_in={tokens['expires_in']!r} refresh_expires_in={tokens['refresh_expires_in']!r}"
        )
        self.store.config.expires_at = int(time.time()) + int(
            tokens["expires_in"] * 0.75
        )
        self.store.config.refresh_expires_at = int(time.time()) + int(
            (tokens["refresh_expires_in"] or 86400) * 0.75
        )
        self.store.config.tokens = tokens
        return tokens["access_token"]

    def do_login(self, password: str | None = None) -> str:
        log.debug(
            f"do_login for realm {self.store.config.realm_name} on {self.store.config.server_url}"
        )
        password = (
            password
            or os.environ.get("NEXTLAYERSDK_PASSWORD")
            or self.store.config.password
        )

        # Interactive:
        if (not self.username or not password) and sys.stdin.isatty():
            if not self.username:
                self.username = getpass.getuser()
            if not password:
                print(
                    "# Note: If you want to log in with another username, just press Enter.\n"
                    "#       The password you enter will be used once to obtain new\n"
                    "#       tokens from IAM and will not be stored anywhere. Once the\n"
                    "#       refresh token expires, you will need to enter it again."
                )
                password = getpass.getpass(f"Password for {self.username}: ")
            if not password:
                self.username = input("Username: ")
                if self.username:
                    self.store.config.username = self.username
                    self.store.write_config()
                password = getpass.getpass(f"Password for {self.username}: ")

        if not self.username or not password:
            raise errors.AuthenticationError(
                "failed to set NEXTLAYERSDK_USERNAME/PASSWORD from config,env-var,interactive"
            )

        extra = self.store.config.extra_params

        log.debug(f"make keycloak token-request for user {self.username}")
        tokens = self.keycloak_openid.token(self.username, password, **extra)
        access_token = self.update_tokens(tokens)
        self.store.write_config()
        return access_token

    def do_refresh(self) -> str:
        try:
            log.debug("make keycloak token-refresh")
            tokens = self.keycloak_openid.refresh_token(
                self.store.config.tokens["refresh_token"]
            )
        except KeycloakGetError as e:
            # e.g. 400: b'{"error":"invalid_grant", "error_description":"Session not active"}'
            # ... when session has been deleted in Keycloak and refresh_token cannot be used anymore
            sys.stderr.write("token refresh failed: %s\n" % (e,))
            return self.do_login()

        # sys.stderr.write("obtained new access_token\n")
        access_token = self.update_tokens(tokens)
        self.store.write_config()
        return access_token

    def get_access_token(self) -> str:
        try:
            try:
                self.store.reload_if_modified()
            except FileNotFoundError:
                pass
            if self.refresh_expired():
                access_token = self.do_login()
            elif self.token_expired():
                access_token = self.do_refresh()
            else:
                access_token = self.store.config.tokens["access_token"]
            return access_token
        except errors.NextlayerSdkError:
            raise
        except Exception as e:
            raise errors.AuthenticationError(e)

    def access_token_info(self) -> dict[str, Any]:
        access_token = self.get_access_token()

        log.debug("obtaining certs from keycloak for token-verification")
        return jwt.decode(
            access_token,
            key=jwt.PyJWK(self.keycloak_openid.certs()["keys"][0]),
            options=dict(verify_aud=False),
            algorithms=["HS256", "RS256"],
        )


def parse_commandline_args():
    import argparse

    parser = argparse.ArgumentParser(
        prog="nextlayer-auth",
        description="Log in via next layer IAM to obtain an access token",
    )
    parser.add_argument(
        "-f",
        "--config",
        help=f"config filename (default: ~/.nextlayer-sdk/auth.{DEFAULT_REALM}.yml)",
    )
    parser.add_argument(
        "-k", "--keycloak-url", help=f"keycloak url - default: {DEFAULT_KEYCLOAK_URL}"
    )
    parser.add_argument(
        "-r", "--realm", help=f"keycloak realm - default: {DEFAULT_REALM}"
    )
    parser.add_argument(
        "-i", "--client-id", help=f"keycloak client_id - default: {DEFAULT_CLIENT_ID}"
    )
    parser.add_argument("-u", "--username", help="username")
    parser.add_argument("-a", "--aud", help="set audience - default: not set")
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(
        "command",
        nargs="*",
        default=["login"],
        help="valid commands: login(default), clear, tokeninfo",
    )
    args = parser.parse_args()
    return args


def main() -> int:
    try:
        args = parse_commandline_args()

        logging.basicConfig()
        if args.verbose:
            log.setLevel(logging.DEBUG)
            log.debug(f"arguments: {args!r}")

        nlauth = NlAuth(
            config_filename=args.config,
            server_url=args.keycloak_url,
            realm_name=args.realm,
            client_id=args.client_id,
            username=args.username,
        )

        if args.aud:
            # set Audience Claim
            nlauth.set_extra_param("audience", args.aud)

        for command in args.command:
            if command == "clear":
                nlauth.clear_tokens()

            elif command == "login":
                access_token = nlauth.get_access_token()
                sys.stdout.write("Authorization: Bearer " + access_token)

            elif command == "tokeninfo":
                print(json.dumps(nlauth.access_token_info(), indent=2))

            else:
                print("unknown command '%s'" % command)
        return 0
    except errors.NextlayerSdkError as e:
        print(e)
        return 1


if __name__ == "__main__":
    sys.exit(main() or 0)
