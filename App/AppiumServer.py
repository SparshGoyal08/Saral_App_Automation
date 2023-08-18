import subprocess

from appium.webdriver.appium_service import AppiumService
import utils.logger as cl


class AppiumServiceClass:
    """
    This class is responsible for starting and stoping Appium Service

    The methods are
        * init_appium_server
        * stop_appium_server
    """
    log = cl.customLogger()

    def __init__(self):
        self.appium_service = AppiumService()

    def init_appium_server(self):
        """
        This method Starts a new Appium Service
        """
        args = {
            # --allow-cors to allow appium to listen to API activities even if the AVD
            # is running on a different source
            "--allow-cors": True
        }
        # check if the service is running
        if not self.appium_service.is_running:
            self.appium_service.start(args=args)
            self.log.info("Appium Service started successfully")
        elif self.appium_service.is_running:
            self.log.info("Appium Service is running")
        else:
            self.log.info("Failed to start Appium Service")

    def stop_appium_server(self):
        """
        This method stops the running Appium Service
        """
        # check if the service is running
        if self.appium_service.is_running:
            self.appium_service.stop()
            assert not self.appium_service.is_running
            self.log.info("Appium service terminated")
        else:
            self.log.info("Appium service is not running")
