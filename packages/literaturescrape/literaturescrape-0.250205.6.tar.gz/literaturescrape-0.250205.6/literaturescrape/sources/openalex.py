import os
from literaturescrape.core.settings import logger
from curl_cffi.requests import AsyncSession
from literaturescrape.core.models import Literature

from literaturescrape.sources import BaseScraper


class OpenAlexScraper(BaseScraper):
    def __init__(self):
        self.name = "openalex"
        self.priority = 5

    async def _fetch(self, doi: str):
        async with AsyncSession(impersonate='chrome119', verify=False, timeout=15, proxy=os.environ.get("LITERATURE_SCRAPE_PROXY")) as client:
            url = f"https://api.openalex.org/works/doi:{doi}"
            resp = await client.get(url)
            # logger.debug(f"Fetching {url} status: {resp.status_code}, {resp.text[:50]}")
            resp.raise_for_status()
            ret = resp.json()
            return ret
    
    def _extract(self, data: dict):
        biblio = data.get("biblio") or dict()

        pages = [str(page) for page in [biblio.get("first_page"), biblio.get("last_page")] if page is not None]
        if len(pages)==2 and pages[0]==pages[1]:
            pages = [pages[0]]
        pages = " - ".join(pages)

        absLst = data.get("abstract_inverted_index")
        if absLst:
            absMap = {}
            for value, inx in absLst.items():
                absMap.update({key:value for key in inx})
            abstract = " ".join([word[1] for word in sorted(absMap.items(), key=lambda item: item[0])])
        else:
            abstract = ""

        doi = data.get("ids", {}).get("doi", "").removeprefix('https://doi.org/')

        additional_info = {}
        
        try:
            pmid = data.get("ids", {}).get("pmid")
            if pmid:
                additional_info["pmid"] = pmid.removeprefix('https://pubmed.ncbi.nlm.nih.gov/')
            
            additional_info["journal_name"] = data.get("primary_location", {}).get("source", {}).get("display_name")
            additional_info["jour_issn"] = data.get("primary_location", {}).get("source", {}).get("issn_l")
            additional_info["is_oa"] = data.get("open_access", {}).get("is_oa")
            additional_info["author"] = ", ".join([au["author"]["display_name"] for au in data.get("authorships", [])])
        except:
            # 这些附加数据, 失败了就不管了
            pass
        

        return Literature(
            title=data["title"],
            doi=doi,
            pmid=additional_info.get("pmid"),
            jour_name=additional_info.get("journal_name"),
            jour_issn=additional_info.get("jour_issn"),
            openAccess=additional_info.get("is_oa", False),
            publish_date=data.get("publication_date"),
            year=data.get("publication_year"),
            volume=biblio.get("volume") or "",
            issue=biblio.get("issue") or "",
            page=pages,
            abstract=abstract,
            author=additional_info.get("author")
        )
    
    
if __name__ == "__main__":
    import asyncio
    scraper = OpenAlexScraper()
    ret = asyncio.run(scraper.execute("10.1186/s12967-024-05786-4"))
    print(ret)