# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LinkhomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    no = scrapy.Field()
    number = scrapy.Field()
    fast_link = scrapy.Field()
    style = scrapy.Field()
    floor = scrapy.Field()
    area = scrapy.Field()
    orientation = scrapy.Field()
    age = scrapy.Field()
    building_type = scrapy.Field()
    elevator = scrapy.Field()
    heating = scrapy.Field()
    decoration = scrapy.Field()
    price = scrapy.Field()
    unit_price = scrapy.Field()
    feature = scrapy.Field()
    loan_period = scrapy.Field()
    tax = scrapy.Field()
    total = scrapy.Field()
    down_payment = scrapy.Field()
    community = scrapy.Field()
    around = scrapy.Field()

    pass
