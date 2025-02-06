import logging
from uuid import UUID
from typing import List, Optional
from urllib.parse import urlencode, urlparse

from .session import LoggingSession
from .auth import AuthorizationCode
from .models import ClientInfo, DailyStatistic, User
from .decorators import require_scope


class TIgolApiClient:
    """
    API client for interacting with the TIgol service.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        api_base_url: str = "https://api.tigol.net",
        log_level=logging.INFO,
    ):
        """
        Initialize the TIgolApiClient.

        Args:
            client_id (str): The client UUID.
            client_secret (str): The client secret UUID.
            api_base_url (str): Base URL for API calls.
            log_level (int): The logging level. Defaults to logging.INFO.
        Raises:
            ValueError: If client_id or client_secret are not valid UUIDs or if the api_base_url does not
                        start with http:// or https://.
        """
        try:
            UUID(client_id)
            UUID(client_secret)
        except ValueError:
            raise ValueError("client_id and client_secret must be valid UUIDs")

        parsed_url = urlparse(api_base_url)
        if parsed_url.scheme not in ["http", "https"]:
            raise ValueError("api_base_url must start with http:// or https://")

        self.client_id = client_id
        self.client_secret = client_secret
        self.api_base_url = api_base_url.rstrip("/")
        
        self._logger = logging.getLogger("TIgolApiClient")
        self._logger.setLevel(log_level)
        self._session = LoggingSession(logger=self._logger)
        
        self.client_info = self._get_client_info()


    def _get_client_info(self) -> ClientInfo:
        token_url = f"{self.api_base_url}/auth/oidc/clients/current"
        response = self._session.get(url=token_url, headers={"Authorization": f"Client {self.client_id}:{self.client_secret}"})
        response.raise_for_status()
        return ClientInfo.from_dict(response.json())
        
    
    def get_authorization_url(
        self,
        redirect_uri: str,
        scopes: Optional[List[str]] = None,
        never_expire: bool = False,
    ) -> str:
        """
        Construct the authorization URL for the OAuth flow.

        Args:
            redirect_uri (str): The URL to redirect to after authorization.
            scopes (Optional[List[str]]): A list of OAuth scopes. Defaults to ["user:read"].
            never_expire (bool): If True, the token will never expire.

        Returns:
            str: The full authorization URL.
        """
        if scopes is None:
            scopes = ["user:read"]

        invalid_scopes = [scope for scope in scopes if scope not in self.client_info.scopes]
        if invalid_scopes:
            raise ValueError(f"The following scopes are invalid: {', '.join(invalid_scopes)}")
        
        scope_str = " ".join(scopes)
        query_params = {
            "client_id": self.client_id,
            "redirect_uri": redirect_uri,
            "scope": scope_str,
        }
        if never_expire:
            query_params["exp"] = "never"

        return f"https://www.tigol.net/oauth/authorize?{urlencode(query_params)}"

    def exchange_code_for_token(self, code: str) -> AuthorizationCode:
        """
        Exchange an authorization code for an access token.

        Args:
            code (str): The authorization code received from the OAuth provider.

        Returns:
            AuthorizationCode: The authorization code object containing token details.

        Raises:
            requests.HTTPError: If the HTTP request fails.
        """
        token_url = f"{self.api_base_url}/auth/oidc/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
        }
        response = self._session.post(token_url, json=payload)
        response.raise_for_status()

        return AuthorizationCode.from_dict(response.json())

    @require_scope("user:read")
    def get_user(self, auth: AuthorizationCode) -> User:
        """
        Retrieve user information using an authorized token.

        Args:
            auth (AuthorizationCode): The authorization token.

        Returns:
            User: The user object with information.

        Raises:
            ValueError: If the provided token does not have the required 'user:read' scope.
            requests.HTTPError: If the HTTP request fails.
        """
        user_url = f"{self.api_base_url}/auth/v1/user/me"
        headers = {"Authorization": f"Bearer {auth.access_token}"}
        response = self._session.get(user_url, headers=headers)
        response.raise_for_status()

        return User.from_dict(response.json())

    @require_scope("user:read")
    def get_daily_statistics(self, auth: AuthorizationCode) -> List[DailyStatistic]:
        """
        Retrieve daily statistics using an authorized token.

        Args:
            auth (AuthorizationCode): The authorization token.

        Returns:
            List[DailyStatistic]: The list of daily statistics.

        Raises:
            ValueError: If the provided token does not have the required 'user:read' scope.
            requests.HTTPError: If the HTTP request fails.
        """
        stats_url = f"{self.api_base_url}/auth/v1/user/daily-statistics"
        headers = {"Authorization": f"Bearer {auth.access_token}"}
        response = self._session.get(stats_url, headers=headers)
        response.raise_for_status()

        stats_data = response.json()
        return [DailyStatistic.from_dict(stat) for stat in stats_data]

    @require_scope("user:write")
    def update_bio(self, auth: AuthorizationCode, new_bio: str) -> bool:
        """
        Update user bio using an authorized token.

        Args:
            auth (AuthorizationCode): The authorization token.
            new_bio (str): The new bio to update. (max. 160 characters)

        Returns:
            bool: True if the bio was updated successfully.

        Raises:
            ValueError: If the provided token does not have the required 'user:write' scope.
            ValueError: If the bio is longer than 160 characters.
            requests.HTTPError: If the HTTP request fails.
        """

        if len(new_bio) > 160:
            raise ValueError("The bio must be 160 characters or less.")

        user_url = f"{self.api_base_url}/auth/v1/user/update-bio"
        headers = {"Authorization": f"Bearer {auth.access_token}"}
        response = self._session.put(user_url, headers=headers, json={"bio": new_bio})
        response.raise_for_status()

        return True

    @require_scope("activity:read")
    def get_activity(self, auth: AuthorizationCode) -> dict:
        """
        Retrieve user activity using an authorized token.

        Args:
            auth (AuthorizationCode): The authorization token.

        Returns:
            dict: The user activity data.

        Raises:
            requests.HTTPError: If the HTTP request fails.
        """
        user_url = f"{self.api_base_url}/auth/v1/activity"
        headers = {"Authorization": f"Bearer {auth.access_token}"}
        response = self._session.get(user_url, headers=headers)
        response.raise_for_status()

        return response.json()

    @require_scope("activity:write")
    def set_activity(
        self,
        auth: AuthorizationCode,
        title: str,
        description: str,
        btn1_text: str,
        btn1_link: str,
        image_url: str,
        expires_in: Optional[int] = None,
    ) -> bool:
        """
        Set user activity using an authorized token.

        Args:
            auth (AuthorizationCode): The authorization token.
            title (str): The title of the activity.
            description (str): The description of the activity.
            btn1_text (str): The text for the first button.
            btn1_link (str): The link for the first button.
            image_url (str): The URL of the image.
            expires_in (Optional[int]): The expiration time in hours (1, 2, 4, 8, 24). Defaults to None.

        Returns:
            bool: True if the activity was set successfully.

        Raises:
            requests.HTTPError: If the HTTP request fails.
        """
        user_url = f"{self.api_base_url}/auth/v1/activity"
        headers = {"Authorization": f"Bearer {auth.access_token}"}
        payload = {
            "title": title,
            "description": description,
            "btn1_text": btn1_text,
            "btn1_link": btn1_link,
            "image_url": image_url,
        }
        if expires_in:
            if expires_in not in [1, 2, 4, 8, 24]:
                raise ValueError(
                    "expires_in must be one of the following values: 1, 2, 4, 8, 24"
                )
            payload["expires_in"] = expires_in

        response = self._session.put(user_url, headers=headers, json=payload)
        response.raise_for_status()

        return True

    @require_scope("activity:write")
    def clear_activity(self, auth: AuthorizationCode) -> bool:
        """
        Clear user activity using an authorized token.

        Args:
            auth (AuthorizationCode): The authorization token.

        Returns:
            bool: True if the activity was cleared successfully.

        Raises:
            requests.HTTPError: If the HTTP request fails.
        """
        user_url = f"{self.api_base_url}/auth/v1/activity"
        headers = {"Authorization": f"Bearer {auth.access_token}"}
        response = self._session.delete(user_url, headers=headers)
        response.raise_for_status()

        return True
