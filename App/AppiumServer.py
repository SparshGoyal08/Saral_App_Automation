from appium.webdriver.appium_service import AppiumService
import utils.logger as cl


class AppiumServiceClass:
    log = cl.customLogger()

    def __init__(self):
        self.appium_service = AppiumService()

    def init_appium_server(self):
        args = {
            "--allow-cors": True
        }
        if not self.appium_service.is_running:
            self.appium_service.start(args=args)
            self.log.info("Appium Service started successfully")
        elif self.appium_service.is_running:
            self.log.info("Appium Service is running")
        else:
            self.log.info("Failed to start Appium Service")

    def stop_appium_server(self):
        if self.appium_service.is_running:
            self.appium_service.stop()
            assert not self.appium_service.is_running
            self.log.info("Appium service terminated")
        else:
            self.log.info("Appium service is not running")
