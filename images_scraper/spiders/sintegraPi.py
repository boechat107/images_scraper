from scrapy import Spider
from images_scraper.spiders.base_spider import BaseSpider

class sintegraPiSpider(BaseSpider):
    name = "sintegraPi"
    base_url = 'http://webas.sefaz.pi.gov.br/SintegraConsultaPublica'

    def __init__(self, *args, **kwargs):
        super(sintegraPiSpider, self).__init__(base_url=self.base_url, 
                                               *args, **kwargs)

    def parse(self, response):
        ## Parsing the captcha's image url.
        sel = response.selector 
        img_addr = sel.xpath('//img[@id="_captcha_cognitivo_image"]/@src').extract()[0]
        ## Getting the complete url.
        img_url = self.base_url + img_addr
        ## Using the Images Pipeline, we just need to create an Item.
        return self.create_image_item(img_url)
