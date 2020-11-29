
import socket
from datetime import datetime, timezone

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import Join, MapCompose, TakeFirst
from robandjohn.items import HorseRaceItem

class TheracesSpider(scrapy.Spider):
    name = 'theraces'

    # Set to 'False' to ignore robot.txt file.
    custom_settings = {
        "ROBOTSTXT_OBEY": "True",
    }

    allowed_domains = ['www.attheraces.com/']
    start_urls = ['https://www.attheraces.com/racecard/Newcastle/01-June-2020/1300']

    housekeeping = {}

    def parse(self, response):

        # Lets instantiate one of our horse race items.
        itemLoader = ItemLoader(item=HorseRaceItem(), response=response)

        # First lets do housekeeping data for this web spider scrape. We need to check it is only done once.
        # So only happens for the first asynchronous block of code to run (scrapy uses twisted!). Store the value in
        # the class attribute so that it can be used by every item that is parsed.
        if not self.housekeeping:
            self.housekeeping["url"] = response.url
            self.housekeeping["project"] = self.settings.get("BOT_NAME")
            self.housekeeping["spider"] = self.name
            self.housekeeping["server"] = socket.gethostname()
            self.housekeeping["date"] = (
                datetime.now()
                .replace(tzinfo=timezone.utc)
                .strftime("%d %B %Y %H:%M:%S")
            )
            self.logger.info(
                f"*** The housekeeping attributes are now data filled with: {self.housekeeping} ***"
            )

        # Set housekeeping attributes in the HorseRaceItem
        itemLoader.add_value('url', response.url)
        itemLoader.add_value('project', self.settings.get("BOT_NAME"))
        itemLoader.add_value('spider', self.name)
        itemLoader.add_value('server', socket.gethostname())
        itemLoader.add_value('date', datetime.now().replace(tzinfo=timezone.utc).strftime("%d %B %Y %H:%M:%S"))

        # XPaths for race details
        itemLoader.add_xpath('race_time', '//div[@class="race-header__content js-race-header__content"]/div/div/div/div/h1/b/text()')
        itemLoader.add_xpath('race_date_and_place', '//div[@class="race-header__content js-race-header__content"]/div/div/div/div/h1/text()', MapCompose(str.strip), lambda  i: i[1])
        itemLoader.add_xpath('race_class', '//div[@class="race-header__content js-race-header__content"]/div/div/div/div/p[2]/text()', MapCompose(str.strip), lambda i: i[0])
        itemLoader.add_xpath('race_start_time', '//div[@class="card-footer__content"]/div/span/span/text()', lambda i: i[0])
        itemLoader.add_xpath('race_winning_time', '//div[@class="card-footer__content"]/div/span/span[2]/text()', lambda i: i[0])

        # XPaths for horse and rider details
        itemLoader.add_xpath('position', '//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-no-draw"]//span/text()')
        itemLoader.add_xpath('horse_url', '//div[@class="horse"]//img/@src')
        itemLoader.add_xpath('race_or', '//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/div/div[4]/span[1]/text()')
        itemLoader.add_xpath('horse_colour', '//div[@class="horse"]//img/@title')
        itemLoader.add_xpath('raced_description', '//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/p/span/text()', MapCompose(str.strip))
        itemLoader.add_xpath('horse_name', '//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/div/div/div/h2/a/text()', MapCompose(str.strip, lambda i: i if(len(i)>=1) else None))
        itemLoader.add_xpath('dst_btn', '//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--form text-align--center"]/text()', MapCompose(lambda i: i.replace('\r', '').replace('\n', ''), str.strip))
        itemLoader.add_xpath('race_ods', '//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/div/div[2]/text()', MapCompose(lambda i: i.replace('\r', '').replace('\n', ''), str.strip))
        itemLoader.add_xpath('race_age_weight', '//*[@id="tab-full-result"]/div/div/div/div[2]//div/div/div[4]/div/div[3]/text()', MapCompose(str.split))

        return itemLoader.load_item()
