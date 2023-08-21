import time
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from Drivers.Drivers import WebDriver
import utils.logger as cl
from urllib3.exceptions import MaxRetryError


class BasePage:
    """
    This is the base class for Pages directory which allows DRY code.

    The methods are:
        * waitForElement
        * getElement
        * clickElement
        * sendKeys
        * isDisplayed
        * isDisplayed
    """
    log = cl.customLogger()

    def __init__(self, driver):
        # initiating driver instance
        self.driver = driver
        self.web = WebDriver().init_driver()

    def waitForElement(self, locatorvalue, locatorType):
        """
        This method is used to de-redundant WebDriverWait.until function
        :param locatorvalue: To pass locator value
        :param locatorType: To pass locator type
        :return: element
        """
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.web, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException, MaxRetryError, KeyboardInterrupt])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % locatorvalue))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % locatorvalue))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        """
        This method is used to fetch element
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: None
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorValue[
                                                                                                          :10] + "....")
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue[
                                                                                                        :10] + "....")
            self.takeScreenshot(locatorType)
            assert False

        return element

    def clickElement(self, locatorValue, locatorType="id"):
        """
        This method is used to click element, it extends the getElement method
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: None
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue[
                                                                                                         :10] + "....")
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue[
                                                                                                                 :10] + "....")
            self.takeScreenshot(locatorType)
            assert False

    def sendKeys(self, text, locatorValue, locatorType):
        """
        This method is used to send keys to input type fields, it extends getElement method
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: None
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue[
                                                                                                            :10] + "....")
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue[
                                                                                                                     :10] + "....")
            self.takeScreenshot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType):
        """
        This method is used to check if the element is visible or not, it extends
        getElement method
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: None
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue[
                                                                                               :10] + "...." + "is displayed ")
            return True
        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue[
                                                                                               :10] + "...." + " is not displayed")
            self.takeScreenshot(locatorType)
            return False

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../Saral_App_Automation/LocalLogs/screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.web.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        allure.attach(self.web.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCode(self, value):
        self.driver.press_keycode(value)
