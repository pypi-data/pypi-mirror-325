# Literature Scrape

## Usage

```
from literatureScrape import async_summary, sync_summary


# 设置代理
# import os
# os.environ["LITERATURE_SCRAPE_PROXY"] = "http://127.0.0.1:1080"


# 同步调用
def test_sync():
    print(sync_summary("10.1186/s12967-024-05786-4"))
        

# 异步调用
async def test_async():
    tasks = [asyncio.create_task(async_summary("10.1186/s12967-024-05786-4")) for _ in range(3)]
    ret = await asyncio.gather(*tasks)
    print(ret)
```