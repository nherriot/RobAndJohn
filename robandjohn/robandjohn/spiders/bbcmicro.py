import scrapy
from itertools import zip_longest


def zip_equal(*iterables):
    """
    Like the in-built `zip`, but checks iterables are of the same length.

    Implementation of zip_equal from more_itertools.
    This is to avoid having an external import.
    Credit to https://stackoverflow.com/a/32954700.
    """
    sentinel = object()
    for combo in zip_longest(*iterables, fillvalue=sentinel):
        if sentinel in combo:
            raise ValueError("Iterables have different lengths")
        yield combo



class BbcmicroSpider(scrapy.Spider):
    name = 'bbcmicro'
    allowed_domains = ['web']
    start_urls = ['http://bbcmicro.co.uk/']

    def parse(self, response):

        # Pull title out of main page.
        titles = response.xpath('//span[@class="row-title"]/a/text()').extract()
        publishers = response.xpath('//div[@class="row-pub"]/a[1]/text()').extract()
        dates = response.xpath('//div[@class="row-dt"]/a/text()').extract()

        self.logger.debug(f"*** Titles length is: {len(titles)}")
        self.logger.debug(f"*** Publishers length is: {len(publishers)}")
        self.logger.debug(f"*** Dates length is: {len(dates)}")

        items = zip_equal(
            titles,
            publishers,
            dates)

        for title, publisher, date in items:

            self.logger.debug(f"Title is: {title}. Published is: {publisher}. Date is: {date}")





