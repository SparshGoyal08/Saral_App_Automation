import traceback

import utils.logger as cl
from Pages.BasePage import BasePage


class PradeshLevelDEPage(BasePage):
    """
    This class contains all the methods needed to interact with elements on Pradesh Level Data Entry page

    The methods are:
        * pradeshIsEnabled
        * fetchSubUnits
        * fetchDataBySubUnit
        * changeMorcha
        * changeCell
        * getTotalCount
        * fetchSortingTypes
        * checkSortedBy
        * changeSortingType
        * openKaryakartaDetailsPage
        * goBackPradeshLevelDEPage
        * swipeOnKaryakarta
        * fetchKaryakartaServices
        * clickOnKaryakartaService
        * karyakartaDeleteServiceActions
        * clickCallOnKaryakarta
        * close
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger()

    TvLocation = "com.saral.application:id/tv_location"
    UnitsRow = "com.saral.application:id/rv_units"
    TotalCount = "com.saral.application:id/tv_count"
    KaryakartaList = "com.saral.application:id/rv_karyakarta"
    Karyakarta = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]"
    CallIcon = "com.saral.application:id/iv_call"
    CloseButton = "com.saral.application:id/iv_close"
    OfficeBearer = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[1]/android.widget.TextView"
    Karyakarni = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[2]/android.widget.TextView"
    Council = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[3]/android.widget.TextView"
    LastEntered = "com.saral.application:id/tv_date"
    Designation = "com.saral.application:id/tv_designation"
    A_Z = "com.saral.application:id/tv_alphabet"
    Verify = "com.saral.application:id/tv_verify"
    Edit = "com.saral.application:id/tv_edit"
    Delete = "com.saral.application:id/tv_delete"
    BackButton = "com.saral.application:id/iv_back"
    AddEntry = "com.saral.application:id/fab_add"
    SortingTypes = []
    SubUnits = []
    KaryakartaServices = []

    def pradeshIsEnabled(self, pradesh: str):
        """
        Choose Pradesh name when entering Sangathan Page first time
        :return: None
        """
        try:
            self.clickElement(self.TvLocation, "id")
            if self.isEnabled(pradesh, "text"):
                self.log.info(pradesh + " is enabled")
                return True
            else:
                self.log.info(pradesh + " is not enabled")
                return False
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchSubUnits(self):
        """
        Fetch Names of subunits
        :return: Subunit names
        """
        try:
            self.SubUnits.append(self.getText(self.OfficeBearer, "xpath"))
            self.SubUnits.append(self.getText(self.Karyakarni, "xpath"))
            self.SubUnits.append(self.getText(self.Council, "xpath"))
            self.log.info("Fetched the list of SubUnits:\n" + str(self.SubUnits))
            return self.SubUnits
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
            self.swipe(900, 510, 200, 510)
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
            self.swipe(850, 500, 250, 500)
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
            Total_Count = self.getText(self.TotalCount, "id")
            self.log.info("The " + Total_Count[0:7] + "is " + Total_Count[7:])
            return Total_Count
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchSortingTypes(self):
        """
        Fetch and Store Sorting types
        :return: list(SortingTypes)
        """
        try:
            self.SortingTypes.append(self.getText(self.LastEntered, "id"))
            self.SortingTypes.append(self.getText(self.Designation, "id"))
            self.SortingTypes.append(self.getText(self.A_Z, "id"))
            self.log.info("Fetched Sorting types:\n" + str(self.SortingTypes))
            return self.SortingTypes
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def changeSortingType(self, sortingtype):
        """
        Change the sorting type
        :param sortingtype: sorting type attribute
        :return: None
        """
        try:
            self.clickElement(sortingtype, "text")
            self.log.info("Changed the sorting type to: " + sortingtype)
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

    def goBackPradeshLevelDEPage(self):
        """
        Go back to Pradesh Level DE Page from Karyakarta details page
        :return: None
        """
        try:
            self.clickElement(self.BackButton, "id")
            self.log.info("Going Back to Pradesh Level Data Entry Page")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def swipeOnKaryakarta(self):
        """
        Swipe on karyakarta row to reveal services
        :return: None
        """
        try:
            self.swipe(850, 920, 250, 920)
            self.log.info("Swiping on Karyakarta record to view services")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchKaryakartaServices(self):
        """
        Fetch all the services that are visible on swiping on Karyakarta record
        :return: list(KaryakartaServices)
        """
        try:
            if self.isDisplayed(self.Verify, "id"):
                self.KaryakartaServices.append(self.getText(self.Verify, "id"))
                self.log.info("Verify Service available, adding it to list")
            if self.isDisplayed(self.Edit, "id"):
                self.KaryakartaServices.append(self.getText(self.Edit, "id"))
                self.log.info("Edit Service available, adding it to list")
            if self.isDisplayed(self.Delete, "id"):
                self.KaryakartaServices.append(self.getText(self.Delete, "id"))
                self.log.info("Delete Service available, adding it to list")
            self.log.info("Services identified are:\n" + str(self.KaryakartaServices))
            return self.KaryakartaServices
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def clickOnKaryakartaService(self, servicename):
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

    def karyakartaDeleteServiceActions(self, action):
        """
        Select options based on action provided in test on delete form
        :param action: Action type
        :return: None
        """
        try:
            self.clickElement(action, "text")
            self.log.info("Clicked on Action: " + action)
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

    def clickAddEntryButton(self):
        """
        Click on Add new entry button
        :return: self.clickAddEntryButton
        """
        try:
            self.clickElement(self.AddEntry, "id")
            self.log.info("Adding a new Entry")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def close(self):
        """
        Close dialogue box
        :return: None
        """
        try:
            self.clickElement(self.CloseButton, "id")
            self.log.info("Close dialogue box")
        except Exception as e:
            # self.ExceptionHandler.handleException(self.driver, e)
            traceback.print_exception(type(e), e, e.__traceback__)
