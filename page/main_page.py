from selenium.webdriver.remote.webdriver import WebDriver

from appium_temp.page.yuedu_search_page import YueduSearchPage


class YueduMainPage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def to_sreach(self):
        el1 = self.driver.find_element_by_id("menu_search")
        el1.click()
        return YueduSearchPage(self.driver)