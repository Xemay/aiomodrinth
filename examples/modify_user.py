from aiomodrinth import ModRinthApi

import asyncio

api = ModRinthApi("your_token", "your username/id")


async def change_bio(bio_text: str):
    await api.modify_user(bio=bio_text)
    # you can also change:
    #   - username
    #   - email
    # using kwargs
    #
    # Example:
    # await api.modify_user(email="your email")

asyncio.run(change_bio("Updated bio"))
