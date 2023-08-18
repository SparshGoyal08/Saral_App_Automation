import subprocess
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from Drivers.Drivers import *
from App.AppiumServer import *
from App.AndroidEmulator import AndroidEmulator
from Pages.LoginPage import LoginPage
import utils.logger as cl
import allure

# initiating logger instance
log = cl.customLogger()


@pytest.fixture(scope="class")
def setup_teardown(request):
    """
    TearDown method to prepare environment before starting test cases
    :return: None
    """
    log.info("********************************* Start Test *********************************")
    AndroidEmulatorInstance = AndroidEmulator()
    AndroidEmulatorInstance.init_android_emulator()
    time.sleep(40)
    AppiumServiceInstance = AppiumServiceClass()
    AppiumServiceInstance.init_appium_server()
    driver_instance = WebDriver()
    driver = driver_instance.init_driver()
    time.sleep(10)
    yield
    driver.quit()
    AndroidEmulatorInstance.uninstall_app_and_kill_emulator()
    AppiumServiceInstance.stop_appium_server()
    subprocess.Popen("C:/Users/DELL/Saral_App_Automation/Resources/AllureReport.bat")


@pytest.mark.usefixtures("setup_teardown")
@allure.severity(allure.severity_level.BLOCKER)
class LoginTest(unittest.TestCase):
    """
    This is login test cases class to test login page
    """
    @pytest.fixture(autouse=True)
    def classObjects(self):
        """
        initiate LoginPage instance
        :return: None
        """
        self.LoginPage = LoginPage(self)

    @pytest.mark.run(order=2)
    def test_login_functionality(self):
        """
        Testing login functionality

        * Step 1: Enter Mobile no.
        * Step 2: Click Next button

        **Assert:** OTP page open or not
        """
        cl.allureLogs("Login functionality")
        self.LoginPage.enterMobileNo("8287210847")
        self.LoginPage.ClickNext()
        assert "OTP"
