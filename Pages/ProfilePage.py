import traceback

from Pages.BasePage import BasePage


class ProfilePage(BasePage):
    """
    This class contains the methods for Profile Page. It extends BasePage class as the base page class contains all the
    necessary methods to de-redundant the code here

    The methods are:
        * clickProfile
        * clickSettings
        * clickChangeLanguage
        * changeLanguage
        * logout
    """

    def __init__(self, driver):
        # initiating the driver instance from the super (Parent) class
        super().__init__(driver)
        self.driver = driver

    ProfileButton = "//android.widget.FrameLayout[@content-desc='Profile']/android.widget.FrameLayout/android.widget.ImageView"
    SettingsDropDown = "(//android.widget.ImageView[@content-desc='Saral image description'])[4]"
    ChangeLanguage = "Change Language"
    LogoutButton = "(//android.widget.ImageView[@content-desc='Saral image description'])[9]"
    SaveButton = "com.saral.application:id/btn_save"
    BackButton = "com.saral.application:id/iv_back"
    Yes = "android:id/button1"
    Cancel = "android:id/button2"

    def clickProfile(self):
        """
        Click on the profile button
        :return: None
        """
        try:
            self.clickElement(self.ProfileButton, "xpath")
            self.log.info("Clicked on Profile Page")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def clickSettings(self):
        """
        Click on the settings button
        :return: None
        """
        try:
            self.clickElement(self.SettingsDropDown, "xpath")
            self.log.info("Clicked on Settings button")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def clickChangeLanguage(self):
        """
        Click on the change language button
        :return: None
        """
        try:
            self.clickElement(self.ChangeLanguage, "text")
            self.log.info("Clicked on Change Language")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def changeLanguage(self, language_id):
        """
        Todo Need to test this on a faster machine @SPBhadra08
        Change the language to specified id
        :param language_id: starting 2 to 10, based on test case
        :return: None
        """
        try:
            languages = []
            for i in range(2, 11):
                languages.append(f"(//android.widget.ImageView[@content-desc='Saral image description'])[{i}]")
            self.clickElement(languages[language_id], "xpath")
            self.clickElement(self.SaveButton, "id")
            self.log.info("Changed app language to " + language_id)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def logout(self):
        """
        Logout of the profile
        :return: None
        """
        try:
            # while self.getToast() != "Logout Successfully":
            if self.isDisplayed("Logout", "text"):
                self.clickElement("Logout", 'text')
                self.log.info("Clicked on Logout button")
                self.clickElement(self.Yes, "id")
                self.log.info("Clicked on Yes, to confirm logout")
            else:
                self.clickElement(self.LogoutButton, "xpath")
                self.clickElement(self.Yes, "id")

            # self.log.info("Logged out successfully", self.getToast())
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)
