# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoinCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    nick_name = scrapy.Field()
    level = scrapy.Field()
    recommend = scrapy.Field()
    non_recommend = scrapy.Field()
    uploaded_time = scrapy.Field()
    context = scrapy.Field()
    view_count = scrapy.Field()