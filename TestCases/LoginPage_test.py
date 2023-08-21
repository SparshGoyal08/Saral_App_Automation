import unittest

import allure
import pytest

import Drivers.Drivers
import utils.logger as cl
from App.AndroidEmulator import AndroidEmulator
from App.AppiumServer import *
from Pages.LoginPage import LoginPage

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
    AppiumServiceInstance = AppiumServiceClass()
    AppiumServiceInstance.init_appium_server()
    driver_instance = Drivers.Drivers.WebDriver()
    web_driver = driver_instance.init_driver()
    yield
    web_driver.quit()
    AndroidEmulatorInstance.uninstall_app_and_kill_emulator()
    AppiumServiceInstance.stop_appium_server()
    subprocess.Popen("C:/Users/DELL/Saral_App_Automation/Resources/AllureReport.bat")


@pytest.mark.usefixtures("setup_teardown")
@allure.suite("Login Page Test Suite")
class LoginPageCases(unittest.TestCase):
    """
    This is login test cases class to test login page
    """
    MobileNo = "8287210847"
    @pytest.fixture(autouse=True)
    def classObjects(self):
        """
        initiate LoginPage instance
        :return: None
        """
        self.LoginPage = LoginPage(self)

    @pytest.mark.run(order=1)
    @allure.testcase("Test Login Functionality")
    def test_login_functionality(self):
        """
        Testing login functionality

        * Step 1: Enter Mobile no.
        * Step 2: Click Next button

        **Assert:** OTP page open or not
        """
        with allure.step("Enter Mobile no."):
            self.LoginPage.enterMobileNo(self.MobileNo)
            log.info(f"Entered mobile no. {self.MobileNo}")
        with allure.step("Click Next button"):
            self.LoginPage.ClickNext()
            log.info("Clicked in next button")
        with allure.step("Assert OTP page"):
            assert "OTP"
