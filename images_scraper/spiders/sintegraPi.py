from scrapy import Spider
from images_scraper.items import ImagesScraperItem

class sintegraPiSpider(Spider):
    name = "sintegraPi"
    base_url = 'http://webas.sefaz.pi.gov.br/SintegraConsultaPublica'
    start_urls = [base_url]

    def parse(self, response):
        ## Parsing the captcha's image url.
        sel = response.selector 
        img_addr = sel.xpath('//img[@id="_captcha_cognitivo_image"]/@src').extract()[0]
        ## Getting the complete url.
        img_url = self.base_url + img_addr
        ## Using the Images Pipeline, we just need to create an Item.
        item = ImagesScraperItem()
        item['image_urls'] = [img_url]
        return item
