# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class CsdnItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class CsdnItem(Item):
    title = Field()
    url = Field()
    releasetime = Field()
    author = Field(
        # input_processor=MapCompose(str.upper)
    )
    content = Field()
