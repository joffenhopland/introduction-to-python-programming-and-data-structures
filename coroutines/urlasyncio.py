import asyncio
import time
import aiohttp
import sys
import selectors

if sys.platform:
    selector = selectors.SelectSelector()
    loop = asyncio.SelectorEventLoop(selector)
    asyncio.set_event_loop(loop)

async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

async def main():
        sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice"
        ] * 80
        start_time = time.time()
        await download_all_sites(sites)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} sites in {duration} seconds")
 
asyncio.run(main())

