import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from Drivers.Drivers import WebDriver
from App.AppiumServer import *
from App.AndroidEmulator import AndroidEmulator
from Pages.LoginPage import LoginPage
import utils.logger as cl

log = cl.customLogger()
@pytest.fixture(scope="class")
def setup_teardown(request):
    log.info("********************************* Start Test *********************************")
    AndroidEmulatorInstance = AndroidEmulator()
    AndroidEmulatorInstance.init_android_emulator()
    time.sleep(40)
    AndroidEmulatorInstance.install_Saral_apk()
    AppiumServiceInstance = AppiumServiceClass()
    AppiumServiceInstance.init_appium_server()
    driver_instance = WebDriver()
    driver = driver_instance.init_driver()
    time.sleep(10)
    yield
    driver.quit()
    AndroidEmulatorInstance.uninstall_app_and_kill_emulator()
    AppiumServiceInstance.stop_appium_server()


@pytest.mark.usefixtures("setup_teardown")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.LoginPage = LoginPage(self)

    @pytest.mark.run(order=2)
    def test_login_functionality(self):
        cl.allureLogs("Login functionality")
        self.LoginPage.enterMobileNo("8287210847")
        self.LoginPage.ClickNext()
        assert "OTP"