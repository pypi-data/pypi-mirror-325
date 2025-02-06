from functools import wraps
from typing import Callable

from .auth import AuthorizationCode


def require_scope(*required_scopes: str):
    """
    Decorator to ensure the authorization token has the required scopes.

    Args:
        *required_scopes (str): The required OAuth scopes.

    Raises:
        ValueError: If the token does not contain the required scopes.
    """

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(self, auth: AuthorizationCode, *args, **kwargs):
            missing_scopes = [
                scope for scope in required_scopes if scope not in auth.scopes
            ]
            if missing_scopes:
                raise ValueError(
                    f"The token lacks the required scopes: {', '.join(missing_scopes)}"
                )

            return func(self, auth, *args, **kwargs)

        return wrapper

    return decorator
