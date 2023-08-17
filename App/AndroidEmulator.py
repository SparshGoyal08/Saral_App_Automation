import subprocess
import utils.logger as cl


class AndroidEmulator:
    log = cl.customLogger()

    def __init__(self):
        self.subprocess = subprocess.Popen

    emulator_bat = "C:/Users/DELL/Saral_App_Automation/Resources/init_emulator.bat"
    install_apk = "C:/Users/DELL/Saral_App_Automation/Resources/install_Saral_apk.bat"
    emulator_kill = "C:/Users/DELL/Saral_App_Automation/Resources/kill_emulator.bat"

    def init_android_emulator(self):
        self.subprocess(self.emulator_bat)
        self.log.info("Android emulator initiated")

    def install_Saral_apk(self):
        self.subprocess(self.install_apk)
        self.log.info("Installing Saral App")

    def uninstall_app_and_kill_emulator(self):
        self.subprocess(self.emulator_kill)
        self.log.info("Uninstall the Saral app and killed the Android emulator")