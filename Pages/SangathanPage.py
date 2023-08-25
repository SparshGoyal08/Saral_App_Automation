import traceback

import utils.logger as cl
from Pages.BasePage import BasePage


class SangathanPage(BasePage):
    """
    This class contains all the methods needed to interact with elements on Sangathan page

    The methods are:
        * choosePradesh
        * chooseLevel
        * clickHelp
        * changePradesh
        * crossPradesh
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger()

    HelpButton = "com.saral.application:id/iv_help"
    TvLocation = "com.saral.application:id/tv_location_name"
    CrossPradesh = "com.saral.application:id/iv_close"

    def choosePradesh(self, pradesh):
        """
        Choose Pardesh name when entering Sangathan Page first time
        :return: None
        """
        try:
            if self.isDisplayed("Choose Pradesh", "text"):
                self.clickElement(pradesh, "text")
                self.log.info("Selected Pradesh as: " + pradesh)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseLevel(self, level):
        """
        Choose Data Entry Level
        :param level: level name
        :return: None
        """
        try:
            self.clickElement(level, "text")
            self.log.info("Selected Level: " + level)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def clickHelp(self):
        """
        Click on Help button
        :return: None
        """
        try:
            self.clickElement(self.HelpButton, "id")
            self.log.info("Clicked on Help button")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def changePradesh(self):
        """
        Change Pradesh name
        :return: None
        """
        try:
            self.clickElement(self.TvLocation, "id")
            self.log.info("Clicked on change pradesh")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def crossPradesh(self):
        """
        Close change pradesh dialogue box
        :return: None
        """
        try:
            self.clickElement(self.CrossPradesh, "id")
            self.log.info("Closed Choose Pradesh dialogue box")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)
