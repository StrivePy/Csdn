# -*- coding: utf-8 -*-
import scrapy
from Csdn.items import CsdnItem
from Csdn.items import CsdnItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class CsdnblogSpider(scrapy.Spider):
    name = 'csdnblog'
    allowed_domains = ['csdn.net']
    start_urls = ['http://blog.csdn.net/oscer2016/article/details/78007472']

    def parse(self, response):
        l = CsdnItemLoader(item=CsdnItem(), response=response)
        # 文章url
        l.add_value('url', response.url)
        # 文章标题
        l.add_xpath('title', '//*[@id="mainBox"]//h6/text()')
        # 文章作者
        l.add_xpath('author', '//*[@id="uid"]/text()', MapCompose(str.upper))
        # 文章发行时间
        l.add_xpath('releasetime', '//*[@id="mainBox"]//span[@class="time"]/text()')
        # 文章内容
        # l.add_xpath('content', '//*[@id="article_content"]'.xpath('string(.)'))
        litem = l.load_item()
        yield litem
