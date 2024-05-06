import os
import subprocess

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from dotenv import load_dotenv


load_dotenv()

IBD_PATH = os.environ['IBD_PATH']

def diagnose() -> str:
    command = f'du -sh {IBD_PATH}'
    return subprocess.check_output(command,
                                   shell=True,
                                   text=True)


if __name__ == '__main__':
    diagnose_results_before: str = diagnose()

    process = CrawlerProcess(settings=get_project_settings())

    process.crawl(crawler_or_spidercls="samsung")
    process.start()

    diagnose_results_after: str = diagnose()
