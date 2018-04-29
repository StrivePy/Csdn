# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class CsdnPipeline(object):
    def process_item(self, item, spider):
        data = re.search('https://blog.csdn.net/oscer2016/article/details/(.*)', item['url']).group(1)
        file_name = '{0}_{1}.txt'.format(item['author'], data)
        text = "标题：" + item['title'] + "\n作者： " + item['author'] + "\n文章地址： " + item['url'] + "\n发布时间： "\
               + item['release_time'] + "\n\n正文： " + item['content']
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(text)
        return item
