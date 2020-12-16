# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class HorseRaceItem(Item):
    # Primary Fields
    race_time = Field()
    race_date_and_place = Field()
    race_class = Field()
    race_start_time = Field()
    race_winning_time = Field()

    # Race Data Fields
    position = Field()
    dst_btn = Field()
    horse_colour = Field()
    horse_url = Field()
    horse_name = Field()
    horse_number = Field()
    raced_description = Field()
    race_ods = Field()
    race_age_weight = Field()
    race_or = Field()


    # Calculated Fields
    images = Field()
    location = Field()

    # Housekeeping Fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()



class RobandjohnItem(Item):

    # Calculated Fields
    images = Field()
    location = Field()

    # Housekeeping Fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()

