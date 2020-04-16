class YueduSearchPage(object):
    def __init__(self, driver):
        self.driver = driver

    def search(self, keyword):
        el1 = self.driver.find_element_by_accessibility_id("搜索")
        el1.click()
        el2 = self.driver.find_element_by_id("io.legado.app.release:id/search_src_text")
        el2.send_keys(keyword)
        self.driver.find_element_by_id("search_src_text").click()
        self.driver.find_element_by_id("search_go_btn").click()
        return self

    def getLasted(self):
        lasteds = self.driver.find_elements_by_id("tv_lasted")
        if len(lasteds) >= 1:
            return lasteds[0].text
        else:
            return ""