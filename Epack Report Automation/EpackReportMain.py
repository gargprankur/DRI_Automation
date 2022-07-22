import datetime
import logging
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from BaseClass import BaseClass
from EpackHomePage import EpackHomePage
from SendEmail import SendEmail
import pandas as pd
from pretty_html_table import build_table


class EpackReportMain(BaseClass):

    def __init__(self):
        self.driver.get("http://pmaxepackprd.corp.emc.com/")
        self._epack_home = EpackHomePage(self.driver)
        today_date = datetime.datetime.now()
        today_date = today_date.strftime("%y%m%d")
        file_name = "Epack_Report" + "_" + today_date + ".log"
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        self._handler = logging.FileHandler(file_name)
        self._logger.addHandler(self._handler)
        self._formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
        self._handler.setFormatter(self._formatter)

    def filter_epack_status(self):
        self.wait.until(expected_conditions.presence_of_element_located((EpackHomePage.table_content)))
        time.sleep(20)
        epack_status_dropdown = self._epack_home.epack_status_dropdown_method()
        epack_status_dropdown.click()

        try:
            pre_epack_assigned = self._epack_home.select_pre_epack_assigned_method()
            pre_epack_assigned.click()

        except NoSuchElementException as ex:
            self._logger.debug("pre epack assigned field is not found")

        try:
            epack_assigned = self._epack_home.select_epack_assigned_method()
            epack_assigned.click()

        except NoSuchElementException as ex:
            self._logger.debug("epack assigned field is not found")

        filter_button = self._epack_home.filter_button_method()
        filter_button.click()

    def get_preepack_epack_list(self):
        epack_number = []
        customer_name = []
        epack_code = []
        epack_current_status = []
        QE_target_delivery = []
        QE_qualified_date = []
        QE_tester = []
        epack_status = {}

        preepack_epack_rows = self._epack_home.preepack_epack_table_rows_method()

        for preepack_epack_row in preepack_epack_rows:

            td_list = preepack_epack_row.find_elements(By.XPATH, 'td')

            epack_number.append(td_list[0].text)
            customer_name.append(td_list[1].text)
            epack_code.append(td_list[2].text)
            epack_current_status.append(td_list[6].text)
            QE_qualified_date.append(td_list[15].text)
            QE_target_delivery.append(td_list[17].text)
            QE_tester.append(td_list[19].text)

            epack_status["Epack Number"] = epack_number
            epack_status["Customer Name"] = customer_name
            epack_status["Code"] = epack_code
            epack_status["Status"] = epack_current_status
            epack_status["QE Target Delivery Date"] = QE_qualified_date
            epack_status["Pre Epack Qualified Date"] = QE_target_delivery
            epack_status["Tester"] = QE_tester

        data = pd.DataFrame(epack_status)

        output = build_table(data, "blue_light", font_size="small", font_family='Open Sans, sans-serif')
        SendEmail(output)


if __name__ == '__main__':
    epack_report_main = EpackReportMain()
    epack_report_main.filter_epack_status()
    epack_report_main.get_preepack_epack_list()