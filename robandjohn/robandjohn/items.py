# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class RobandjohnItem(scrapy.Item):
    # Primary Fields

    # Calculated Fields
    images = Field()
    location = Field()

    # Housekeeping Fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
