from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestEtuDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "etu"
        caps["appPackage"] = "com.etu.santu.professor.beta"
        caps["appActivity"] = "com.letu.modules.view.common.launch.activity.LaunchPageActivity"
        caps["noReset"] = True
        caps['unicodeKeyboard'] = True
        caps['showChromedriverLog'] = True
        # caps['chromedriverExecutable'] = "./chromedriver/2.20/chromedriver"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_demo_with_webview(self):
        self.driver.find_element_by_id("teacherAppIvIcon").click()
        # self.driver.find_element_by_accessibility_id("show_search").click()
        # self.driver.find_element_by_id("search_et_text").send_keys(":etudeveloper")
        for i in range(5):
            sleep(1)
            print(self.driver.contexts)

        self.driver.switch_to.context(self.driver.contexts[1])
        print(self.driver.current_context)

        # WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[src=/h/component_assets/right.svg]")))
        self.driver.find_element_by_xpath("//*[@class='weekNavigator']/div[1]/a[1]/img").click()
        # com.etu.santu.professor.beta
        # /h/component_assets/right.svg

    def teardown(self):
        sleep(20)
        self.driver.quit()