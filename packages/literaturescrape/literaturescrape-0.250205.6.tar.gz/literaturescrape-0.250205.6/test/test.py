from literaturescrape import sync_summary

from sys import stdout
from literaturescrape.core.settings import logger
logger.remove()
logger.add(stdout, level="DEBUG")

print(sync_summary("10.1007/s10570-024-06297-7"))

