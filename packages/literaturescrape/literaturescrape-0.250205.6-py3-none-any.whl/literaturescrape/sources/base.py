
import asyncio
from literaturescrape.core.settings import logger

from abc import ABC, abstractmethod
from literaturescrape.core.models import Literature, Response
from typing import Optional


class BaseScraper(ABC):
    def __init__(self, name:str):
        self.name = name
        self.priority = 0  # 优先级
    
    @abstractmethod
    async def _fetch(self, doi:str) -> str:
        pass
    
    @abstractmethod
    def _extract(self, data:str) -> Optional[Literature]:
        pass
    
    async def execute(self, doi:str) -> Optional[Response]:
        response = Response(source=self.name)
        
        data = None
        
        try:
            data = await self._fetch(doi)
        except Exception as e:
            logger.debug(f"[{self.name}] [{doi}] {e}")
            response.fetch_flag = False
            response.fetch_err_reason = str(e)
        else:
            response.fetch_flag = True
        
        if data:
            try:
                literature = await asyncio.to_thread(self._extract, data)
            except Exception as e:
                logger.debug(f"[{self.name}] [{doi}] {e}")
                response.extract_flag = False
                response.extract_err_reason = str(e)
            else:
                response.extract_flag = True
                
                if isinstance(literature, Literature):
                    response.finished = True
                    
                response.literature = literature
        
        response.priority = self.priority
                
        return response