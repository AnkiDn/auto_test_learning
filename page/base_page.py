from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list = [(By.ID, "tips"),
                   (By.ID, "text_view")]
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        print(locator)
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception(locator)
            return self.driver.find_element(*locator)

    def find_elements(self, locator):
        print(locator)
        try:
            return self.driver.find_elements(*locator)
        except:
            self.handle_exception(locator)
            return self.driver.find_elements(*locator)

    def handle_exception(self, locator):
        page_source = self.driver.page_source
        for (key, value) in self._black_list:
            if "text_view" == value:
                sleep(5)
                self.driver.back()
                return

            if value in page_source:
                self.driver.find_element(key, value).click()
                return

            else:
                "%s not found "% str(locator)
