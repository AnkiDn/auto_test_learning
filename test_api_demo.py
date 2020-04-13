
from appium import webdriver

class TestYudeDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "apiDemo"
        caps["appPackage"] = "com.touchboarder.android.api.demos"
        caps["appActivity"] = "com.example.android.apis.ApiDemos"
        caps["automationName"] = "Uiautomator2"
        caps["noReset"] = True
        caps['unicodeKeyboard'] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)


    def test_demo(self):
        self.driver.find_element_by_xpath("//*[@text='Views']").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='MAKE A POPUP!']").click()
        assert "Edit" in self.driver.find_element_by_xpath("//*[@text='Edit']").text
        self.driver.find_element_by_xpath("//*[@text='Search']").click()
        assert "Clicked popup menu item Search" in self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

    def teardown(self):
        pass
        # self.driver.quit()