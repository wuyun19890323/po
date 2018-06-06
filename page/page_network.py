from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class PageNetwork(BaseAction):
    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.driver = driver

    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    move_net_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    first_net_class_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    net_class_2g_button = By.XPATH, "//*[contains(@text,'2G')]"
    net_class_3g_button = By.XPATH, "//*[contains(@text,'3G')]"

    def click_more(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.click(self.more_button)

    def click_move_net(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.click(self.move_net_button)

    def click_first_net_class(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.click(self.first_net_class_button)

    def click_net_class_2g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
        self.click(self.net_class_2g_button)

    def click_net_class_3g(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
        self.click(self.net_class_3g_button)