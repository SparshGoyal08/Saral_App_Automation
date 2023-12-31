import time
import traceback

import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from uiautomator import Device
from urllib3.exceptions import MaxRetryError

import utils.logger as cl
# from utils.ExceptionHandler import ExceptionHandler
from Drivers.Drivers import WebDriver


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
    # ExceptionHandler = ExceptionHandler

    def __init__(self, driver):
        # initiating driver instance
        self.driver = driver
        self.web = WebDriver().init_driver()

    def waitForElement(self, locatorvalue: str, locatorType: str):
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
        elif locatorType == "accessibility id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ACCESSIBILITY_ID, locatorvalue))
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
        elif locatorType == "keycode":
            element = wait.until(lambda x: x.press_keycode(locatorvalue))
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorValue: str, locatorType: str):
        """
        This method is used to fetch element
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: element
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorValue)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)

        return element

    def getText(self, locatorValue: str, locatorType: str):
        """
        Todo @SPBhadra08 use this for getToast method, remove this Todo line after
        Get text method to get the text value associated with an element
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: Text from the element
        """
        element = None
        text = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            text = element.text
            self.log.info(
                "Element with LocatorType: " + locatorType + " and locatorValue :" + locatorValue + " has text :" + text)
            return text
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info(
                "Element with LocatorType: " + locatorType + " and locatorValue :" + locatorValue + " does not have text")
            self.takeScreenshot(locatorType)

    def getToast(self):
        """
        Todo : Need to optimize this @SPBhadra08
        getToast method is used to fetch the toast message on screen
        :return: toast message
        """
        toast = Device().toast.get_message()
        return toast

    def clickElement(self, locatorValue: str, locatorType="id"):
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
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)

    def sendKeys(self, text, locatorValue: str, locatorType: str):
        """
        This method is used to send keys to input type fields, it extends getElement method
        :param text: text value to be passed
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
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)

    def isEmpty(self, locatorValue: str, locatorType: str):
        """
        Check if the input field is empty or not
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: None
        """
        element = None
        try:
            pass
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            attr = element.get_attributes()
            self.log.info(f"Found following attributes that needs to be cleared\n {attr}")
            return attr
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info("No attributes found to be cleared off")
            self.takeScreenshot(locatorType)

    def clear(self, locatorValue: str, locatorType: str):
        """
        Clear the input field in order to fill new values
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: True: if clear() else: False
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.clear()
            self.log.info(
                "Element with locatorType: " + locatorType + " and locatorValue: " + locatorValue + " is cleared")
            return True
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info(
                "Element with locatorType: " + locatorType + " and locatorValue: " + locatorValue + " is not cleared")
            self.takeScreenshot(locatorType)
            return False

    def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int):
        """
        Swipe method is used to swipe on the page based on x and y co-ordinates
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :param start_x: Start point for horizontal scroll
        :param start_y: Start point for vertical scroll
        :param end_x: End point for horizontal scroll
        :param end_y: End point for vertical scroll
        :parameter:
            1. Vertical Scroll: start_x == end_x
            2. Horizontal Scroll: start_y == end_y
            3. Downward Scroll: start_y < end_y
            4. Upward Scroll: start_y > end_y
            5. Right-Left Scroll: start_x > end_x
            6. Left-Right Scroll: start_x < end_x
        :return:
        """
        element = None
        try:
            self.web.swipe(start_x, start_y, end_x, end_y, duration=100)
            self.log.info("Swipe function on Carousel is taking place")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info("Swipe function on Carousel is taking place")
            self.takeScreenshot("Carousel")

    def scrollIntoView(self, locatorValue, locatorType):
        """
        Scroll into view allows scrolling until a specific element is visible
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: None
        """
        element = None
        try:
            if locatorType == "text":
                self.web.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(\"" + locatorValue + "\").instance(0))")
            if locatorType == "xpath":
                self.web.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                      "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().xpath(\"" + locatorValue + "\").instance(0))")
            if locatorType == "id":
                self.web.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                      "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().id(\"" + locatorValue + "\").instance(0))")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def isDisplayed(self, locatorValue: str, locatorType: str):
        """
        This method is used to check if the element is visible or not, it extends
        getElement method
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: True: if isDisplayed() else: False
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is displayed ")
            return True
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            self.takeScreenshot(locatorType)
            return False

    def isEnabled(self, locatorValue: str, locatorType: str):
        """
        Method to check if an element is enabled or not
        :param locatorValue: To pass locator value
        :param locatorType: To pass locator type
        :return: True: if isEnabled else: False
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_enabled()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is enabled")
            return True
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not enabled")
            self.takeScreenshot(locatorType)
            return False

    def pushFile(self, destinationPath, sourcePath):
        """
        Push File to AVD
        :param destinationPath: Destination path
        :param sourcePath: Source Path
        :return: None
        """
        try:
            self.web.push_file(destinationPath, sourcePath)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def screenShot(self, screenshotName):
        """
        Take Screenshot of the current page of Android device
        :param screenshotName: name of the screenshot
        :return: None
        """
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../Saral_App_Automation/LocalLogs/screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.web.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        """
        Attach screenshot to allure report
        :param text: name of the screenshot as the locatortype
        :return:
        """
        allure.attach(self.web.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCode(self, value):
        """
        Keycode press method to interact with Android core buttons
        :param value:
        :return:
        """
        self.driver.press_keycode(value)
