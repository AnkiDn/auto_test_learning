from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from appium_temp.page.main_page import YueduMainPage


class App:
    driver: WebDriver = None
    
    @classmethod
    def start(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "yuedu"
        caps["appPackage"] = "io.legado.app.release"
        caps["appActivity"] = "io.legado.app.ui.welcome.WelcomeActivity"
        caps["noReset"] = True
        caps['unicodeKeyboard'] = True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(5)
        return YueduMainPage(cls.driver)
    
    @classmethod
    def quit(cls):
        cls.driver.quit()