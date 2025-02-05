import asyncio
from literaturescrape.core.settings import logger

# 兼容windows系统
import sys
if sys.platform == "win32":
    from asyncio.windows_events import WindowsSelectorEventLoopPolicy
    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

from literaturescrape.core.models import Response, Literature
from literaturescrape.sources import BaseScraper, OpenAlexScraper, ThirdironScraper


scraper_list: list[BaseScraper] = [OpenAlexScraper(), ThirdironScraper()]



def select_best_match(results: list[Response]) -> dict | None:
    # 选择最佳匹配
    best_result = Literature()
    
    if results:
        ret = sorted(results, key=lambda x: x.priority, reverse=True)
        for key in best_result.__dict__:
            for item in ret:
                if item.literature:
                    value = getattr(item.literature, key)
                    if value:
                        setattr(best_result, key, value)
                        logger.debug(f"[{item.source}] {key} : {value}")
                        break
        return best_result.to_dict()
    else:
        return None


async def async_summary(doi: str) -> dict | None:
    tasks = [asyncio.create_task(scraper.execute(doi)) for scraper in scraper_list]
    results: list[Response | None] = await asyncio.gather(*tasks)
    
    # 过滤失败的请求
    succeed_results:list[Response] = [item for item in results if item is not None and item.literature is not None]
    literature = select_best_match(succeed_results)
    return literature


def sync_summary(doi: str) -> dict | None:
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    info = loop.run_until_complete(async_summary(doi))
    return info


