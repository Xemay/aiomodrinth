## Aiomodrinth

Aiomodrinth is a package for asynchronous interaction with the Modrinth API

----

### Basic usage

```python
import asyncio
from aiomodrinth import ModRinthApi

api = ModRinthApi("your_auth_token", "your_username/id")

async def get_project_description(project_id: str):
    project = await api.get_project(project_id)
    print(project.description)

asyncio.run(get_project_description("project_id"))
```
