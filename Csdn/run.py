# -*- coding: utf-8 -*-

from scrapy import cmdline
name = 'csdnblog'
cmd = 'scrapy crawl {spider_name}'.format(spider_name=name)
cmdline.execute(cmd.split())
