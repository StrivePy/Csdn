# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class CsdnPipeline(object):

    def process_item(self, item, spider):
        data = re.search('https://blog.csdn.net/oscer2016/article/details/(.*)', item.get('url')).group(1)
        file_name = '{0}_{1}.txt'.format(item.get('author'), data)
        base_text = "标题：{title}\n作者：{author}\n文章地址：{url}\n发布时间：{releasetime}\n\n正文："
        text = base_text.format(title=item.get('title'),
                                author=item.get('author'),
                                url=item.get('url'),
                                releasetime=item.get('releasetime'))
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(text)
        return item
