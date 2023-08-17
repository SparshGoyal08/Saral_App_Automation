import utils.logger as cl
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

    MobileNo = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText"
    # MobileNo = "com.saral.application:id/et_mobile"
    NextButton = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button"
    # NextButton = "Next"

    def enterMobileNo(self, no):
        """
        to enter mobile no. on login page
        :param no: pass the mobile no. from test case
        :return: None
        """
        if self.isDisplayed(self.MobileNo, "xpath"):
            print("Input box accessible")
            self.sendKeys(no, self.MobileNo, "xpath")
            cl.allureLogs("Enter Mobile number")
        else:
            print("Input box not found")

    def ClickNext(self):
        """
        Click the next button after entering mobile no.
        :return: None
        """
        if self.isDisplayed(self.NextButton, "xpath"):
            self.clickElement(self.NextButton, "xpath")
            cl.allureLogs("Clicking the next button")
        else:
            print("cannot find the next button")
