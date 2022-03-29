from aiomodrinth.api import ModRinthApi

import asyncio

api = ModRinthApi()


async def search():
    results = await api.search("craft", limit=3, index='downloads', categories=['fabric', 'magic'], versions="1.18.1")

    # in addition to the category, you can sort the results by license, game version and project type
    # project_type=['mod', 'modpack'] or project_type='mod'
    # ----
    # parameters can be lists or string

    print(results.hits[0].downloads)
    # to get a complete project you can use the method .to_project() for any search result in 'hits'

    project = await results.hits[0].to_project()
    print(project.body)

asyncio.run(search())
