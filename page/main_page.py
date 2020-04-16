from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from appium_temp.page.base_page import BasePage
from appium_temp.page.yuedu_search_page import YueduSearchPage


class YueduMainPage(BasePage):
    _menu_search = (By.ID, "menu_search")
    def to_sreach(self):
        el1 = self.find_element(self._menu_search)
        el1.click()
        return YueduSearchPage(self.driver)