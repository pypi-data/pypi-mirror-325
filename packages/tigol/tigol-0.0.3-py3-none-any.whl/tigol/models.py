from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class User:
    id: int
    first_name: str = ""
    last_name: str = ""
    username: str = ""
    email: str = ""
    bio: str = ""
    uuid: str = ""
    two_factor_enabled: bool = False
    created_at: str = ""
    updated_at: str = ""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        return cls(**data)


@dataclass
class DailyStatistic:
    id: int
    date: str
    successful_logins: int
    failed_logins: int
    api_requests: int

    @staticmethod
    def from_dict(data: dict) -> "DailyStatistic":
        return DailyStatistic(
            id=data["id"],
            date=data["date"],
            successful_logins=data["successful_logins"],
            failed_logins=data["failed_logins"],
            api_requests=data["api_requests"],
        )

@dataclass
class ClientInfo:
    approved: bool
    client_id: str
    created_at: str
    description: str
    logo_url: str
    name: str
    owner: User
    public: bool
    redirect_uri: str
    scopes: str
    updated_at: str
    website: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ClientInfo":
        owner_data = data.pop("owner")
        owner = User.from_dict(owner_data)
        return cls(owner=owner, **data)