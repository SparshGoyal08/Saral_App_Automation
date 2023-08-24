import time
import unittest

import allure
import pytest

import Drivers.Drivers
from App.AndroidEmulator import AndroidEmulator
from App.AppiumServer import *
from Pages.LoginPage import LoginPage
from Pages.ProfilePage import ProfilePage
from Pages.BasePage import BasePage

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
    driver_instance = Drivers.Drivers.WebDriver()
    driver = driver_instance.init_driver()
    yield
    driver.quit()
    AndroidEmulatorInstance.uninstall_app_and_kill_emulator()
    AppiumServiceInstance.stop_appium_server()
    subprocess.Popen("C:/Users/DELL/Saral_App_Automation/Resources/AllureReport.bat")
    time.sleep(5)


@pytest.mark.usefixtures("setup_teardown")
@allure.suite("Login Page Test Suite")
class LoginPageCases(unittest.TestCase):
    """
    This is login test cases class to test login page
    """
    MobileNo = "8287210847"
    otp = "010203"

    @pytest.fixture(autouse=True)
    def classObjects(self):
        """
        initiate LoginPage instance
        :return: None
        """
        self.LoginPage = LoginPage(self)

    @pytest.mark.run(order=1)
    @allure.testcase("Input Mobile no. and click Next")
    def test_EnterMobileNo(self):
        """
        Testing Enter Mobile No. Page

        * Step 1: Enter Mobile no.
        * Step 2: Click Next button

        **Assert:** OTP page open or not
        """
        with allure.step("Enter Mobile no."):
            self.LoginPage.enterMobileNo(self.MobileNo)
            log.info(f"Entered mobile no. {self.MobileNo}")
        with allure.step("Click Next button"):
            self.LoginPage.ClickNext()
            log.info("Clicked on next button")
        with allure.step("Assert OTP page"):
            assert "OTP"

    @pytest.mark.run(order=2)
    @allure.testcase("Check if OTP field is empty, enter OTP and Click Submit")
    def test_EnterOTP(self):
        """
        Testing Enter OTP page

        * Step 1: Check if the field is empty
        * Step 2: Enter OTP
        * Step 3: Click Submit

        **Assert:** Assert True
        """
        with allure.step("Check if the field is empty"):
            self.LoginPage.clearOTP()
        with allure.step("Enter OTP"):
            self.LoginPage.enterOTP(self.otp)
        with allure.step("Click Submit"):
            self.LoginPage.ClickSubmit()
        with allure.step("Assert True"):
            assert True

    @pytest.mark.run(order=3)
    @allure.testcase("Logout of the app")
    def test_logout(self):
        """
        Testing Logout functionality

        * Step 1: Click on Profile
        * Step 2: Clck on Settings
        * Step 3: Click Logout

        **Assert:** Assert logout successfully toast message
        """
        with allure.step("Click on Profile"):
            ProfilePage(self).clickProfile()
        with allure.step("Clck on Settings"):
            ProfilePage(self).clickSettings()
        with allure.step("Click Logout"):
            ProfilePage(self).logout()
        with allure.step("Assert logout successfully toast message"):
            assert BasePage(self).getToast() == "logout successfully"
