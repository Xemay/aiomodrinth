import aiohttp

from aiomodrinth.common import BASE_URL
from aiomodrinth.models.project import Project
from aiomodrinth.models.enums import SupportStatus, ProjectType, Category

from aiomodrinth.models.utils import string_to_datetime

from typing import Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class SearchResults:
    hits: list['SearchProject']
    offset: int
    limit: int
    total_hits: int

    @classmethod
    def fromjson(cls, kwargs):
        kwargs['hits'] = SearchProject.fromlist(kwargs['hits'])

        return cls(**kwargs)


@dataclass
class SearchProject:
    slug: Optional[str]
    title: Optional[str]
    description: Optional[str]
    categories: Optional[list[Category]]
    client_side: Optional[SupportStatus]
    server_side: Optional[SupportStatus]
    project_type: ProjectType
    downloads: int
    icon_url: Optional[str]
    project_id: str
    author: str
    versions: list[str]
    follows: int
    date_created: datetime
    date_modified: datetime
    latest_version: Optional[str]
    license: str
    gallery: list[str]

    def __eq__(self, other):
        return isinstance(other, SearchProject) and self.project_id == other.project_id

    async def to_project(self) -> Project:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(url=BASE_URL+f'project/{self.project_id}')
            project = Project.fromjson(await resp.json())
            return project

    @classmethod
    def fromjson(cls, **kwargs) -> 'SearchProject':
        kwargs['categories'] = Category.fromlist(kwargs['categories'])
        kwargs['client_side'] = SupportStatus[kwargs['client_side'].upper()]
        kwargs['server_side'] = SupportStatus[kwargs['server_side'].upper()]
        kwargs['project_type'] = ProjectType[kwargs['project_type'].upper()]
        kwargs['date_created'] = string_to_datetime(kwargs['date_created'])
        kwargs['date_modified'] = string_to_datetime(kwargs['date_modified'])

        return cls(**kwargs)

    @staticmethod
    def fromlist(sprojects: list[dict]) -> list['SearchProject']:
        return [SearchProject.fromjson(**prjct) for prjct in sprojects]
