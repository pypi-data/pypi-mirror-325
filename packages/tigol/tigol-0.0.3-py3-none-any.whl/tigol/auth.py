from typing import List, Dict, Any


class AuthorizationCode:
    def __init__(self, access_token: str, scopes: List[str]):
        self.access_token = access_token
        self.scopes = scopes

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AuthorizationCode":
        token = data.get("access_token")
        if not token:
            raise ValueError("Access token not found in response.")

        scope_raw = data.get("scope", "")
        scopes = scope_raw.replace(",", " ").split()
        return cls(access_token=token, scopes=scopes)
