# -*- coding: utf-8 -*-
import scrapy
import logging
from Csdn.items import CsdnItem

logger = logging.getLogger(__name__)


class CsdnblogSpider(scrapy.Spider):
    name = 'csdnblog'
    allowed_domains = ['csdn.net']
    start_urls = ['http://blog.csdn.net/oscer2016/article/details/78007472']

    def parse(self, response):
        item = CsdnItem()
        # 文章url
        url = response.url
        # 文章标题
        title = response.xpath('//*[@id="mainBox"]//h6/text()').extract_first()
        # 文章作者
        author = response.xpath('//*[@id="uid"]/text()').extract_first()
        # 文章发行时间
        release_time = response.xpath('//*[@id="mainBox"]//span[@class="time"]/text()').extract_first()
        # 文章内容
        content = response.xpath('//*[@id="article_content"]').xpath('string(.)').extract_first()
        for field in item.fields:
            try:
                item[field] = eval(field)
            except NameError:
                logger.error('name %s is not defined', field)
        yield item
