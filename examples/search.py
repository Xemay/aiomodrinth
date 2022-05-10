import aiomodrinth
from aiomodrinth.api import ModRinthApi
from aiomodrinth import Facet, Facets
from aiomodrinth.models.project import Category, GameVersion, ProjectType, ProjectLicense

import asyncio

api = ModRinthApi()


async def search():
    facets = Facets(Facet(Category.ADVENTURE) & Facet(Category.FABRIC), Facet(GameVersion("1.17.1")))
    results = await api.search(query="", limit=20, index='relevance', facets=facets)

    print(results.hits[0].downloads)

    # in addition to the category and game version, you can sort the results by license and project type
    # project_type=['mod', 'modpack'] or project_type='mod'

asyncio.run(search())
