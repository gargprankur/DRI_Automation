from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class BaseClass:
    #services = Service("C:\\Users\\gargp6\\OneDrive - Dell Technologies\Documents\\chromedriver.exe")
    #driver = webdriver.Chrome(service=services)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(30)
    wait = WebDriverWait(driver, 90)
