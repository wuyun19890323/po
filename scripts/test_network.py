import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.page_network import PageNetwork

class Test_mobile_network():
    def setup(self):
        self.driver = init_driver()
        self.network_page = PageNetwork(self.driver)

    def test_mobile_network_2g(self):
        self.network_page.click_more()
        self.network_page.click_move_net()
        self.network_page.click_first_net_class()
        self.network_page.click_net_class_2g()
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()


    def test_mobile_network_3g(self):
        self.network_page.click_more()
        self.network_page.click_move_net()
        self.network_page.click_first_net_class()
        self.network_page.click_net_class_3g()
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
