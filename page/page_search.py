from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageSearch(BaseAction):

    search_button = By.ID, "com.android.settings:id/search"
    input = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def search_click(self):
        self.click(self.search_button)

    def input_content(self,text):
        self.send_text(self.input,text)

    def back_click(self):
        self.click(self.back_button)
