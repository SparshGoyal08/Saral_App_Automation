import traceback

from Pages.BasePage import BasePage


class GreetingsPage(BasePage):
    """
    This class contains all the methods needed to interact with elements on Greetings page

    The methods are:
        * clickGreetings
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Greetings = "com.saral.application:id/menu_greetings"

    def clickGreetings(self):
        """
        Click on Greetings page
        :return: None
        """
        try:
            self.clickElement(self.Greetings, "id")
            self.log.info("Clicked on Greetings page")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)
