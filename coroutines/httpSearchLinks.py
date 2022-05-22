import asyncio
import time
import aiohttp
import re
import urllib.error
import urllib.parse
import sys
import selectors

if sys.platform:
    selector = selectors.SelectSelector()
    loop = asyncio.SelectorEventLoop(selector)
    asyncio.set_event_loop(loop)
    
HREF_RE = re.compile(r'href="(.*?)"')

async def download_site(session, url):
    found = set()
    async with session.get(url) as response:
        # print("Read {0} from {1}".format(response.content_length, url))
        html = await response.text()
        # print(html)
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                print("Error parsing URL: %s", link)
                pass
            else:
                found.add(abslink)
        print("Found {0}  links for{1} ".format(len(found), url))
        for p in found:
            print(f"{url}\t{p}\n")


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

async def main():
        sites = [
        "https://www.uit.no/startsida",
        "http://olympus.realpython.org/dice",
        ] * 1
        start_time = time.time()
        await download_all_sites(sites)
        duration = time.time() - start_time
        print(f"Downloaded {len(sites)} sites in {duration} seconds")
 
asyncio.run(main())

