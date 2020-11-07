import scrapy


class TheracesSpider(scrapy.Spider):
    name = 'theraces'
    allowed_domains = ['www.attheraces.com/']
    start_urls = ['https://www.attheraces.com/racecard/Newcastle/01-June-2020/1300']

    def parse(self, response):

        response.xpath(
            '//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-no-draw"]//span/text()').extract()


        positions_selector = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-no-draw"]//span/text()')
        dist_btn = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--form text-align--center"]/text()').extract()
        horse_colours = response.xpath('//div[@class="horse"]//img/@title').extract()
        horse_urls = response.xpath('//div[@class="horse"]//img/@src').extract()
        horse_names = response.xpath('//div[@class="tabs__content"]//div[@class="card-body"]//div[@class="card-entry "]//div[@class="card-cell card-cell--fill unpadded-left"]/div/div/div/h2/a/text()').extract()

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
            self.logger.info(f"Dist Bin is: {db}")

        for position in positions_selector:
            self.logger.info(f"Position number is: {position.extract()}")

        for horse_strip, horse_image in zip(horse_colours, horse_urls):
            self.logger.info(f" Horse strip colours is : {horse_strip}")
            self.logger.info(f"and horse image is: {horse_image}")
