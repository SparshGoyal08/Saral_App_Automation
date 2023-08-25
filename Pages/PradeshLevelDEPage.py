import traceback

import utils.logger as cl
from Pages.BasePage import BasePage


class PradeshLevelDEPage(BasePage):
    """
    This class contains all the methods needed to interact with elements on Pradesh Level Data Entry page

    The methods are:
        * choosePradesh
        * fetchSubUnits
        * fetchDataBySubUnit
        * changeMorcha
        * changeCell
        * getTotalCount
        * checkSortedBy
        * changeSortingType
        * openKaryakartaDetailsPage
        * swipeOnKaryakarta
        * KaryakartaService
        * clickCallOnKaryakarta
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger()

    TvLocation = "com.saral.application:id/tv_location"
    UnitsRow = "com.saral.application:id/rv_units"
    TotalCount = "com.saral.application:id/tv_count"
    SortingTypes = ["Last Entered", "Designation", "A-Z"]
    KaryakartaList = "com.saral.application:id/rv_karyakarta"
    Karyakarta = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]"
    CallIcon = "com.saral.application:id/iv_call"

    def choosePradesh(self):
        """
        Choose Pardesh name when entering Sangathan Page first time
        :return: None
        """
        try:
            self.clickElement(self.TvLocation, "id")
            self.log.info("Clicked on Change Pradesh drop down")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchSubUnits(self):
        """
        Fetch Names of subunits
        :return: Subunit names
        """
        try:
            OfficeBearer = self.getElement("Office Bearer", "text")
            Karyakarni = self.getElement("Karyakarni", "text")
            Council = self.getElement("Council", "text")
            return OfficeBearer, Karyakarni, Council
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchDataBySubUnit(self, SubUnit):
        """
        Click on any subunit and fetch data by subunit
        :param SubUnit: Subunit name
        :return: None
        """
        try:
            self.clickElement(SubUnit, "text")
            self.log.info("Sorted the list by: " + SubUnit)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def changeMorcha(self, morchaname):
        """
        Change Morcha type
        :param morchaname: Name of the morcha to be changed to
        :return: None
        """
        try:
            self.swipe(self.UnitsRow, "id", 850, 500, 250, 500, 100)
            self.clickElement("Morcha", "text")
            self.clickElement(morchaname, "text")
            self.log.info("Changed Morcha type to: " + morchaname)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def changeCell(self, cellname):
        """
        Change cell name
        :param cellname: Name of the cell to be changed to
        :return: None
        """
        try:
            self.swipe(self.UnitsRow, "id", 850, 500, 250, 500, 100)
            self.clickElement("Cell", "text")
            self.clickElement(cellname, "text")
            self.log.info("Changed Cell type to: " + cellname)
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def getTotalCount(self):
        """
        Get total count of karyakartas
        :return: Total Count value (str)
        """
        try:
            Total_Count = self.getElement(self.TotalCount, "id")
            self.log.info("The " + Total_Count[0:7] + "is " + Total_Count[7:])
            return Total_Count
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def checkSortedBy(self):
        """
        Check which attributes is used for sorting now
        :return: None
        """
        try:
            for SortingType in self.SortingTypes:
                if self.isEnabled(SortingType, "text"):
                    self.log.info("Current Sorting Type is: " + SortingType)
                    CurrentSortingType = SortingType
                    return CurrentSortingType
                else:
                    continue
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def changeSortingType(self, sortingtype):
        """
        Change the sorting type
        :param sortingtype: sorting type attribute
        :return:
        """
        try:
            if sortingtype != self.checkSortedBy():
                self.clickElement(sortingtype, "text")
                self.log.info("Changed the sorting type to: " + sortingtype)
            else:
                print(sortingtype + " is already selected, choose another sorting type from\n" + self.SortingTypes)
                self.changeSortingType(sortingtype)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def openKaryakartaDetailsPage(self):
        """
        Open Karyakarta details page
        :return: None
        """
        try:
            self.clickElement(self.Karyakarta, "xpath")
            self.log.info("Clicked on first karyakarta")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def swipeOnKaryakarta(self):
        """
        Swipe on karyakarta row to reveal services
        :return: None
        """
        try:
            self.swipe(self.Karyakarta, "xpath", 850, 920, 250, 920, 100)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def KaryakartaService(self, servicename):
        """
        Click on Service name after swiping
        :param servicename: name of the service
        :return: None
        """
        try:
            self.clickElement(servicename, "text")
            self.log.info("Clicked on " + servicename + " service")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def clickCallOnKaryakarta(self):
        """
        Click on call button for the first record
        :return: None
        """
        try:
            self.clickElement(self.CallIcon, "id")
            self.log.info("Clicked on Call Icon")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)
