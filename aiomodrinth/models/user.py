from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from aiomodrinth.models.enums import UserRole

from .utils import string_to_datetime


@dataclass
class User:
    username: str
    name: Optional[str]
    email: Optional[str]
    bio: Optional[str]
    id: str
    github_id: int
    avatar_url: str
    created: datetime
    role: UserRole

    @classmethod
    def fromjson(cls, kwargs: dict) -> 'User':
        kwargs['created'] = string_to_datetime(kwargs['created'])
        kwargs['role'] = UserRole[kwargs['role'].upper()]

        return User(**kwargs)
