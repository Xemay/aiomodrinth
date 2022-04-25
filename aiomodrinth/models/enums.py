from enum import Enum


class Category(Enum):
    ADVENTURE = 'adventure'
    CURSED = 'cursed'
    DECORATION = 'decoration'
    EQUIPMENT = 'equipment'
    FOOD = 'food'
    LIBRARY = 'library'
    MAGIC = 'magic'
    MISC = 'misc'
    OPTIMIZATION = 'optimization'
    STORAGE = 'storage'
    TECHNOLOGY = 'technology'
    UTILITY = 'utility'
    WORLDGEN = 'worldgen'

    FABRIC = 'fabric'
    FORGE = 'forge'

    @classmethod
    def fromlist(cls, categories: list[str]) -> list['Category']:
        cats = []
        for category in categories:
            cats.append(cls[category.upper()])

        return cats


class Loader(Enum):
    FORGE = 'forge'
    FABRIC = 'fabric'
    QUILT = 'quilt'

    @staticmethod
    def fromlist(loaders: list) -> list['Loader']:
        return [Loader[load.upper()] for load in loaders]


class SupportStatus(Enum):
    REQUIRED = 'required'
    OPTIONAL = 'optional'
    UNSUPPORTED = 'unsupported'


class ProjectStatus(Enum):
    APPROVED = 'approved'
    REJECTED = 'rejected'
    DRAFT = 'draft'
    UNLISTED = 'unlisted'
    PROCESSING = 'processing'
    UNKNOWN = 'unknown'


class ProjectType(Enum):
    MOD = 'mod'
    MODPACK = 'modpack'


class VersionType(Enum):
    RELEASE = 'release'
    BETA = 'beta'
    ALPHA = 'alpha'
    SNAPSHOT = 'snapshot'


class DependencyType(Enum):
    REQUIRED = 'required'
    OPTIONAL = 'optional'
    INCOMPATIBLE = 'incompatible'


class UserRole(Enum):
    DEVELOPER = 'developer'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class HashAlgorithm(Enum):
    """ Possible hash algorithms used by modrinth """
    SHA512 = 'sha512'
    SHA1 = 'sha1'
    UNKNOWN = 'unknown'  #: Custom value

    @classmethod
    def forString(cls, string: str):
        try:
            return HashAlgorithm[string]
        except KeyError:
            return HashAlgorithm.UNKNOWN

    @classmethod
    def forDict(cls, hashes: dict[str, str]) -> dict['HashAlgorithm', str]:
        phashes = {}
        for algorithm, value in hashes.items():
            phashes[HashAlgorithm.forString(algorithm)] = value
        return phashes
