import scrapy


class BbcmicroSpider(scrapy.Spider):
    name = 'bbcmicro'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    def parse(self, response):
        pass
