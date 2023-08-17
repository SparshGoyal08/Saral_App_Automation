import subprocess
import utils.logger as cl


class AndroidEmulator:
    """
    This class is responsible for Android emulator tasks

    The methods are
        * init_android_emulator
        * install_Saral_apk, and
        * uninstall_app_and_kill_emulator
    """
    log = cl.customLogger()

    def __init__(self):
        # initiating the subprocess.Popen class into self.subprocess variable
        self.subprocess = subprocess.Popen

    emulator_bat = "C:/Users/DELL/Saral_App_Automation/Resources/init_emulator.bat"
    install_apk = "C:/Users/DELL/Saral_App_Automation/Resources/install_Saral_apk.bat"
    emulator_kill = "C:/Users/DELL/Saral_App_Automation/Resources/kill_emulator.bat"

    def init_android_emulator(self):
        """
        This method initiates a new Android emulator using the batch (.bat) file
        mentioned above
        """
        self.subprocess(self.emulator_bat)
        self.log.info("Android emulator initiated")

    def install_Saral_apk(self):
        """
        This method installs the Saral app to the Android emulator using the batch (.bat)
        file
        """
        self.subprocess(self.install_apk)
        self.log.info("Installing Saral App")

    def uninstall_app_and_kill_emulator(self):
        """
        This method unistalls the Saral app and kills the AVD using the batch (.bat)
        file
        """
        self.subprocess(self.emulator_kill)
        self.log.info("Uninstall the Saral app and killed the Android emulator")
