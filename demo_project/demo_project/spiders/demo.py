# -*- coding: utf-8 -*-
import scrapy
from scrapy.exception import CloseSpide
import json
import time

# $ scrapy crawl demo -o data.json -a id ="test"
class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['www.demo.com']
    url = 'http://www.demo.com/'
    timestamp = int(time.time())
    
    cookies = {
        'key': 'value'
        'timestamp':timestamp
    }

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse_id,
                                cookies=self.cookies)

    def parse_id(self, response):
        data = json.loads(response.body)
        # view the raw json response
        with open('sample.json', 'w') as file:
            file.write(json.dumps(data))

        page_urls = data.get('key')
        if page_urls is None:
            raise CloseSpide("No result available in this id")

        for page_url in page_urls:
            yield scrapy.Request(url='http://www.demo{0}.com'.format(self.id),callback=self.parse,
                                cookies=self.cookies)

        pagination_metadata = data.get('pagination_key')

        if pagination_metadata.get('has_next_page'):
            next_page_id = pagination_metadata.get('next_page')
            yield scrapy.Request(url='http://www.demo.com{0}'.format(next_page_id), callback=self.parse_id)

    def parse(self, response):
        page = json.loads(response.body).get('key')
        yield {
            'key': page.get('key')
        }
