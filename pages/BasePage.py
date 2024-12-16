from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from exceptiions import PageException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            raise PageException

    def wait_for_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            raise PageException

    def click_element(self, locator):
        try:
            self.wait_for_element(locator).click()
        except Exception as e:
            raise PageException

    def send_keys_to_element(self, locator, text):
        try:
            self.wait_for_element(locator).send_keys(text)
        except Exception as e:
            raise PageException
