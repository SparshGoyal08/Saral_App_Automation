import re
import time
import unittest

import allure
import pytest

import Drivers.Drivers as Driver
from App.AndroidEmulator import AndroidEmulator
from App.AppiumServer import *
from Pages.BasePage import BasePage
from Pages.DataEntryForm import DataEntryForm
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
    time.sleep(20)
    AppiumServiceInstance = AppiumServiceClass()
    subprocess.Popen("C:/Users/DELL/Saral_App_Automation/Resources/FreePorts.bat")
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
@allure.suite("Data Entry Form Test Cases Suite")
class DataEntryFormCases(unittest.TestCase):
    """
    This is Data Entry Form Test cases class to test data entry form
    """
    MobileNo = "8287210847"
    otp = "010203"
    Pradesh = "Assam"
    Level = "Pradesh"
    Name = "John Doe"
    Designation = "Prabhari"
    PhoneNumbers = ["1234567890", "8860345598"]
    PhonePattern = "^[5-9][0-9]{9}$"
    GuardianName = ["John Doe Father"]
    Status = ["Yes", "No", "Clear", "Yes"]
    PrimaryMemberID = ["123", "5678", "1234567890"]
    PrimaryMemberPattern = "^[1-4][0-9]{9}$"
    Ages = ["17", "200", "18"]
    AgePattern = "^(18|19|[2-9]\\d|1\\d\\d)$"
    BloodGroup = "B+"
    Genders = ["Male", "Female", "Other"]
    STDCodes = [1, 2, 12345678]
    STDCodePattern = "^\\d{2,8}$"
    LandlineNumbers = ["0123456789", "9876543210"]
    LandlinePattern = "^[1-9]\\d{1,19}$"
    Emails = ["john.doe", "@example.com", "john.doe@example.com"]
    EmailPattern = "^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,10}$"
    ActualDOB = "10 January 2005"
    ExpectedDB = "10/01/2005"
    Address = "Sample address 123 @ नमूना पता"
    VillageWard = "Sample Village Name. नमूना ग्राम का नाम|"
    Tehsil = "Sample Tehsil Name. नमूना तहसील का नाम|"
    District = "Baksa"
    PinCodes = ["000000", "012345", "12345", "123456"]
    PinCodePattern = "^[1-9][0-9]{5}$"
    Profession = "Teacher"
    VidhanSabha = "1 - Ratabari"
    Booth = ["0", "1251", "100"]
    BoothPattern = "^([1-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1][0-2][0-4][0-9]|1250)$"
    VoterIDs = ["12345678!", "X1Y2Z3A4B5C6D7E8F9"]
    VoterIDPattern = "^[A-Z0-9]{9,20}$"
    AadhaarNumbers = ["1234567890", "123456789012"]
    AadharPattern = "^[0-9]{12}$"
    PannaNumbers = ["2", "41"]
    PannaNumberPattern = "^([3-9]|[12345][0-9]|40)$"
    RationNumbers = ["AB12", "1234", "1234ABCD5678"]
    RationNumberPattern = "^[A-Z0-9]{8,}$"
    Facebook = "www.fb.com/johndoe"
    Twitter = "www.twitter.com/johndoe"
    Instagram = "www.instagram.com/johndoe"
    Linkedin = "www.linkedin.com/johndoe"
    SubCaste = "Sample SubCaste"
    Qualification = "Sample Qualification Input"
    ActiveMemberID = "SMPL123@xyz"
    PartyZila = "Baksa"
    PartyMandal = "Musalpur"

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

    @pytest.mark.depends(on=["test_Login"])
    @allure.testcase("Go to data Entry form")
    def test_goToDataEntryForm(self):
        """
        Testing go to Data Entry form

        Step 1: Go to Pradesh Level Data Entry Page\n
        Step 2: Go to Data Entry Form

        """
        with allure.step("Go to Pradesh Level Data Entry Page"):
            HomePage(self).clickSangathan()
            SangathanPage(self).choosePradesh(self.Pradesh)
            SangathanPage(self).chooseLevel(self.Level)
            log.info("Pradesh Level Data Entry Page visible")
        with allure.step("Go to Data Entry Form"):
            PradeshLevelDEPage(self).clickAddEntryButton()
            log.info("On data Entry Form")

    @pytest.mark.depends(on=["test_Login", "test_goToDataEntryForm"])
    @allure.testcase("Test Mandatory (*) Primary fields")
    def test_mandatoryPrimaryFields(self):
        """
        Testing Mandatory (*) Primary Fields

        Step 1: Enter Name
            > Assert Name
        Step 2: Input Designation
            > Assert Designation
        Step 3: Enter Phone number
            > Assert Entered Phone number matches allowed pattern\n
            > Fetch Error message in else case
        Step 4: Choose Inchargee
            > Assert Inchargee

        """
        with allure.step("Enter Name"):
            DataEntryForm(self).inputName(self.Name)
            with allure.step("Assert " + self.Name):
                CurrentName = BasePage(self).isDisplayed(self.Name, "text")
                assert CurrentName
        with allure.step("Input Designation"):
            DataEntryForm(self).chooseDesignation(self.Designation)
            with allure.step("Assert " + self.Designation):
                CurrentDesignation = BasePage(self).isDisplayed(self.Designation, "text")
                assert CurrentDesignation
        with allure.step("Enter Phone number"):
            for phonenumber in self.PhoneNumbers:
                DataEntryForm(self).inputPhoneNumber(phonenumber)
                with allure.step("Assert " + phonenumber + " Pattern matches " + self.PhonePattern):
                    if re.match(self.PhonePattern, phonenumber):
                        log.info(phonenumber + " Phone Number pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid phone number", "text")
                        assert ErrorMessage
                        BasePage(self).clear(phonenumber, "text")
        with allure.step("Choose Inchargee"):
            BasePage(self).scrollIntoView("Inchargeeee*", "text")
            InchargeeList = DataEntryForm(self).fetchInchargees()
            for Inchargee in InchargeeList:
                DataEntryForm(self).chooseInchargee(Inchargee)
                with allure.step("Assert " + Inchargee):
                    CurrentInchargee = BasePage(self).isDisplayed(Inchargee, "text")
                    assert CurrentInchargee

    @pytest.mark.depends(on=["test_Login", "test_goToDataEntryForm", "test_mandatoryPrimaryFields"])
    @allure.testcase("Test Non-Mandatory (-*-) Primary fields")
    def test_nonMandatoryPrimaryFields(self):
        """
        Testing Non-Mandatory (-*-) Primary Fields

        Step 1: Enter Father's/Husband's Name
            > Assert Guardian name
        Step 2: Check SmartPhone availability
            > Assert SmartPhone status is enabled
        Step 3: Enter Primary Member ID
            > Assert Primary member ID Pattern matches allowed\n
            > Fetch Error Message else
        Step 4: Enter Age
            > Assert entered age is accuarate based on allowed range\n
            > Fetch error message else

        """
        BasePage(self).scrollIntoView("Name*", "text")
        with allure.step("Enter Father's/Husband's Name"):
            for guardian in self.GuardianName:
                DataEntryForm(self).inputFatherHusbandName(guardian)
                with allure.step("Assert " + guardian):
                    CurrentGuardianName = BasePage(self).isDisplayed(guardian, "text")
                    if CurrentGuardianName:
                        assert True
                    else:
                        BasePage(self).clear(guardian, "text")
        with allure.step("Check SmartPhone availability"):
            for smartphonestatus in self.Status:
                DataEntryForm(self).chooseSmartPhoneAvailability(smartphonestatus)
                with allure.step("Assert " + smartphonestatus + " is enabled"):
                    CurrentSmartPhoneStatus = BasePage(self).isEnabled(smartphonestatus, "text")
                    assert CurrentSmartPhoneStatus is True
        with allure.step("Enter Primary Member ID"):
            for primarymemberid in self.PrimaryMemberID:
                DataEntryForm(self).inputMemberID(primarymemberid)
                with allure.step("Assert " + primarymemberid + " Pattern matches " + self.PrimaryMemberPattern):
                    if re.match(self.PrimaryMemberPattern, primarymemberid):
                        log.info(primarymemberid + " Primary Member ID pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid primary member id", "text")
                        assert ErrorMessage
                        BasePage(self).clear(primarymemberid, "text")
        with allure.step("Enter Age"):
            BasePage(self).scrollIntoView("Fill Secondary Information", "text")
            for age in self.Ages:
                DataEntryForm(self).inputAge(age)
                with allure.step("Assert " + age + " is accurate according to " + self.AgePattern):
                    if re.match(self.AgePattern, age):
                        log.info(age + " age pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid age", "text")
                        assert ErrorMessage
                        BasePage(self).isDisplayed("Blood Group", "text")
                        BasePage(self).clear(age, "text")

    @pytest.mark.depends(
        on=["test_Login", "test_goToDataEntryForm", "test_mandatoryPrimaryFields", "test_nonMandatoryPrimaryFields"])
    @allure.testcase("Test Secondary fields")
    def test_secondaryFields(self):
        """
        Test Secondary Information Fields

        Step 1: Open Secondary Fields\n
        Step 2: Enter Blood Group\n
        Step 3: Choose Gender
            > Assert Enter Gender is enabled\n
        Step 4: Enter Whatsapp Number
            > Assert entered WhatsApp Numbers' pattern matches allowed pattern\n
            > Fetch Error Message else\n
        Step 5: Enter STD Code
            > Assert entered STD Code pattern matches allowed pattern\n
            > Fetch Error message else\n
        Step 6: Enter Landline Number
            > Assert entered Landline number pattern matches allowed pattern\n
            > Fetch error message else\n
        Step 7: Fetch Categories\n
        Step 8: Choose Category
            > Assert Category\n
        Step 9: Choose Caste
            > Assert Caste\n
        Step 10: Enter New Caste
            > Assert New Caste\n
        Step 11: Enter Email
            > Assert entered email pattern matches allowed pattern\n
            > Fetch error message else\n
        Step 12: Choose DOB
            > Assert DOB\n
        Step 13: Enter Address
            > Assert Address\n
        Step 14: Enter Village/Ward Name
            > Assert Village/Ward Name\n
        Step 15: Enter Tehsil
            > Assert Tehsil\n
        Step 16: Choose District
            > Assert District\n
        Step 17: Enter Pin Code
            > Assert entered PIN Code pattern matches allowed pattern\n
            > Fetch Error message else\n
        Step 18: Fetch Education List\n
        Step 19: Choose Education
            > Assert Education\n
        Step 20: Choose Profession
            > Assert Profession\n
        Step 21: Check Bike Status
            > Assert Bike Status\n
        Step 22: Check Car Status
            > Assert Car Status\n
        Step 23: Choose Vidhan Sabha where He/She Votes
            > Assert Vidhan Sabha\n
        Step 24: Enter Booth where He/She Votes
            > Assert Booth pattern matches allowed pattern\n
            > Fetch error message else\n
        Step 25: Enter Voter ID
            > Assert Voter ID pattern matches allowed pattern\n
            > Fetch Error Message else\n
        Step 26: Enter Aadhaar Number
            > Assert Aadhaar number entered pattern matches allowed pattern\n
            > Fetch error message else\n
        Step 27: Enter Panna Number
            > Assert entered Panna Number pattern matches allowed pattern\n
            > Fetch Error message else\n
        Step 28: Enter Ration Card Number
            > Assert enetered ration card number pattern matches allowed pattern\n
            > Fetch Error message else\n
        Step 29: Enter Social Media profile links\n
        Step 30: Fetch Salutation list\n
        Step 31: Choose Salutation
            > Assert Salutation\n
        Step 32: Enter Sub Caste\n
        Step 33: Enter Qualification\n
        Step 34: Fetch Religion List\n
        Step 35: Choose Religion
            > Assert Religion\n
        Step 36: Enter Active member ID\n
        Step 37: Choose Party Mandal before Party Zila\n
        Step 38: Choose Party Party Zila\n
        Step 39: Choose Party Mandal\n

        """
        with allure.step("Open Secondary Fields"):
            BasePage(self).scrollIntoView("Fill Secondary Information", "text")
            if BasePage(self).isDisplayed("Blood Group", "text"):
                log.info("Secondary Information fields already visible")
            else:
                DataEntryForm(self).clickSecondaryInformationButton()
        with allure.step("Enter Blood Group"):
            BasePage(self).scrollIntoView("WhatsApp Number", "text")
            DataEntryForm(self).inputBloodGroup(self.BloodGroup)
        with allure.step("Choose Gender"):
            for gender in self.Genders:
                DataEntryForm(self).chooseGender(gender)
                with allure.step("Assert " + gender + " is enabled"):
                    CurrentGender = BasePage(self).isEnabled(gender, "text")
                    assert CurrentGender is True
        with allure.step("Enter Whatsapp Number"):
            for whatsapp in self.PhoneNumbers:
                DataEntryForm(self).inputWhatsappNumber(whatsapp)
                with allure.step("Assert " + whatsapp + " pattern matches " + self.PhonePattern):
                    if re.match(self.PhonePattern, whatsapp):
                        log.info(whatsapp + " Whatsapp Number pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid whatsapp number", "text")
                        assert ErrorMessage
                        BasePage(self).clear(whatsapp, "text")
        with allure.step("Enter STD Code"):
            for stdcode in self.STDCodes:
                DataEntryForm(self).inputSTDCode(stdcode)
                with allure.step("Assert " + str(stdcode) + " pattern matches " + self.STDCodePattern):
                    if re.match(self.STDCodePattern, str(stdcode)):
                        log.info(str(stdcode) + " STD Code pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid std code", "text")
                        assert ErrorMessage
                        BasePage(self).clear(str(stdcode), "text")
        with allure.step("Enter Landline Number"):
            BasePage(self).scrollIntoView("Email", "text")
            for landline in self.LandlineNumbers:
                DataEntryForm(self).inputLandline(landline)
                with allure.step("Assert " + landline + " pattern matches " + self.LandlinePattern):
                    if re.match(self.LandlinePattern, landline):
                        log.info(landline + " Landline Number pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid landline", "text")
                        assert ErrorMessage
                        BasePage(self).clear(landline, "text")
        with allure.step("Fetch Categories"):
            CategoryList = DataEntryForm(self).fetchCategory()
        with allure.step("Choose Category"):
            DataEntryForm(self).chooseCategory(CategoryList[0])
            with allure.step("Assert " + CategoryList[0]):
                CurrentCategory = BasePage(self).isDisplayed(CategoryList[0], "text")
                assert CurrentCategory
        with allure.step("Choose Caste"):
            DataEntryForm(self).chooseCaste("Brahmin")
            with allure.step("Assert Brahmin"):
                CurrentCaste = BasePage(self).isDisplayed("Brahmin", "text")
                assert CurrentCaste
        with allure.step("Enter New Caste"):
            DataEntryForm(self).chooseCategory(CategoryList[4])
            DataEntryForm(self).addNewCaste("New Caste")
            with allure.step("Assert New Caste"):
                CurrentNewCaste = BasePage(self).isDisplayed("New Caste", "text")
                assert CurrentNewCaste
        with allure.step("Enter Email"):
            for email in self.Emails:
                DataEntryForm(self).inputEmail(email)
                with allure.step("Assert " + email + " Pattern matches " + self.EmailPattern):
                    if re.match(self.EmailPattern, email):
                        log.info(email + " Email pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid email address", "text")
                        assert ErrorMessage
                        BasePage(self).clear(email, "text")
        with allure.step("Choose DOB"):
            DataEntryForm(self).chooseDOB(self.ActualDOB, "OK")
            with allure.step("Assert " + self.ActualDOB):
                assert BasePage(self).isDisplayed(self.ExpectedDB, "text")
        with allure.step("Enter Address"):
            DataEntryForm(self).inputAddress(self.Address)
            with allure.step("Assert " + self.Address):
                CurrentAddress = BasePage(self).isDisplayed(self.Address, "text")
                assert CurrentAddress
        with allure.step("Enter Village"):
            DataEntryForm(self).inputVillageWard(self.VillageWard)
            with allure.step("Assert " + self.VillageWard):
                CurrentVillageWardName = BasePage(self).isDisplayed(self.VillageWard, "text")
                assert CurrentVillageWardName
        with allure.step("Enter Tehsil"):
            BasePage(self).scrollIntoView("Education", "text")
            DataEntryForm(self).inputTehsil(self.Tehsil)
            with allure.step("Assert " + self.Tehsil):
                CurrentTehsilName = BasePage(self).isDisplayed(self.Tehsil, "text")
                assert CurrentTehsilName
        with allure.step("Choose District"):
            DataEntryForm(self).chooseDistrict(self.District)
            with allure.step("Assert " + self.District):
                CurrentDistrictName = BasePage(self).isDisplayed(self.District, "text")
                assert CurrentDistrictName
        with allure.step("Enter Pin Code"):
            for pincode in self.PinCodes:
                DataEntryForm(self).inputPinCode(pincode)
                with allure.step("Assert " + pincode + " pattern matches " + self.PinCodePattern):
                    if re.match(self.PinCodePattern, pincode):
                        log.info(pincode + " Pin Code pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid pincode", "text")
                        assert ErrorMessage
                        BasePage(self).clear(pincode, "text")
        with allure.step("Fetch Education List"):
            EducationList = DataEntryForm(self).fetchEducationList()
        with allure.step("Choose Education"):
            for education in EducationList:
                DataEntryForm(self).chooseEducation(education)
                with allure.step("Assert " + education):
                    CurrentEducation = BasePage(self).isDisplayed(education, "text")
                    assert CurrentEducation
        with allure.step("Choose Profession"):
            DataEntryForm(self).chooseProfession(self.Profession)
            with allure.step("Assert " + self.Profession):
                CurrentProfession = BasePage(self).isDisplayed(self.Profession, "text")
                assert CurrentProfession
        with allure.step("Bike Status"):
            for bikestatus in self.Status:
                DataEntryForm(self).checkBikeStatus(bikestatus)
                with allure.step("Assert " + bikestatus):
                    CurrentBikeStatus = BasePage(self).isEnabled(bikestatus, "text")
                    assert CurrentBikeStatus
        with allure.step("Car Status"):
            for carstatus in self.Status:
                DataEntryForm(self).checkCarStatus(carstatus)
                with allure.step("Assert " + carstatus):
                    CurrentCarStatus = BasePage(self).isEnabled(carstatus, "text")
                    assert CurrentCarStatus
        with allure.step("Choose Vidhan Sabha where He/She Votes"):
            DataEntryForm(self).chooseVidhanSabha(self.VidhanSabha)
            with allure.step("Assert " + self.VidhanSabha):
                CurrentVidhanSabha = BasePage(self).isDisplayed(self.VidhanSabha, "text")
                assert CurrentVidhanSabha
        with allure.step("Choose Booth where He/She Votes"):
            BasePage(self).scrollIntoView("Panna Number", "text")
            for booth in self.Booth:
                DataEntryForm(self).inputBooth(booth)
                with allure.step("Assert " + booth + " pattern matches " + self.BoothPattern):
                    if re.match(self.BoothPattern, booth):
                        log.info(booth + " Booth number pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid booth", "text")
                        assert ErrorMessage
                        BasePage(self).clear(booth, "text")
        with allure.step("Enter Voter ID"):
            for voterid in self.VoterIDs:
                DataEntryForm(self).inputVoterID(voterid)
                with allure.step("Assert " + voterid + " Pattern matches " + self.VoterIDPattern):
                    if re.match(self.VoterIDPattern, voterid):
                        log.info(voterid + " Voter ID pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid voter id", "text")
                        assert ErrorMessage
                        BasePage(self).clear(voterid, "text")
        with allure.step("Enter Aadhaar Number"):
            for aadhaar in self.AadhaarNumbers:
                DataEntryForm(self).inputAadhaar(aadhaar)
                with allure.step("Assert " + aadhaar + " Pattern matches " + self.AadharPattern):
                    if re.match(self.AadharPattern, aadhaar):
                        log.info(aadhaar + " Aadhaar Number pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid aadhaar number", "text")
                        assert ErrorMessage
                        BasePage(self).clear(aadhaar, "text")
        with allure.step("Enter Panna Number"):
            for panna in self.PannaNumbers:
                DataEntryForm(self).inputPannaNumber(panna)
                with allure.step("Assert " + panna + " Pattern matches " + self.PannaNumberPattern):
                    if re.match(self.PannaNumberPattern, panna):
                        log.info(panna + " Panna Number pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid panna number", "text")
                        assert ErrorMessage
                        BasePage(self).clear(panna, "text")
        with allure.step("Enter Ration card number"):
            for ration in self.RationNumbers:
                DataEntryForm(self).inputRationCardNumber(ration)
                with allure.step("Assert " + ration + " Pattern matches " + self.RationNumberPattern):
                    if re.match(self.RationNumberPattern, ration):
                        log.info(ration + " Ration Card Number pattern is accurate")
                        assert True
                    else:
                        ErrorMessage = BasePage(self).isDisplayed("Enter valid ration card number", "text")
                        assert ErrorMessage
                        BasePage(self).clear(ration, "text")
        with allure.step("Enter Social Media"):
            with allure.step("Enter Facebook"):
                DataEntryForm(self).inputFacebook(self.Facebook)
            with allure.step("Enter Twitter"):
                DataEntryForm(self).inputTwitter(self.Twitter)
            with allure.step("Enter Instagram"):
                BasePage(self).scrollIntoView("Sub caste", "text")
                DataEntryForm(self).inputInstagram(self.Instagram)
            with allure.step("Enter Linkedin"):
                DataEntryForm(self).inputLinkedin(self.Linkedin)
        with allure.step("Fetch Salutations"):
            SalutationsList = DataEntryForm(self).fetchSalutation()
        with allure.step("Choose Salutation"):
            for salutation in SalutationsList:
                DataEntryForm(self).chooseSalutation(salutation)
                with allure.step("Assert " + salutation):
                    CurrentSalutation = BasePage(self).isDisplayed(salutation, "text")
                    assert CurrentSalutation
        with allure.step("Enter SubCaste"):
            DataEntryForm(self).inputSubCaste(self.SubCaste)
        with allure.step("Enter Qualification"):
            DataEntryForm(self).inputQualification(self.Qualification)
        with allure.step("Fetch Religions"):
            ReligionList = DataEntryForm(self).fetchReligionList()
        with allure.step("Choose Religion"):
            for religion in ReligionList:
                DataEntryForm(self).chooseReligion(religion)
                with allure.step("Assert " + religion):
                    CurrentReligion = BasePage(self).isDisplayed(religion, "text")
                    assert CurrentReligion
        with allure.step("Enter Active member ID"):
            DataEntryForm(self).inputActiveMemberID(self.ActiveMemberID)
        with allure.step("Choose Party Mandal before Party Zila"):
            BasePage(self).scrollIntoView("Preview & Submit Details", "text")
            # DataEntryForm(self).choosePartyMandal(self.PartyMandal)
            # Todo fetch, print and assert toast message here
        with allure.step("Choose Party Zila"):
            DataEntryForm(self).choosePartyZila(self.PartyZila)
        with allure.step("Choose Party Mandal"):
            DataEntryForm(self).choosePartyMandal(self.PartyMandal)
