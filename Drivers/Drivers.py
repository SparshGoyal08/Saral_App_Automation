from appium import webdriver
from Configs import Configs


class WebDriver:
    """
    This class is responsible for initiating a new driver
    """

    def __init__(self):
        # initiating webdriver class
        self.driver = webdriver.Remote

    def init_driver(self):
        """
        This method initiates a webdriver at the below-mentioned local host and appends
        desired capabilities pulled from config file
        :return: driver
        """
        desired_caps = Configs.caps
        driver = self.driver("http://127.0.0.1:4723", desired_caps)
        return driver
