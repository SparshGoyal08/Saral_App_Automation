import traceback
from selenium.common.exceptions import *
from Pages.BasePage import BasePage


class HomePage(BasePage):
    """
    This class contains all the methods needed to interact with elements on Home page

    The methods are:
        * clickHome
        * clickSangathan
        * clickSocialMedia
    """

    def __int__(self, driver):
        super().__init__(driver)
        self.driver = driver

    HomePage = "com.saral.application:id/menu_home"
    SangathanCard = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[1]/android.widget.ImageView"
    SocialMediaCard = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/androidx.cardview.widget.CardView[2]/android.widget.ImageView"

    def clickHome(self):
        """
        Click on Home Page
        :return:
        """
        try:
            if self.clickElement(self.HomePage, "id"):
                self.log.info("Clicked on Home Page")
        except Exception as e:
            self.ExceptionHandler.handleException(self.driver, e)

    def clickSangathan(self):
        """
        Click on Sangathan
        :return: None
        """
        try:
            if self.clickElement(self.SangathanCard, "xpath"):
                self.log.info("Clicked on Sangathan")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def clickSocialMedia(self):
        """
        Click on Social Media Card
        :return: None
        """
        try:
            if self.clickElement(self.SocialMediaCard, "xpath"):
                self.log.info("Clicked on Social Media Card")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)