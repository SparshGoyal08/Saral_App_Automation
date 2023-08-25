import traceback

from Pages.BasePage import BasePage


class SocialMediaPage(BasePage):
    """
    This class contains all the methods needed to interact with elements on Social Media page

    The methods are:
        * clickSocialMedia
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SocialMedia = "com.saral.application:id/menu_social"

    def clickSocialMedia(self):
        """
        Click on Social Media page
        :return: None
        """
        try:
            self.clickElement(self.SocialMedia, "id")
            self.log.info("Clicked on Social Media page")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)
