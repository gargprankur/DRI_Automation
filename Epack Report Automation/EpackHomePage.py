from selenium.webdriver.common.by import By


class EpackHomePage:
    def __init__(self, driver):
        self._driver = driver

    table_content = (By.XPATH, '//div[@class = "k-grid-content"]')

    epack_status_dropdown = (By.XPATH, '//th[@data-title = "Status"]/a')

    select_pre_epack_assigned = (By.XPATH, '//ul[contains(@class, "k-reset")]/li/label/input[@value = "Pre-EPack Assigned"]')

    select_epack_assigned = (By.XPATH, '//ul[contains(@class, "k-reset")]/li/label/input[@value = "Assigned"]')

    filter_button = (By.XPATH, '//button[text() = "Filter"]')

    preepack_epack_table_rows = (By.XPATH, '//tbody/tr')

    def epack_status_dropdown_method(self):
        return self._driver.find_element(*EpackHomePage.epack_status_dropdown)

    def select_pre_epack_assigned_method(self):
        return self._driver.find_element(*EpackHomePage.select_pre_epack_assigned)

    def select_epack_assigned_method(self):
        return self._driver.find_element(*EpackHomePage.select_epack_assigned)

    def filter_button_method(self):
        return self._driver.find_element(*EpackHomePage.filter_button)

    def preepack_epack_table_rows_method(self):
        return self._driver.find_elements(*EpackHomePage.preepack_epack_table_rows)

    def table_content_method(self):
        return self._driver.find_elements(*EpackHomePage.table_content)