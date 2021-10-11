"""
Send GET requests to a collection of http links,
returning those links which do not return 200 OK
When run directly, take links as cli arguments
"""
import asyncio
import sys
import aiohttp

CONCURRENCY = 16


async def fetch(session, lock, url):
    """
    Locked async HTTP GET
    """
    async with lock:
        return await session.get(url)


async def main(links):  # pylint: disable=redefined-outer-name
    """
    Send GET requests for link in links, return responses of requests
    which do not return 200 OK. Semaphore limits number of concurrent
    requests for performance reasons while remaining non-blocking
    """
    lock = asyncio.Semaphore(CONCURRENCY)
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(
                *[fetch(session, lock, url) for url in links]
                )
        failures = [r for r in responses if r.status != 200]  # pylint: disable=redefined-outer-name
        return failures


if __name__ == '__main__':
    links = sys.argv[1:]
    failures = asyncio.run(main(links))
    for fail in failures:
        print(fail.url, fail.status)
