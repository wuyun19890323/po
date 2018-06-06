from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageDisplay(BaseAction):

    # def __init__(self, driver):
    #     BaseAction.__init__(self, driver)

    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    input = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_display(self):
       # self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.click(self.search_button)

    def input_text(self, text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        self.send_text(self.input, text)

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        self.click(self.back_button)