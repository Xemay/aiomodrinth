"""
Aiomodrinth

this package that makes it easy to asynchronously interact with the API modrinth.com
"""


#import aiohttp
from aiomodrinth.api import ModRinthApi, Facets, full_project
from aiomodrinth.facets import Facet, FacetAnd, FacetOr, Facets

from aiomodrinth.models.project import ProjectType, Category, ProjectLicense, GameVersion

__author__ = 'Xemay'
__version__ = '0.1.1'
