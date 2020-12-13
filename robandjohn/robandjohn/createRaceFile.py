# Utility function to write output for 'theraces' spider


import os
from datetime import datetime
import logging



def write_race_file(summary, race_details):

    logging.debug("***** running the write race file function *****")
    try:
        file_name = "Race_" + summary['race title'].replace(" ", "_") + ".txt"
        logging.info(f"File name is: {file_name}")

    except KeyError:
        logging.error("Expected parameters don't exist for this race. We need a race title and date to write or file")

    else:

        if os.path.exists(file_name):
            logging.debug("File exists already updating")
            with open(file_name, 'a') as updating_file:
                updating_file.write(f" \n********** Updating File - Written at: {datetime.now()} **********")
                updating_file.write(f" \n\nRace Details\n")
                updating_file.write(" Position   Horse Name             Odds       Age   Weight   Dst Btn\n")
                updating_file.write(
                    " -----------------------------------------------------------------------------------\n")

                for name, position, odds, btn, age, weight, colour in race_details:
                    updating_file.write(f"   {position:<8} {name:<22} {odds:<10} {age:<5} {weight:<10} {btn:<1} \n")
                updating_file.write(
                    " -----------------------------------------------------------------------------------\n")

        else:
            with open(file_name, 'w') as race_file:
                race_file.write(
                    " ****************************** Johns Horse Race File ******************************\n")
                race_file.write(
                    " ***********************************************************************************\n")
                race_file.write(" Race Summary\n")
                race_file.write(
                    " -----------------------------------------------------------------------------------\n")
                race_file.write(f" Race Title:      {summary['race title']}\n")
                race_file.write(f" Race Website:    {summary['web site']}\n")
                race_file.write(f" Race Time:       {summary['race time']}\n")
                race_file.write(f" Actual Start:    {summary['start time']}\n")
                race_file.write(f" Race Class:      {summary['race class']}\n")
                race_file.write(f" Winning Time:    {summary['winning time']}\n")
                race_file.write(f" Spider name:     {summary['spider name']}\n")
                race_file.write(f" Scraped at:      {summary['scrape time']}\n")
                race_file.write(
                    " -----------------------------------------------------------------------------------\n")
                race_file.write(f" \n\nRace Details - Written at: {datetime.now()}\n")
                race_file.write(" Position   Horse Name             Odds       Age   Weight   Dst Btn\n")
                race_file.write(
                    " -----------------------------------------------------------------------------------\n")

                for name, position, odds, btn, age, weight, colour in race_details:
                    race_file.write(f"   {position:<8} {name:<22} {odds:<10} {age:<5} {weight:<10} {btn:<1} \n")
                race_file.write(
                    " -----------------------------------------------------------------------------------\n")





