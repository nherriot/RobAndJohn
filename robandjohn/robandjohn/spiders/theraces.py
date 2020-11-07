import scrapy


class TheracesSpider(scrapy.Spider):
    name = 'theraces'
    allowed_domains = ['www.attheraces.com/']
    start_urls = ['https://www.attheraces.com/racecard/Newcastle/01-June-2020/1300']

    def parse(self, response):

        # XPaths for race details
        race_time = response.xpath('//div[@class="race-header__content js-race-header__content"]/div/div/div/div/h1/b/text()').extract()[0]
        race_date_and_place = response.xpath('//div[@class="race-header__content js-race-header__content"]/div/div/div/div/h1/text()').extract()[1].strip()
        race_class = response.xpath('//div[@class="race-header__content js-race-header__content"]/div/div/div/div/p[2]/text()').extract()[0].strip()
        start_time = response.xpath('//div[@class="card-footer__content"]/div/span/span/text()').extract()[0]
        winning_time = response.xpath('//div[@class="card-footer__content"]/div/span/span[2]/text()').extract()[0]

        self.logger.info(f"\n*** Race details ***\n  Race time: {race_time}\n  Race Course: {race_date_and_place}\n  Race class: {race_class}\n  Race Start Time: {start_time}\n  Race Winning Time: {winning_time}")


        # XPaths for horse and rider details
        positions_selector = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-no-draw"]//span/text()')
        dist_btn = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--form text-align--center"]/text()').extract()
        horse_colours = response.xpath('//div[@class="horse"]//img/@title').extract()
        horse_urls = response.xpath('//div[@class="horse"]//img/@src').extract()
        horse_names = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/div/div/div/h2/a/text()').extract()
        race_descriptions = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/p/span/text()').extract()
        race_ods = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/div/div[2]/text()').extract()
        race_age_weight = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/div/div[3]/text()').extract()
        race_or = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/div/div[4]/span/text()').extract()


        for o_r in race_or:
            self.logger.info(f"Race OR is; {o_r}")

        for age_weight in race_age_weight:
            clean_age_weight = age_weight.strip().replace('\n', '')
            self.logger.info(f"Race age and weight is: {clean_age_weight}")

        for ods in race_ods:
            ods_clean = ods.strip().replace('\n','')
            self.logger.info(f"Race ods are: {ods_clean}")

        for race in race_descriptions:
            self.logger.info(f"Race description: {race.strip()}")

        cleaned_horse_names = []
        for horse in horse_names:
            self.logger.info(f"Horse name is: {horse.strip()} *** String size is: {len(horse.strip())} ***")
            if len(horse.strip()) >= 1:
                # Empty list string from padding characters like /n/r so we can ignore those
                cleaned_horse_names.append(horse.strip())

        self.logger.info(f"\n***Cleaned horse names***\n")
        for horse in cleaned_horse_names:
            self.logger.info(f"Horse name is: {horse.strip()}")

        for db in dist_btn:
            self.logger.info(f"Dist Bin is: {db.strip()}")

        for position in positions_selector:
            self.logger.info(f"Position number is: {position.extract()}")

        for horse_strip, horse_image in zip(horse_colours, horse_urls):
            self.logger.info(f" Horse strip colours is : {horse_strip}")
            self.logger.info(f"and horse image is: {horse_image}")
