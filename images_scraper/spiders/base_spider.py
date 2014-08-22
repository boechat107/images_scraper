from scrapy import Spider
from scrapy.http import Request
from images_scraper.items import ImagesScraperItem

class BaseSpider(Spider):
    start_urls = None
    base_url = None
    runtimes = None
    exec_times = 0

    def __init__(self, runtimes='1', base_url=None, *args, **kwargs):
        super(BaseSpider, self).__init__(*args, **kwargs)
        self.runtimes = int(runtimes)
        self.base_url = base_url
        self.start_urls = [base_url]
    
    def create_image_item(self, *urls):
        item = ImagesScraperItem()
        item['image_urls'] = list(urls)
        ## Counting how many times the scraper was executed.item
        self.exec_times += 1
        ## If it reached the maximum number of times, just an item is returned.
        ## Otherwise, an item and a new Request are returned.
        if self.exec_times < self.runtimes:
            return item, Request(url=self.base_url, dont_filter=True)
        return item
