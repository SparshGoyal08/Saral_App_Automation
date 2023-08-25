from selenium.common.exceptions import *
import traceback
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """
    This class contains the methods for login page. It extends BasePage class as the base page class contains all the
    necessary methods to de-redundant the code here

    The methods are:
        * enterMobileNo
        * ClickNext
    """

    def __init__(self, driver):
        # initiating the driver instance from the super (Parent) class
        super().__init__(driver)
        self.driver = driver

    MobileNo = "com.saral.application:id/et_mobile"
    NextButton = "Next"
    otp = "com.saral.application:id/otp_view"
    submit = "Submit"
    AndridUpdate = "android:id/button1"
    CloseApp = "android:id/aerr_close"

    def enterMobileNo(self, no):
        """
        to enter mobile no. on login page
        :param no: pass the mobile no. from test case
        :return: None
        """
        try:
            self.sendKeys(no, self.MobileNo, "id")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def ClickNext(self):
        """
        Click the next button after entering mobile no.
        :return: None
        """
        try:
            print("Found Next button")
            self.clickElement(self.NextButton, "text")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def clearOTP(self):
        """
        clear OTP field
        :return: None
        """
        try:
            self.clear(self.otp, "id")
            self.log.info("Cleared OTP field")
        except NoSuchElementException:
            if self.isDisplayed("android:id/message", "id"):
                self.log.info("Identified an error related to app, trying to resolve, please wait!")
                self.clickElement("0", "index")
                self.clickElement(187, "keycode")
                self.clickElement(187, "keycode")
                self.clear(self.otp, "id")
                self.log.info("Cleared OTP field")
            else:
                print("NoSuchElementException Encountered")

    def enterOTP(self, otp):
        """
        Enter OTP in the OTP inout field
        :return: None
        """
        try:
            self.sendKeys(otp, self.otp, "id")
            self.log.info(f"Entered OTP {otp}")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def ClickSubmit(self):
        """
        Click Submit button After entering OTP
        :return: None
        """
        try:
            self.clickElement(self.submit, "text")
            self.log.info("Clicked on Submit button")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)
