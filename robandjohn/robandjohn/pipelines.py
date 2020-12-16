# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import logging
from robandjohn.utils import unpack_list
from robandjohn.createRaceFile import write_race_file
from itertools import zip_longest

class TheRacesPipeline:
    def process_item(self, item, spider):
        logging.info("*** Running Currys Pipeline for MONGO Database ***")

        if spider.name == "theraces":
            if item['race_time']:
                logging.debug(f"Spider name: {unpack_list(item['spider'])}")
                logging.debug(f"Web site scraped: {unpack_list(item['url'])}")
                logging.debug(f"Race Date & Location: {unpack_list(item['race_date_and_place'])}")
                logging.debug(f"Race time: {unpack_list(item['race_time'])}  Actual Start time: {unpack_list(item['race_start_time'])}")
                logging.debug(f"Winning time: {unpack_list(item['race_winning_time'])}")
                logging.debug(f"Race Class: {unpack_list(item['race_class'])}")
                logging.debug(f"Information scraped at: {unpack_list(item['date'])}")

                race_summary = {
                    "spider name": unpack_list(item['spider']),
                    "web site": unpack_list(item['url']),
                    "race title": unpack_list(item['race_date_and_place']),
                    "race time": unpack_list(item['race_time']),
                    "start time": unpack_list(item['race_start_time']),
                    "winning time": unpack_list(item['race_winning_time']),
                    "race class": unpack_list(item['race_class']),
                    "scrape time": unpack_list(item['date'])
                }

                # calculate age and weight from list
                horse_ages = []
                horse_weights = []
                for loop_counter, age_weight in enumerate(item['race_age_weight']):
                    if (loop_counter % 2) == 0:
                        horse_ages.append(age_weight)
                    else:
                        horse_weights.append(age_weight)

                race_details = zip_longest(item['horse_name'],
                                           item['horse_number'],
                                           item['position'],
                                           item['race_ods'],
                                           item['dst_btn'],
                                           horse_ages,
                                           horse_weights,
                                           item['horse_colour'])

                write_race_file(race_summary, race_details)


        return item


class RobandjohnPipeline:
    def process_item(self, item, spider):

        logging.info("\n\n ***** HELLO WORLD ! *****")
        return item


