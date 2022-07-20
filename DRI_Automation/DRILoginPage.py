from selenium.webdriver.common.by import By


class DRILoginPage:

    def __init__(self, driver):
        self.driver = driver

    authentication_method_dropdown = (By.XPATH, '//mat-select[contains(@class, "mat-select")]')

    select_SSO = (By.XPATH, '//span[text() = "SSO"]')

    submit_button = (By.XPATH, '//button[@type = "submit"]')

    def authentication_method_dropdown_method(self):
        return self.driver.find_element(*DRILoginPage.authentication_method_dropdown)

    def select_SSO_method(self):
        return self.driver.find_element(*DRILoginPage.select_SSO)

    def submit_button_method(self):
        return self.driver.find_element(*DRILoginPage.submit_button)