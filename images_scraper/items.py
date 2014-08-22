# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagesScraperItem(scrapy.Item):
    ## Following the idea of http://doc.scrapy.org/en/latest/topics/images.html
    image_urls = scrapy.Field()
    images = scrapy.Field()
