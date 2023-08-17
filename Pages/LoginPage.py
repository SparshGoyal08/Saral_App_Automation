import utils.logger as cl
from Pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import By


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    MobileNo = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText"
    # MobileNo = "com.saral.application:id/et_mobile"
    NextButton = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button"

    # NextButton = "Next"
    def enterMobileNo(self, no):
        """Mobile_no = Driver().find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText")
        if Mobile_no.is_displayed():
            print("Input box visible")
            Mobile_no.send_keys("8287210847")
        else:
            print("input box not visible")"""
        if self.isDisplayed(self.MobileNo, "xpath"):
            """mobile_input = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.MobileNo))
            )"""
            print("Input box accessible")
            self.sendKeys(no, self.MobileNo, "xpath")
            cl.allureLogs("Enter Mobile number")
        else:
            print("Input box not found")

    def ClickNext(self):
        """next_button = Driver().find_element(AppiumBy.XPATH,
                                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button")
        next_button.click()"""

        if self.isDisplayed(self.NextButton, "xpath"):
            self.clickElement(self.NextButton, "xpath")
            cl.allureLogs("Clicking the next button")
        else:
            print("cannot find the next button")
