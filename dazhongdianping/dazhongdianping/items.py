# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class ShopsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()              #店名
    # shop_url = Field()
    shop_URL = Field()          #店铺URL
    comment_counts = Field()    #店铺评论数
    avgprice = Field()          #人均费用
    taste = Field()             #口味评分
    environment = Field()       #环境评分
    service = Field()           #服务评分
    title = Field()             #类型
    district = Field()          #商区
    address = Field()           #地址

class CommentItem(Item):
    name = Field()          #店铺
    comment = Field()       #评论
    star = Field()
