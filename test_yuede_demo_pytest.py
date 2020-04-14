import datetime
# from appium.webdriver.common.touch_action import TouchAction
from time import sleep

import pytest
import yaml
from appium import webdriver
from hamcrest import *
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class TestYudeDemo:
    search_yuede_data = yaml.safe_load(open("search_yuede.yaml", "r"))

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "yuedu"
        caps["appPackage"] = "io.legado.app.release"
        caps["appActivity"] = "io.legado.app.ui.welcome.WelcomeActivity"
        caps["noReset"] = True
        caps['unicodeKeyboard'] = True
        # caps['udid'] = "emulator-5554"

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

    @pytest.mark.parametrize("book_name, num", [
        ("剑来", 1),
        ("诡秘之主", 0)
    ])
    def test_data_param(self, book_name, num):
        el1 = self.driver.find_element_by_accessibility_id("搜索")
        el1.click()
        el2 = self.driver.find_element_by_id("io.legado.app.release:id/search_src_text")
        el2.send_keys(book_name)
        self.driver.find_element_by_id("search_src_text").click()
        self.driver.find_element_by_id("search_go_btn").click()
        counts = self.driver.find_element_by_id("bv_originCount")
        assert "originCount" in counts.get_attribute("resource-id")
        assert int(counts.text) >= num
        assert_that(counts.get_attribute("package"), equal_to("io.legado.app.release"))

    @pytest.mark.parametrize("book_name, num", search_yuede_data)
    def test_data_param_from_yaml(self, book_name, num):
        el1 = self.driver.find_element_by_accessibility_id("搜索")
        el1.click()
        el2 = self.driver.find_element_by_id("io.legado.app.release:id/search_src_text")
        el2.send_keys(book_name)
        self.driver.find_element_by_id("search_src_text").click()
        self.driver.find_element_by_id("search_go_btn").click()
        counts = self.driver.find_element_by_id("bv_originCount")
        assert "originCount" in counts.get_attribute("resource-id")
        assert int(counts.text) >= num
        assert_that(counts.get_attribute("package"), equal_to("io.legado.app.release"))

    def test_step_case_from_yaml(self):
        TestYueduCase("search_yuede_test_case.yaml").run(self.driver)

    def teardown(self):
        # pass
        self.driver.quit()

class TestYueduCase:
    def __init__(self, case_file):
        file = open(case_file, "r")
        self.steps = yaml.safe_load(file)

    def run(self, driver: WebDriver):
        for step in self.steps:
            print(step)
            element = None
            if isinstance(step, dict):
                if "id" in step.keys():
                    element = driver.find_element_by_id(step["id"])
                elif "xpath" in step.keys():
                    element = driver.find_element_by_xpath(step["xpath"])
                else:
                    print(step.keys())

                if "click" in step.keys():
                    element.click()
                elif "input" in step.keys():
                    element.send_keys(step["input"])

                if "get" in step.keys():
                    text = element.get_attribute(step["get"])
                    print(text)
