import asyncio

# 兼容windows系统
import sys
if sys.platform == "win32":
    from asyncio.windows_events import WindowsSelectorEventLoopPolicy
    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

from literaturescrape.core.models import Response, Literature
from literaturescrape.sources import BaseScraper, OpenAlexScraper, ThirdironScraper


scraper_list: list[BaseScraper] = [OpenAlexScraper(), ThirdironScraper()]

async def async_summary(doi: str) -> dict | None:
    tasks = [asyncio.create_task(scraper.execute(doi)) for scraper in scraper_list]
    results: list[Response | None] = await asyncio.gather(*tasks)
    
    # 过滤失败的请求
    succeed_results:list[Response] = [item for item in results if item is not None and item.literature is not None]
    ret = sorted(succeed_results, key=lambda x: x.priority, reverse=True)
    # todo: 选择最佳匹配
    if ret:
        literature:Literature = ret[0].literature # type: ignore
        return literature.to_dict()
    else:
        return None


def sync_summary(doi: str) -> dict | None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    info = loop.run_until_complete(async_summary(doi))
    return info


