import scrapy


class TheracesSpider(scrapy.Spider):
    name = 'theraces'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    def parse(self, response):
        pass
