import time
import datetime
import logging
import argparse

""" Selenium packages imports"""
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from BaseClass import BaseClass
"""Below are Page Object classes of DRI Functionality"""
from DRICatalog import DRICatalog
from DRILoginPage import DRILoginPage

"""
Developed By: Prankur Garg
Date: 18th July 2022
"""

class DRIMain(BaseClass):
    def __init__(self):
        self._login_page = DRILoginPage(self.driver)
        self.driver.get("https://dri-portal.cec.lab.emc.com/local-login")
        self._dri_catalog = DRICatalog(self.driver)
        today_date = datetime.datetime.now()
        today_date = today_date.strftime("%y%m%d")
        file_name = "DRI" + "_" + today_date + ".log"
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        self._handler = logging.FileHandler(file_name)
        self._logger.addHandler(self._handler)
        self._formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        self._handler.setFormatter(self._formatter)


    def parse_cmd_args(self):
        parser = argparse.ArgumentParser("help = Here we will be providing the NT ID of tester with which we want to filter "
                                "Owned by column")
        parser.add_argument('--nt_id', type = str, required= True, help = "Please provide NT ID of owner of assets")
        parsed_args = parser.parse_args()
        self._owned_by = parsed_args.nt_id

    def DRI_login(self):
        # We are selecting SSO method to login here
        self._logger.info("We are at Login Page and selecting SSO logging method")
        drop_down = self._login_page.authentication_method_dropdown_method()
        drop_down.click()

        select_SSO = self._login_page.select_SSO_method()
        drop_down.send_keys(Keys.ENTER)

        submit_button = self._login_page.submit_button_method()
        submit_button.click()

    def catalog_page_filter_column(self):
        """ Here we enable the Column Filter slide bar if not enabled already """
        self._logger.info("We are at Catalog Page now")

        column_filters = self._dri_catalog.column_filter_method()

        if column_filters.get_attribute("aria-checked") == "false":
            self.driver.execute_script("arguments[0].click();", column_filters)

        self._logger.info("Group Filter slider bar should be ON now")

        # Filtering Owned by Column
        self._logger.info(f"Filtering the owned by Column by name:- {self._owned_by}")
        owned_by = self._dri_catalog.owned_by_filter_method()
        self.driver.execute_script("arguments[0].scrollIntoView();", owned_by)
        time.sleep(2)
        owned_by.send_keys(self._owned_by)
        time.sleep(2)
        owned_by.send_keys(Keys.ENTER)

        datetime_today = datetime.datetime.today()
        today_month = datetime_today.month
        today_day = datetime_today.day
        today_year = datetime_today.year

        self._logger.info(f"Filtering the available assets by today's date which is {datetime.datetime.now()}")

        date_selection = self._dri_catalog.date_selection_method()
        date_selection.send_keys(today_month)
        time.sleep(2)

        date_selection.send_keys(today_day)
        time.sleep(2)

        date_selection.send_keys(today_year)
        time.sleep(5)

    def get_bundle_list(self):
        bundle_name_list = self._dri_catalog.bundle_name_list_method()
        print(len(bundle_name_list))

        length = len(bundle_name_list) / 3
        self._logger.info(f"We have {length} number of bundle available to be reserved which are owned by {self._owned_by}")
        bundle_name_list = bundle_name_list[:int(length)]
        bundle_list_text = []
        for bundle in bundle_name_list:

            bundle_text = bundle.get_attribute('text')
            bundle_list_text.append(bundle_text)

        for bundle in bundle_list_text:
            self._logger.info(f"We are going to reserve bundle {bundle}")
            bundle_name = self._dri_catalog.bundle_name_filter_method()
            bundle_name.send_keys(bundle)
            bundle_name.send_keys(Keys.ENTER)
            self.enhance_validity()
            time.sleep(5)
            self.catalog_page_filter_column()
        self.driver.close()

    def enhance_validity(self):
        action_rows = self._dri_catalog.action_rows_method()

        for rows in action_rows:
            date_buttons = rows.find_elements(By.XPATH, 'div/div/button[@action-type = "onReserve"]')
            for date_button in date_buttons:
                date_button.click()
                time.sleep(3)

                try:
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    unreserved_window = self._dri_catalog.unreserved_window_method()

                    unreserved_window_title = self._dri_catalog.unreserved_window_title_method()

                    unreserved_window_title = unreserved_window_title.text
                    if "Unreservable Assets" in unreserved_window_title:
                        self._logger.error(f"Asset can not be reserved. It might be empty")
                    time.sleep(2)
                    back_catalog_button = self._dri_catalog.back_to_catalog_button_method()
                    self.wait.until(expected_conditions.element_to_be_clickable(back_catalog_button[8]))
                    back_catalog_button[8].click()


                except NoSuchElementException as ex:
                    self._logger.info("Bundle is not empty")
                    datetime_today = datetime.datetime.today()
                    datetime_after_15_days = datetime.datetime.today() + datetime.timedelta(days = 14)
                    today_date_formatted = datetime_today.strftime("%m/%d/%y %H:%M")

                    start_date = self._dri_catalog.start_date_reservation_method()
                    start_date.clear()
                    start_date.send_keys(today_date_formatted)

                    after_15_days_date_formatted = datetime_after_15_days.strftime("%m/%d/%y %H:%M")

                    end_date = self._dri_catalog.end_date_reservation_method()
                    end_date.clear()
                    end_date.send_keys(after_15_days_date_formatted)
                    time.sleep(10)
                    reserve_button = self._dri_catalog.reserve_button_method()
                    self.wait.until(expected_conditions.element_to_be_clickable(reserve_button))
                    reserve_button.click()


if __name__ == '__main__':
    dri_main = DRIMain()
    dri_main.parse_cmd_args()
    dri_main.DRI_login()
    dri_main.catalog_page_filter_column()
    dri_main.get_bundle_list()

