from time import sleep

from appium import webdriver

class TestH5Demo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "h5"
        caps["browserName"] = "Chrome"
        caps["noReset"] = True
        caps["showChromedriverLog"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)


    def testDemo(self):
        self.driver.get("https://testerhome.com/")
        print(self.driver.current_context)
        print(self.driver.contexts)
        self.driver.find_element_by_css_selector("#mobile-search-form > input").send_keys("appium")

    def teardown(self):
        sleep(20)
        self.driver.quit()