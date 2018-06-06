import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.page_display import PageDisplay

class Test_mobile_display():
    def setup(self):
        self.driver = init_driver()
        self.display_page = PageDisplay(self.driver)

    def test_mobile_display_input(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys("hello")
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        self.display_page.click_display()
        self.display_page.click_search()
        self.display_page.input_text("hello")
        self.display_page.click_back()


