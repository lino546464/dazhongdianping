# -*- coding: utf-8 -*-
from scrapy import Spider,Selector,Request
from ..items import ShopsItem,CommentItem
import time

start = time.time()
class DianpingSpider(Spider):

    name = "dianping"
    allowed_domains = ["dianping.com"]
    base_url = 'http://www.dianping.com'
    # start_urls = (
    #     # 'https://www.dianping.com/search/category/1/10',
    #     'http://www.dianping.com/shop/5275754'
    # )
    # def start_requests(self):
    #     for i in range(1,10):
    #         url = self.base_url + '/search/category/1/10/p' + str(i)
    #         yield Request(url,self.parse)

    def parse(self, response):
        select = Selector(response)
        shops = select.xpath('//div[@id="shop-all-list"]/ul/li/div[@class="txt"]')
        for shop in shops:
            name = shop.xpath('div[1]/a/h4/text()').extract()[0]
            shop_url = shop.xpath('div[1]/a/@href').extract()[0]
            shop_URL = self.base_url + shop_url
            title = shop.xpath('div[3]/a[1]/span/text()').extract()[0]
            district = shop.xpath('div[3]/a[2]/span/text()').extract()[0]
            comment_url = shop_URL + '/review_more'
            # print(name,shop_URL)
            yield Request(comment_url, self.parse_comment, meta={'name': name,
                                                                 'comment_url': comment_url})
            # yield Request(shop_URL,self.parse_detail,meta={'title':title,
            #                                                'district':district})
        # next_page = select.xpath('//div[@class="page"]/a[@class="next"]')
        # if next_page:
        #     next_url = select.xpath('//div[@class="page"]/a[@class="next"]/@href').extract()[0]
        #     next_URL = self.base_url + next_url
        #     print(next_URL)
        #     yield Request(next_URL, self.parse)
        # else:
        #     print('店铺抓取结束！')
        #     end = time.time()
        #     print('共耗时{}s'.format(end - start))
    '''
    def parse_detail(self, response):
        item = ShopsItem()
        title = response.meta['title']
        district = response.meta['district']
        select = Selector(response)
        shop = select.xpath('//div[@class="main"]/div[@id="basic-info"]')
        #shops = select.xpath('//div[@id="shop-all-list"]/ul/li/div[@class="txt"]')

        name = shop.xpath('h1[@class="shop-name"]/text()').extract()[0]
        # shop_url = shop.xpath('div[1]/a/@href').extract()[0]
        # shop_URL = self.base_url + shop_url
        comment_counts = shop.xpath('div[@class="brief-info"]/span[@id="reviewCount"]/text()').extract()[0]
        avgprice = shop.xpath('div[@class="brief-info"]/span[@id="avgPriceTitle"]/text()').extract()[0]
        taste = shop.xpath('div[@class="brief-info"]/span[@id="comment_score"]/span[1]/text()').extract()[0]
        environment = shop.xpath('div[@class="brief-info"]/span[@id="comment_score"]/span[2]/text()').extract()[0]
        service = shop.xpath('div[@class="brief-info"]/span[@id="comment_score"]/span[3]/text()').extract()[0]
        # title = shop.xpath('div[3]/a[1]/span/text()').extract()[0]
        # district = shop.xpath('div[3]/a[2]/span/text()').extract()[0]
        address = shop.xpath('div[@itemprop="street-address"]/span[@class="item"]/text()').extract()[0]
        # comment_url = shop_URL + '/review_more'
        item['name'] = name
        # item['shop_URL'] = shop_URL
        item['comment_counts'] = comment_counts
        item['avgprice'] = avgprice
        item['taste'] = taste
        item['environment'] = environment
        item['service'] = service
        item['title'] = title
        item['district'] = district
        item['address'] = address
        yield item
            # yield Request(comment_url,self.parse_comment,meta={'name':name,
            #                                                    'comment_url':comment_url})
        print(name,comment_counts,avgprice,taste,environment,service,title,district,address)

        # next_page = select.xpath('//div[@class="page"]/a[@class="next"]')
        # if next_page:
        #     next_url = select.xpath('//div[@class="page"]/a[@class="next"]/@href').extract()[0]
        #     next_URL = self.base_url + next_url
        #     print(next_URL)
        #     yield Request(next_URL,self.parse)
        # else:
        #     print('店铺抓取结束！')
        '''

    def start_requests(self):
        comment_url = 'http://www.dianping.com/shop/5275754/review_more_4star'
        yield Request(comment_url,self.parse_comment,meta={'comment_url':comment_url})

    def parse_comment(self, response):
        # name = response.meta['name']
        comment_url = response.meta['comment_url']
        item = CommentItem()
        # name = '耶里夏丽'
        select = Selector(response)
        comment_list = select.xpath('//div[@class="comment-list"]/ul/li/div[@class="content"]')
        for comments in comment_list:
            comment = comments.xpath('div[@class="comment-txt"]/div/text()').extract()[0]
            star = comments.xpath('div[@class="user-info"]/span[1]/@title').extract()[0]
            item['comment'] = str(comment).strip()
            item['star'] = str(star).strip()
            # item['name'] = name
            print(str(comment).strip(),str(star).strip())
            yield item
            #print(comment)

        next_page = select.xpath('//div[@class="Pages"]/div/a[@class="NextPage"]')
        if next_page:
            next_url = next_page.xpath('@href').extract()[0]
            next_URL = comment_url + next_url
            print(next_URL)
            yield Request(next_URL,self.parse_comment,meta={'comment_url':comment_url})

        else:
            print('评论抓取完毕！')

        end = time.time()
        print('共耗时{}s'.format(end-start))

