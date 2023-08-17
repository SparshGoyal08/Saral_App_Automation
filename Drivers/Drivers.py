import time
from appium import webdriver
from Configs import Configs


class WebDriver:
    def init_driver(self):
        desired_caps = Configs.caps
        driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)
        return driver