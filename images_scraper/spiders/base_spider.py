from scrapy import Spider
from images_scraper.items import ImagesScraperItem

class BaseSpider(Spider):
    start_urls = None

    def __init__(self, runtimes=1, base_url=None, *args, **kwargs):
        super(BaseSpider, self).__init__(*args, **kwargs)
        ## Replicates the base_url N runtimes.
        self.start_urls = [base_url] * runtimes
    
    @staticmethod
    def create_image_item(*urls):
        item = ImagesScraperItem()
        item['image_urls'] = list(urls)
        return item
