import asyncio
import sys

import aiohttp

async def links_test(links):
    """Given a list of valid URL links,
    return all links that do not return a 200 status code using HTTP GET requests"""
    failures = []
    for link in links:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                if response.status != 200:
                    failures.append(response)
    return failures

def run(links):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(links_test(links))

if __name__ == '__main__':
    fails = run(sys.argv[1:])
    for f in fails:
        print(f.url, f.status)
