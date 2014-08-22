# -*- coding: utf-8 -*-

# Scrapy settings for images_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'images_scraper'

SPIDER_MODULES = ['images_scraper.spiders']
NEWSPIDER_MODULE = 'images_scraper.spiders'

AUTOTHROTTLE_ENABLED = True
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (X11; Linux i686; rv:23.0) Gecko/20100101 Firefox/23.0'

ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.images.ImagesPipeline': 1
}

IMAGES_STORE = './'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'images_scraper (+http://www.yourdomain.com)'
