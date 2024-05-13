import aiohttp
from urllib.parse import quote

class DeloreanPremium():
    async def get(self, *, url, api_key, advanced_mode=False):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://dlr-api.woozym.workers.dev/?url={quote(url)}", headers={"x-api-key": api_key}) as response:
                if response.status != 200:
                    return await response.text()
                try:
                    r = await response.json()
                    if advanced_mode:
                        return r
                    return r["result"]
                except Exception as e:
                    print(e)
                    return "API is currently offline or down. Please try again later."
                
class DeloreanFree():
    async def get(self, *, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://delorean-free-api.woozym.workers.dev/api/linkvertise?url={quote(url)}") as response:
                if response.status != 200:
                    return await response.text()
                try:
                    r = await response.json()
                    return r["result"]
                except Exception as e:
                    print(e)
                    return "API is currently offline or down. Please try again later."
                
class DeloreanOwner():
    async def get(self, url, api_key,advanced_mode=True):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://localhost:4685/?url={quote(url)}", headers={"x-api-key": api_key}) as response:
                if response.status != 200:
                    return await response.text()
                try:
                    r = await response.json()
                    if advanced_mode:
                        return r
                    return r["result"]
                except Exception as e:
                    print(e)
                    return "API is currently offline or down. Please try again later."       