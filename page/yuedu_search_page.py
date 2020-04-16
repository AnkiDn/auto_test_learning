from selenium.webdriver.common.by import By

from appium_temp.page.base_page import BasePage


class YueduSearchPage(BasePage):
    _search_src_text = (By.ID, "io.legado.app.release:id/search_src_text")
    _search_go_btn = (By.ID, "search_go_btn")
    _tv_lasted = (By.ID, "tv_lasted")

    def search(self, keyword):
        el2 = self.find_element(self._search_src_text)
        el2.send_keys(keyword)
        el2.click()
        self.find_element(self._search_go_btn).click()
        return self

    def getLasted(self):
        lasteds = self.find_elements(self._tv_lasted)
        if len(lasteds) >= 1:
            return lasteds[0].text
        else:
            return ""