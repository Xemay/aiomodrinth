from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, Any, NamedTuple

from .utils import string_to_datetime
from aiomodrinth.models.enums import SupportStatus, ProjectStatus, ProjectType, Category, DependencyType, VersionType, \
    Loader, HashAlgorithm
from aiomodrinth.license import License
from aiomodrinth.models.gallery import GalleryImage


class GameVersion(NamedTuple):
    version: str

    def __str__(self):
        return self.version


@dataclass
class Project:
    slug: Optional[str]
    title: str
    description: str
    categories: list[Category]
    client_side: SupportStatus
    server_side: SupportStatus
    body: str
    status: ProjectStatus
    license: License
    issues_url: Optional[str]
    source_url: Optional[str]
    wiki_url: Optional[str]
    discord_url: Optional[str]
    donation_urls: list[str]
    project_type: ProjectType
    downloads: int
    icon_url: Optional[str]
    id: str
    team: str
    moderator_message: str
    published: datetime
    updated: datetime
    followers: int
    versions: list[str]
    gallery: list[GalleryImage]

    def __eq__(self, other) -> bool:
        return isinstance(other, Project) and self.id == other.id

    @classmethod
    def fromjson(cls, kwargs: dict[Any]):
        kwargs['client_side'] = SupportStatus[kwargs['client_side'].upper()]
        kwargs['server_side'] = SupportStatus[kwargs['server_side'].upper()]
        kwargs['status'] = ProjectStatus[kwargs['status'].upper()]
        kwargs['license'] = License(**kwargs['license'])
        kwargs['project_type'] = ProjectType[kwargs['project_type'].upper()]
        kwargs['published'] = string_to_datetime(kwargs['published'])
        kwargs['updated'] = string_to_datetime(kwargs['updated'])
        kwargs['categories'] = Category.fromlist(kwargs['categories'])
        kwargs['gallery'] = GalleryImage.fromlist(kwargs['gallery'])

        del kwargs['body_url']

        return cls(**kwargs)

    @staticmethod
    def fromlist(projects: list[dict]) -> list['Project']:
        projects_ = [Project.fromjson(pjct) for pjct in projects]
        return projects_


@dataclass
class VersionFile:
    hashes: dict[HashAlgorithm, str]
    url: str
    filename: str
    primary: bool

    @classmethod
    def fromjson(cls, kwargs: dict) -> 'VersionFile':
        kwargs['hashes'] = HashAlgorithm.forDict(kwargs['hashes'])

        return VersionFile(**kwargs)

    @classmethod
    def forList(cls, versionList: list[dict[str, Any]]) -> list['VersionFile']:
        versions = []
        for version in versionList:
            versions.append(VersionFile(**version))

        return versions


@dataclass
class ProjectVersion:
    name: str
    version_number: str
    changelog: Optional[str]
    game_versions: list[str]
    version_type: VersionType
    loaders: list[Loader]
    featured: bool
    id: str
    project_id: str
    author_id: str
    date_published: datetime
    downloads: int
    files: list[VersionFile]

    @classmethod
    def fromjson(cls, kwargs: dict) -> 'GameVersion':
        kwargs["game_versions"] = [GameVersion(version) for version in kwargs["game_versions"]]
        kwargs['version_type'] = VersionType[kwargs['version_type'].upper()]
        kwargs['loaders'] = Loader.fromlist(kwargs['loaders'])
        kwargs['date_published'] = string_to_datetime(kwargs['date_published'])
        kwargs['files'] = VersionFile.forList(kwargs['files'])

        return cls(**kwargs)

    @staticmethod
    def fromlist(pversions: list) -> list['GameVersion']:
        return [ProjectVersion.fromjson(pvers) for pvers in pversions]


@dataclass
class Dependency:
    version_id: Optional[str]
    project_id: Optional[str]
    dependency_type: DependencyType


class ProjectLicense(Enum):
    CUSTOM = 'custom'
    LGPL = 'lgpl'
    APACHE = 'apache',
    BSD_2_CLAUSE = 'bsd-2-clause'
    BSD_3_CLAUSE = 'bsd-3-clause',
    BSL = 'bsl'
    CC0 = 'cc0'
    UNLICENSE = 'unlicense'
    MPL = 'mpl'
    MIT = 'mit'
    ARR = 'arr'
    LGPL3 = 'lgpl-3'

    def __str__(self):
        return self.value
