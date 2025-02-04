# nextlayer-sdk-python

Client utilities to interact with next layer public APIs.

## Configuration

The module will use a YAML Config file in , where it also needs to **write** to, to store
and update the obtained Tokens and their expiry (similar like `kubctl` does with kubeconfig).

_Example `~/.nextlayer-sdk/auth.nlcustomers.yml`:_

```yaml
server_url: https://login.nextlayer.at/auth/
realm_name: nlcustomers
client_id: nextlayer-sdk-python
username: foobar
password: topsecret

extra_params:
  audience: nextlayer-sdk-python

```

Except for `username`, all settings are optional, but if no `password` is
supplied in config, the password will be asked interactively (if STDIN is a TTY) !

Alternatively the username can be suppled in the `NEXTLAYERSDK_USERNAME` environment
variable or directly passed to the `NlAuth` cosntructor.

Alternatively the password can be suppliend in the `NEXTLAYERSDK_PASSWORD` environment
variable.

## Usage

```python
import requests
from nextlayer.sdk.auth import NlAuth

nlauth = NlAuth()
access_token = nlauth.get_access_token()

# make Request to some API Endpoint
rsp = requests.get(
    "https://portal.nextlayer.at/apis/v1/users/self",
    headers={"Authorization": "Bearer " + access_token},
)
```

You need to call the `.get_access_token()` Method **every time** you make API-Calls,
because it checks if the Token is still valid and will refresh it if necessary.

### Usage with httpx

```python
import httpx

from nextlayer.sdk.auth_httpx import NlHttpxAuth

client = httpx.Client(
    timeout=httpx.Timeout(30.0),
    base_url=f"{base_url}/api/v2",
    auth=NlHttpxAuth(),
)
```
