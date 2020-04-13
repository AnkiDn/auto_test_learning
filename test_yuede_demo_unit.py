from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class TestYudeDemo:
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "yuedu"
        caps["appPackage"] = "io.legado.app.release"
        caps["appActivity"] = "io.legado.app.ui.welcome.WelcomeActivity"

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

    def tearDown(self):
        self.driver.quit()