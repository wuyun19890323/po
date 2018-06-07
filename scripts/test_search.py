import sys,os
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.page_search import PageSearch


class TestSearch:
    def setup(self):
        self.driver = init_driver()
        self.search_page = PageSearch(self.driver)

    def test_search(self):
        # 点击放大镜、输入文字、返回
        self.search_page.search_click()
        self.search_page.input_content("hello")
        self.search_page.back_click()

    def test_001(self):
        print("123")
        assert 0

