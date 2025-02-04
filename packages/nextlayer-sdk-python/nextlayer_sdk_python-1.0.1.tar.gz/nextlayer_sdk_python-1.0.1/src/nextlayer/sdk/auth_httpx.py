from typing import Generator

import httpx

from .auth import NlAuth


class NlHttpxAuth(httpx.Auth):
    def __init__(self, *args, **kwargs):
        self.nlauth = NlAuth(*args, **kwargs)

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["Authorization"] = "Bearer " + self.nlauth.get_access_token()
        yield request
