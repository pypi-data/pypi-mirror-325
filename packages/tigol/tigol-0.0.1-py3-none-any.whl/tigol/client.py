from .session import LoggingSession
from .auth import AuthorizationCode
from .models import User
import logging

logger = logging.getLogger("TIgolApiClient")

class TIgolApiClient:
    def __init__(self, client_id: str, client_secret: str, api_base_url: str = "https://api.tigol.net"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_base_url = api_base_url.rstrip("/")
        self.session = LoggingSession(logger=logger)

    def get_authorization_url(self, redirect_uri: str, scopes=None) -> str:
        if scopes is None:
            scopes = ["user:read"]
        scope_str = " ".join(scopes)
        return f"https://www.tigol.net/oauth/authorize?client_id={self.client_id}&redirect_uri={redirect_uri}&scope={scope_str}"

    def exchange_code_for_token(self, code: str) -> AuthorizationCode:
        response = self.session.post(
            f"{self.api_base_url}/auth/oidc/token",
            json={"client_id": self.client_id, "client_secret": self.client_secret, "code": code},
        )
        response.raise_for_status()
        return AuthorizationCode.from_dict(response.json())

    def get_user(self, auth: AuthorizationCode) -> User:
        if "user:read" not in auth.scopes:
            raise ValueError("The token lacks 'user:read' scope.")
        response = self.session.get(
            f"{self.api_base_url}/auth/v1/user/me",
            headers={"Authorization": f"Bearer {auth.access_token}"},
        )
        response.raise_for_status()
        return User.from_dict(response.json())
