from aiomodrinth.models.user import User

from dataclasses import dataclass


@dataclass
class TeamMember:
    team_id: str
    user: User
    role: str
    permissions: int
    accepted: bool

    @classmethod
    def fromjson(cls, **kwargs) -> 'TeamMember':
        kwargs['user'] = User.fromjson(kwargs['user'])

        return cls(**kwargs)

    @staticmethod
    def fromlist(team_members: list[dict]) -> list['TeamMember']:
        return [TeamMember.fromjson(**tm) for tm in team_members]
