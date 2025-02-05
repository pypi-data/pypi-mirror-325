import sys
from literaturescrape.core.settings import logger
logger.remove()
logger.add(sys.stdout, level="INFO")

from .run import sync_summary, async_summary



