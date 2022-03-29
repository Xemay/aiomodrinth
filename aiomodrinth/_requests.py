import aiohttp

from aiomodrinth.common import BASE_URL


async def get(way: str, headers=None, **kwargs) -> aiohttp.ClientResponse:
    async with aiohttp.ClientSession(headers=headers) as s:
        resp = await s.get(url=f"{BASE_URL}{way}", **kwargs)
        return resp


async def post(way: str, payload: dict | list, headers=None, **kwargs) -> aiohttp.ClientResponse:
    async with aiohttp.ClientSession(headers=headers) as s:
        resp = await s.post(url=f"{BASE_URL}{way}", data=payload, **kwargs)
        return resp


async def patch(way: str, headers=None, **kwargs) -> aiohttp.ClientResponse:
    async with aiohttp.ClientSession(headers=headers) as s:
        resp = await s.patch(url=f"{BASE_URL}{way}", **kwargs)
        return resp


async def delete(way: str, headers=None, **kwargs) -> aiohttp.ClientResponse:
    async with aiohttp.ClientSession(headers=headers) as s:
        resp = await s.delete(url=f"{BASE_URL}{way}", **kwargs)
        return resp
