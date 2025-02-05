import os
from literaturescrape.core.settings import logger
from urllib.parse import quote
from curl_cffi.requests import AsyncSession
from literaturescrape.core.models import Literature

from literaturescrape.sources import BaseScraper


class ThirdironScraper(BaseScraper):
    def __init__(self):
        self.name = "thirdiron"
        self.priority = 9

    async def _fetch(self, doi: str):
        async with AsyncSession(impersonate='chrome119', verify=False, timeout=15) as client:
            query = quote(f"doi:{doi}", safe='')
            url = f"https://api.thirdiron.com/v2/articles/{query}?include=issue%2Cjournal&reload=true"
            resp = await client.get(url, headers={'Authorization': 'Bearer 190f1a5d-5685-4b77-ba52-ee25d697542e'})
            ret = resp.json()
            return ret
    
    def _extract(self, data: dict):
        additional_data = {}
        
        included = data.get("included", [])
        data = data["data"]["attributes"]
        
        try:
            start_page = data.get("startPage", '').strip()
            end_page = data.get("endPage", '').strip()
            pages = f"{start_page}-{end_page}" if start_page and end_page else start_page
            author = ", ".join([" ".join(au.split(", ", 1)[::-1]) for au in data["authors"].split("; ")])
            
            additional_data["pages"] = pages
            additional_data["author"] = author
        except:
            pass
        
        
        for item in included:
            if item["type"] == "issues":
                additional_data["volume"] = item['volume']
                additional_data["issue"] = item['number']
                
            elif item["type"] == "journals": 
                additional_data["jour_name"] = item['attributes']['title']
                
                issn = item['attributes']['issn']
                if issn:
                    additional_data["jour_issn"] = issn[:4] + "-" + issn[4:]
                
        
        return Literature(
            title=data["title"],
            doi=data["doi"],
            pmid=data["pmid"],
            jour_name=additional_data.get("jour_name"),
            jour_issn=additional_data.get("jour_issn"),
            openAccess=data["openAccess"],
            publish_date=data["date"],
            year=data["date"][:4],
            volume=additional_data.get("volume"),
            issue=additional_data.get("issue"),
            page=additional_data.get("pages"),
            abstract=data.get("abstract"),
            author=additional_data.get("author"),
        )
    
    
if __name__ == "__main__":
    import asyncio
    scraper = ThirdironScraper()
    ret = asyncio.run(scraper.execute("10.1186/s12967-024-05786-4"))
    print(ret)