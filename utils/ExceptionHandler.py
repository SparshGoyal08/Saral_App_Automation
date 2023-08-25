"""
////////////////////////////////////////////--DEPRECATED--\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""
import traceback
import utils.logger as cl


# Todo Need to work on Custom Exception Handler
class ExceptionHandler:
    """
    This is a custom exception handler class

    Methods
        * handleException
    """

    def __init__(self, driver):
        self.driver = driver

    log = cl.customLogger()

    def handleException(self, exception):
        """
        This is a custom Exception handler
        :param exception: Exception name to be handled
        :return: None
        """
        try:
            from Pages.BasePage import BasePage  # Move the import here
            self.log.info("################################# Exception Identified #################################")
            traceback.print_exception(type(exception), exception, exception.__traceback__)
            BasePage(self.driver).takeScreenshot(str(exception))
        except Exception as e:
            self.log.error("An error occurred while handling exception: ", e)
