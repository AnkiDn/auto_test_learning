import datetime

from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
from time import sleep

from hamcrest import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By



class TestYudeDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "yuedu"
        caps["appPackage"] = "io.legado.app.release"
        caps["appActivity"] = "io.legado.app.ui.welcome.WelcomeActivity"
        caps["noReset"] = True
        caps['unicodeKeyboard'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_demo(self):
        sleep(10)
        self.driver.back()
        # TouchAction(driver).move_to(x=10,y=10).perform()
        # TouchAction(driver).press(x=10,y=10).release().perform()
        # driver.tap([(298,148)])
        # driver.back()
        el1 = self.driver.find_element_by_accessibility_id("搜索")
        el1.click()
        el2 = self.driver.find_element_by_id("io.legado.app.release:id/search_src_text")
        el2.send_keys("剑来")

    def test_capabilities(self):
        el1 = self.driver.find_element_by_accessibility_id("搜索")
        el1.click()
        el2 = self.driver.find_element_by_id("io.legado.app.release:id/search_src_text")
        el2.send_keys("剑来")

    def test_performance(self):
        print(self.driver.get_performance_data_types())
        for p in self.driver.get_performance_data_types():
            try:
                print(self.driver.get_performance_data("io.legado.app.release", p, 5))
            except:
                pass

    def test_wait(self):
        # io.legado.app.release:id/text_view

        # WebDriverWait(self.driver, 15).until(lambda x: len(self.driver.find_elements_by_id("text_view")) >= 1)
        # sleep(5)
        # self.driver.back()

        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "text_view"))
        # )
        # sleep(5)
        # self.driver.back()


        def loaded(driver):
            print(datetime.datetime.now())
            if len(self.driver.find_elements_by_id("text_view")) >= 1:
                sleep(5)
                self.driver.back()
                return True
            else:
                return False
        try:
            WebDriverWait(self.driver, 15).until(loaded)
        except:
            print("no data")

        el1 = self.driver.find_element_by_accessibility_id("搜索")
        el1.click()
        el2 = self.driver.find_element_by_id("io.legado.app.release:id/search_src_text")
        el2.send_keys("剑来")

    def test_xpath(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'menu_my_config') and @content-desc='我的']").click()

    def test_assert(self):
        el1 = self.driver.find_element_by_accessibility_id("搜索")
        el1.click()
        el2 = self.driver.find_element_by_id("io.legado.app.release:id/search_src_text")
        el2.send_keys("剑来")
        self.driver.find_element_by_id("search_src_text").click()
        self.driver.find_element_by_id("search_go_btn").click()
        lasteds = self.driver.find_elements_by_id("tv_lasted")
        if len(lasteds) >= 1:
            assert "tv_lasted" in lasteds[0].get_attribute("resource-id")
            assert "最新" in lasteds[0].text
            assert_that(lasteds[0].get_attribute("package"), equal_to("io.legado.app.release"))

    def teardown(self):
        pass
        # self.driver.quit()