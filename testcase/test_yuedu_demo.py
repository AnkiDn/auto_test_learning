from time import sleep

from appium import webdriver

from appium_temp.page.yuedu_search_page import YueduSearchPage


class TestYueduDemo:
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

    def test_demo_po(self):
        searchPage = YueduSearchPage(self.driver)
        searchPage.search("剑来")
        assert "最新" in searchPage.getLasted()

    def teardown(self):
        sleep(20)
        self.driver.quit()
        
