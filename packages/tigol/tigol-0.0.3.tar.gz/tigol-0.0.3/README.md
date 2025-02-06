# TIgol API Wrapper (Python)

This repository provides a Python wrapper for the TIgol API.

## Example

You can find an example usage [here](https://github.com/alessiodam/TIgol-examples/blob/main/python/oauth/app.py).

```python
# Description: Example script to demonstrate how to use the TIgol API Client to get user information
# This expects a valid client ID and a valid client secret to be used for the API client
# When creating the application on TIgol, please ensure that the redirect URI is set to `https://example.com/authorized`
import sys
from src.tigol import TIgolApiClient, User

# Initialize the TIgol API Client
tigol_client = TIgolApiClient(
  client_id="client_id",
  client_secret="client_secret",
)

# Get authorization code from user
auth_url = tigol_client.get_authorization_url(redirect_uri="https://example.com/authorized", scopes=["user:read"])
auth_code_input = input(f"""
Please go to the following URL to authorize the application:

{auth_url}

After authorization, you will be redirected to a URL. 
Please copy the code from the redirected URL (for example, copy `abc` from ?token=abc) and paste it here: 
""")
auth_code = auth_code_input.strip()

token_obj = tigol_client.exchange_code_for_token(code=auth_code)
if "user:read" not in token_obj.scopes:
  print("user:read scope wasn't accepted, can't continue.")
  sys.exit(1)

user_obj: User = tigol_client.get_user(token_obj)
print(f"User Information: {user_obj}")
```

## License

This project is licensed under the GNU AGPLv3 License. See the [LICENSE](LICENSE) file for details.
