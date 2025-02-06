from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    bio: str
    uuid: str
    two_factor_enabled: bool
    created_at: str
    updated_at: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        return cls(**data)
