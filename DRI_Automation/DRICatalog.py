from selenium.webdriver.common.by import By


class DRICatalog:
    def __init__(self, driver):
        self.driver = driver

    column_filter = (By.XPATH, '//div[@class = "mat-slide-toggle-bar"]/input')

    bundle_name_filter = (By.XPATH, '//input[@aria-label = "Name Filter Input"]')

    owned_by_filter = (By.XPATH, '//input[@aria-label = "Owned By Filter Input"]')

    date_selection = (By.XPATH, '//input[@type = "date"]')

    actions_rows = (By.XPATH, '//div[@name = "right"]/div')

    unreserved_window = (By.XPATH, '//div[@class = "cdk-overlay-pane"]')

    unreserved_window_title = (By.XPATH, '//h1[@class = "mat-dialog-title"]')

    #back_to_catalog_button = (By.XPATH, '//button[contains(@class, "mat-button")]/span[contains(text(), "Back to Catalog")]')
    #back_to_catalog_button = (By.XPATH, '//button[contains(@class, "mat-button")]/span[1]')
    #back_to_catalog_button = (By.XPATH, '//button[contains(@class, "mat-button")]')

    #back_to_catalog_button = (By.XPATH, '//span[contains(text(), "Back to Catalog")]/parent::button[contains(@class, "mat-button")]/parent::div')

    back_to_catalog_button = (By.XPATH, '//button')
    start_date_reservation = (By.XPATH, '//input[@name = "qa-startdate-input"]')

    end_date_reservation = (By.XPATH, '//input[@name = "qa-enddate-input"]')

    reserve_button = (By.XPATH, '//span[contains(text(), "Reserve")]/parent::button')

    bundle_name_list = (By.XPATH, '//a[@class = "pointer"]')


    def column_filter_method(self):
        return self.driver.find_element(*DRICatalog.column_filter)

    def owned_by_filter_method(self):
        return self.driver.find_element(*DRICatalog.owned_by_filter)

    def date_selection_method(self):
        return self.driver.find_element(*DRICatalog.date_selection)

    def action_rows_method(self):
        return self.driver.find_elements(*DRICatalog.actions_rows)

    def unreserved_window_method(self):
        return self.driver.find_element(*DRICatalog.unreserved_window)

    def unreserved_window_title_method(self):
        return self.driver.find_element(*DRICatalog.unreserved_window_title)

    def back_to_catalog_button_method(self):
        return self.driver.find_elements(*DRICatalog.back_to_catalog_button)

    def bundle_name_filter_method(self):
        return self.driver.find_element(*DRICatalog.bundle_name_filter)

    def start_date_reservation_method(self):
        return self.driver.find_element(*DRICatalog.start_date_reservation)

    def end_date_reservation_method(self):
        return self.driver.find_element(*DRICatalog.end_date_reservation)

    def reserve_button_method(self):
        return self.driver.find_element(*DRICatalog.reserve_button)

    def bundle_name_list_method(self):
        return self.driver.find_elements(*DRICatalog.bundle_name_list)

