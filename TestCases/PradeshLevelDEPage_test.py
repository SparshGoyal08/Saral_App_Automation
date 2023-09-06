import time
import unittest

import allure
import pytest

import Drivers.Drivers as Driver
from App.AndroidEmulator import AndroidEmulator
from App.AppiumServer import *
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.PradeshLevelDEPage import PradeshLevelDEPage
from Pages.SangathanPage import SangathanPage

log = cl.customLogger()


@pytest.fixture(scope="class")
def setup_teardown(request):
    """
    TearDown method to prepare environment before starting test cases
    :return: None
    """
    log.info("********************************* Start Test *********************************")
    AndroidEmulatorInstance = AndroidEmulator()
    AndroidEmulatorInstance.init_android_emulator()
    time.sleep(40)
    AppiumServiceInstance = AppiumServiceClass()
    AppiumServiceInstance.init_appium_server()
    driver_instance = Driver.WebDriver()
    driver = driver_instance.init_driver()
    yield
    AndroidEmulatorInstance.uninstall_app_and_kill_emulator()
    AppiumServiceInstance.stop_appium_server()
    subprocess.Popen("C:/Users/DELL/Saral_App_Automation/Resources/AllureReport.bat")
    time.sleep(5)
    log.info("********************************* End Test *********************************")


@pytest.mark.usefixtures("setup_teardown")
@allure.suite("Pradesh Level Data Entry Page Test Suite")
class PradeshLevelDEPageCases(unittest.TestCase):
    """
    This is Pradesh Level Data Entry Page test cases class to test Pradesh Level Data Entry Page
    """
    MobileNo = "8287210847"
    otp = "010203"
    Pradesh = "Assam"
    Level = "Pradesh"

    @pytest.fixture(autouse=True)
    def classObjects(self):
        """
        initiate LoginPage instance
        :return: None
        """
        self.LoginPage = LoginPage(self)

    @pytest.mark.run(order=1)
    @allure.testcase("Login")
    def test_Login(self):
        """
        Testing Login functionality

        * Step 1: Enter Mobile no. Page
        * Step 2: Enter OTP and click Next

        """
        with allure.step("Mobile No. Page"):
            self.LoginPage.enterMobileNo(self.MobileNo)
            self.LoginPage.ClickNext()
        with allure.step("Enter OTP and click Next"):
            self.LoginPage.clearOTP()
            self.LoginPage.enterOTP(self.otp)
            self.LoginPage.ClickSubmit()

    @pytest.mark.run(order=2)
    @allure.testcase("Open Pradesh Level Data Entry Page")
    def test_openPradeshLevelDEPage(self):
        """
        Testing Open Pradesh level data Entry page functionality

        * Step 1: Click on Sangathan
        * Step 2: Choose Pradesh
        * Step 3: Choose Level

        """
        with allure.step("Click on Sangathan"):
            HomePage(self).clickSangathan()
            log.info("Clicked on Sangathan")
        with allure.step("Choose Pradesh"):
            SangathanPage(self).choosePradesh(self.Pradesh)
        with allure.step("Choose Level"):
            SangathanPage(self).chooseLevel(self.Level)

    @pytest.mark.depends(on=["test_Login", "test_openPradeshLevelDEPage"])
    @allure.testcase("Check if Assam is enabled")
    def test_checkPradesh(self):
        """
        Checking if correct pradesh is enabled or not

        * Step 1: Check if self.Pradesh is enabled

        """
        with allure.step("Check if " + self.Pradesh + " is enabled"):
            if PradeshLevelDEPage(self).pradeshIsEnabled(self.Pradesh):
                SangathanPage(self).crossPradesh()
            else:
                SangathanPage(self).choosePradesh(self.Pradesh)

    @pytest.mark.depends(on=["test_Login", "test_openPradeshLevelDEPage", "test_checkPradesh"])
    @allure.testcase("Fetch data by SubUnits")
    def test_fetchDataBySubUnit(self):
        """
        Testing fetch data by subunits functionality

        * Step 1: Checking if all three subunits are present
        * Step 2: Fetch Sorting types and store them in a list
        * Step 3: Click on each Subunit from above list
        * Step 4: Click on Subunit: SubUnit
        * Step 5: Change Sorting type: SortingType
        * Step 6: Assert Count

        """

        with allure.step("Checking if all three subunits are present"):
            SubUnits = PradeshLevelDEPage(self).fetchSubUnits()
            print(SubUnits)

        with allure.step("Fetch Sorting types and store them in a list"):
            SortingTypes = PradeshLevelDEPage(self).fetchSortingTypes()
            print(SortingTypes)

        with allure.step("Click on each Subunit from above list"):
            for SubUnit in SubUnits:
                with allure.step("Click on Subunit: " + SubUnit):
                    PradeshLevelDEPage(self).fetchDataBySubUnit(SubUnit)
                    TotalCount = PradeshLevelDEPage(self).getTotalCount()
                    print("The Total number of Karyakarta in " + SubUnit + " SubUnit is " + TotalCount[7:])

                    for SortingType in SortingTypes:
                        with allure.step("Change Sorting type: " + SortingType):
                            PradeshLevelDEPage(self).changeSortingType(SortingType)
                            Count = PradeshLevelDEPage(self).getTotalCount()
                            print("Sorting Type: " + SortingType + " and Count: " + Count)

                            with allure.step("Assert Count"):
                                assert Count == TotalCount

    @pytest.mark.depends(
        on=["test_Login", "test_openPradeshLevelDEPage", "test_checkPradesh", "test_fetchDataBySubUnit"])
    @allure.testcase("Change Morcha and Cell")
    def test_changeMorchaAndCell(self):
        """
        Test change Morcha and Cell and assert count for each

        * Step 1: Fetch Sorting types and store them in a list
        * Step 2: Change Morcha
        * Step 3: Change Sorting type: SortingType
        * Step 4: Assert Count
        * Step 5: Change Cell
        * Step 6: Change Sorting type: SortingType
        * Step 7: Assert Count

        """

        with allure.step("Fetch Sorting types and store them in a list"):
            SortingTypes = PradeshLevelDEPage(self).fetchSortingTypes()
            print(SortingTypes)

        with allure.step("Change Morcha"):
            PradeshLevelDEPage(self).changeMorcha("OBC")
            TotalCountMorcha = PradeshLevelDEPage(self).getTotalCount()
            print("The Total number of Karyakarta in OBC Morcha is " + TotalCountMorcha[7:])

            for SortingType in SortingTypes:  # Iterate through sorting types
                with allure.step("Change Sorting type: " + SortingType):
                    PradeshLevelDEPage(self).changeSortingType(SortingType)
                    Count = PradeshLevelDEPage(self).getTotalCount()
                    print("Sorting Type: " + SortingType + " and Count: " + Count)

                    with allure.step("Assert Count"):
                        assert Count == TotalCountMorcha

        with allure.step("Change Cell"):
            PradeshLevelDEPage(self).changeCell("IT Cell")
            TotalCountCell = PradeshLevelDEPage(self).getTotalCount()
            print("The Total number of Karyakarta in IT Cell is " + TotalCountCell[7:])

            for SortingType in SortingTypes:  # Iterate through sorting types
                with allure.step("Change Sorting type: " + SortingType):
                    PradeshLevelDEPage(self).changeSortingType(SortingType)
                    Count = PradeshLevelDEPage(self).getTotalCount()
                    print("Sorting Type: " + SortingType + " and Count: " + Count)

                    with allure.step("Assert Count"):
                        assert Count == TotalCountCell

    @pytest.mark.depends(
        on=["test_Login", "test_openPradeshLevelDEPage", "test_checkPradesh", "test_fetchDataBySubUnit",
            "test_changeMorchaAndCell"])
    @allure.testcase("Click on Karyakarta details page")
    def test_clickOnKaryakartaDetailsPage(self):
        """
        Test open Karyakarta details page

        * Step 1: Open Karyakarta Details page for first karyakarta
        * Step 2: Store details of Karyakarta
        * Step 3: Go back to Pradesh Level Data Entry Page

        """
        with allure.step("Open Karyakarta Details page for first karyakarta"):
            PradeshLevelDEPage(self).openKaryakartaDetailsPage()
        with allure.step("Store details of Karyakarta"):
            pass
        with allure.step("Go back to Pradesh Level Data Entry Page"):
            PradeshLevelDEPage(self).goBackPradeshLevelDEPage()

    @pytest.mark.depends(
        on=["test_Login", "test_openPradeshLevelDEPage", "test_checkPradesh", "test_fetchDataBySubUnit",
            "test_changeMorchaAndCell", "test_clickOnKaryakartaDetailsPage"])
    @allure.testcase("Click on Karyakarta details page")
    def test_karyakartaServices(self):
        """
        Test Karyakarta Services

        * Step 1: Swipe on Karyakarta
        * Step 2: Fetch Karyakarta Services list
        * Step 3: Click on each service and close

        """
        with allure.step("Swipe on Karyakarta"):
            PradeshLevelDEPage(self).swipeOnKaryakarta()
        with allure.step("Fetch Karyakarta Services list"):
            Services = PradeshLevelDEPage(self).fetchKaryakartaServices()
        with allure.step("Click on each service and close"):
            for Service in Services:
                PradeshLevelDEPage(self).clickOnKaryakartaService(Service)
                if Service == 'Verify':
                    PradeshLevelDEPage(self).close()
                    PradeshLevelDEPage(self).swipeOnKaryakarta()
                elif Service == 'Edit':
                    PradeshLevelDEPage(self).goBackPradeshLevelDEPage()
                    PradeshLevelDEPage(self).swipeOnKaryakarta()
                elif Service == 'Delete':
                    PradeshLevelDEPage(self).karyakartaDeleteServiceActions("Cancel")

    @pytest.mark.depends(
        on=["test_Login", "test_openPradeshLevelDEPage", "test_checkPradesh", "test_fetchDataBySubUnit",
            "test_changeMorchaAndCell", "test_clickOnKaryakartaDetailsPage", "test_karyakartaServices"])
    @allure.testcase("Click on Karyakarta details page")
    def test_clickCallOnKaryakarta(self):
        """
        Test Click on Call button for Karyakarta

        * Step 1: Click on call button next to a Karyakarta

        """
        with allure.step("Click on call button next to a Karyakarta"):
            PradeshLevelDEPage(self).clickCallOnKaryakarta()
