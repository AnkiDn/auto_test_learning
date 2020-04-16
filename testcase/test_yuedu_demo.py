from appium_temp.page.app import App


class TestYueduDemo:
    def setup(self):
        self.main_page = App.start()

    def test_demo_po(self):
        searchPage = self.main_page.to_sreach()
        searchPage.search("剑来")
        assert "最新" in searchPage.getLasted()

    def teardown(self):
        App.quit()
        
