import aiohttp
import json
from typing import Literal

from ._requests import *
from aiomodrinth.common import BASE_URL

from aiomodrinth.exceptions import InvalidToken, InvalidUser

from aiomodrinth.models.project import Project
from aiomodrinth.models.user import User
from aiomodrinth.models.member import TeamMember
from aiomodrinth.models.search import SearchResults
from aiomodrinth.exceptions import ObjectNotFound


class ModRinthApi:
    """
    The main class for interacting with the API
    """

    def __init__(self, token: str = None, user: str = "none"):

        if not isinstance(user, str):
            raise ValueError("The username/id must be a string")

        self.user = user

        if token is not None:
            if not isinstance(token, str):
                raise ValueError("The token must be a string")
            self._token = token
        else:
            self._token = "none"

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token: str):
        if not isinstance(token, str):
            raise ValueError("The token must be a string")
        self._token = token

    async def search(self, query: str,
                     index: Literal['relevance', 'downloads', 'follows', 'newest', 'updated'] = 'relevance',
                     offset: int = 0,
                     limit: int = 10,
                     **kwargs) -> SearchResults:
        facets = []
        for k in kwargs.keys():
            if isinstance(kwargs[k], list):
                for i in kwargs[k]:
                    facets.append([f"{k}:{i}"])
            elif isinstance(kwargs[k], str):
                facets.append([f"{k}:{kwargs[k]}"])
            else:
                raise ValueError("Sorting params must be a string or list")
        params = {'query': query, 'index': str(index), 'offset': str(offset), 'limit': str(limit)}
        if len(facets) > 0:
            params['facets'] = json.dumps(facets)
        response = await get('search', params=params)
        if response.status == 400:
            raise ValueError("Incorrect parameters are specified")

        return SearchResults.fromjson(await response.json())

    async def get_project(self, project_id: str) -> Project | None:
        response = await get(way=f"project/{project_id}")
        if response.status == 404:
            return None
        return Project.fromjson(await response.json())

    async def get_user(self, user_id: str) -> User | None:
        response = await get(way=f"user/{user_id}")
        if response.status == 404:
            return None
        json = await response.json()
        return User.fromjson(json)

    async def modify_user(self, **kwargs):
        response = await patch(f"user/{self.user}", json=kwargs, headers={'Authorization': self._token})
        if response.status == 401:
            raise InvalidToken
        elif response.status == 404:
            raise InvalidUser

    async def user_projects(self, user_id) -> list[Project] | None:
        response = await get(f"user/{user_id}/projects")
        if response.status == 404:
            return None
        return Project.fromlist(await response.json())

    async def followed_projects(self) -> list[Project] | None:
        response = await get(f"user/{self.user}/follows", headers={'Authorization': self._token})
        if response.status == 401:
            raise InvalidToken
        if response.status == 404:
            return None
        return Project.fromlist(await response.json())

    async def project_members(self, project_id: str) -> list[TeamMember] | None:
        response = await get(f"project/{project_id}/members")
        if response.status == 404:
            return None
        return TeamMember.fromlist(await response.json())

    async def team_members(self, team_id: str) -> list[TeamMember] | None:
        response = await get(f"team/{team_id}/members")
        if response.status == 404:
            return None
        return TeamMember.fromlist(await response.json())
