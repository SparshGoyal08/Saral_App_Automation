import traceback

import utils.logger as cl
from Pages.BasePage import BasePage


class DataEntryForm(BasePage):
    """
    This class contains all the methods needed to interact with elements on Data Entry Form

    The methods are:
        * uploadImage
        * Input Name
        * inputFatherHusbandName
        * chooseDesignation
        * chooseSmartPhoneAvailability
        * inputPhoneNumber
        * inputMemberID
        * inputAge
        * fetchInchargee
        * inputInchargee
        * clickSecondaryInformationButton
        * inputBloodGroup
        * chooseGender
        * inputWhatsappNumber
        * inputSTDCode
        * inputLandlineNumber
        * fetchCategory
        * chooseCategory
        * fetchCaste
        * chooseCaste
        * addNewCaste
        * inputEmail
        * chooseDOB
        * inputFullAddress
        * inputVillageWard
        * inputTehsil
        * chooseDistrict
        * inputPinCode
        * fetchEducation
        * chooseEducation
        * chooseProfession
        * checkBikeStatus
        * checkCarStatus
        * inputVoterID
        * uploadVoterID
        * inputAadhaar
        * uploadAadhaar
        * inputPannaNumber
        * inputRation
        * uploadRation
        * inputFacebook
        * inputTwitter
        * inputInstagram
        * inputLinkedin
        * fetchSalutation
        * chooseSalutation
        * inputSubCaste
        * inputQualification
        * fetchReligion
        * chooseReligion
        * inputActiveMemberID
        * choosePartyZila
        * choosePartyMandal
        * clickPreviewandSubmit
        * close
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger()

    AddPhoto = "com.saral.application:id/iv_photo"
    AddPhotoCamera = "com.saral.application:id/iv_camera"
    PhotoDestination = "/storage/emulated/0/Download/KaryakartaImage.jpg"
    JohnDoe = "C:/Users/DELL/Saral_App_Automation/Resources/KaryakartaImage.jpg"
    AllowButton = "com.android.packageinstaller:id/permission_allow_button"
    Image = "KaryakartaImage.jpg"
    Name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.EditText"
    Father_HusbandName = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.EditText"
    DesignationDropDown = "com.saral.application:id/tv_value"
    PhoneNumber = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.EditText"
    PrimaryMemberID = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.widget.EditText"
    Age = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.EditText"
    InchargeeDropDown = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.widget.TextView[2]"
    InchargeeList = []
    SecondaryInfo = "com.saral.application:id/tv_secondary"
    BloodGroup = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[1]/android.widget.EditText"
    WhatsAppNumber = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.EditText"
    STDCode = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.EditText"
    LandlineNumber = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.EditText"
    CategoryDropDown = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[2]"
    CategoryList = []
    CasteDropDown = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView[2]"
    AddCaste = "com.saral.application:id/iv_add"
    NewCaste = "com.saral.application:id/et_caste"
    Submit = "com.saral.application:id/btn_submit"
    CasteList = []
    Email = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.EditText"
    DOB = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView[2]"
    OK = "android:id/button1"
    Cancel = "android:id/button2"
    FullAddress = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.widget.EditText"
    VillageWard = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[8]/android.widget.EditText"
    Tehsil = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.EditText"
    Disrict = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[2]"
    PinCode = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.EditText"
    EducationDropDown = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView[2]"
    EducationList = []
    ProfessionDropDown = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView[2]"
    VidhanSabhaDropDown = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[9]/android.widget.TextView[2]"
    Booth = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.EditText"
    VoterIDInput = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.EditText"
    VoterIDDestination = "/storage/emulated/0/Download/JohnDoeVoterID.jpg"
    JohnDoeVoterID = "C:/Users/DELL/Saral_App_Automation/Resources/JohnDoeVoterID.jpg"
    AadhaarInput = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.EditText"
    AadhaarDestination = "storage/emulated/0/Download/JohnDoeAadhaar.jpg"
    JohnDoeAadhaar = "C:/Users/DELL/Saral_App_Automation/Resources/JohnDoeAadhaar.jpg"
    PannaNumber = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.EditText"
    RationCardNumberInput = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.view.ViewGroup/android.widget.EditText"
    RationCardDestination = "/storage/emulated/0/Download/JohnDoeRationCard.jpg"
    JohnDoeRationCard = "C:/Users/DELL/Saral_App_Automation/Resources/JohnDoeRationCard.jpg"
    SalutationDropDown = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView[2]"
    SalutationList = []
    SubCaste = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.EditText"
    Qualification = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.EditText"
    ReligionDropDown = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.widget.TextView[2]"
    ReligionList = []
    ActiveMember = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[8]/android.widget.EditText"
    PartyZila = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView[2]"
    PartyMandal = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.widget.TextView[2]"
    PreviewButton = 'com.saral.application:id/btn_preview'
    CloseButton = "com.saral.application:id/iv_close"

    def uploadImage(self):
        """
        Upload Karyakarta image
        :return: self.uploadImage
        """
        try:
            self.pushFile(self.PhotoDestination, self.JohnDoe)
            self.clickElement(self.AddPhoto, "id")
            self.clickElement("Gallery", "text")
            self.clickElement(self.AllowButton, "id")
            self.clickElement(self.Image, "text")
            self.log.info("Uploaded Image: " + self.JohnDoe)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputName(self, name):
        """
        Input Karyakarta name
        :param name: name of karyakarta
        :return: self.inputName
        """
        try:
            self.sendKeys(name, self.Name, "xpath")
            self.log.info("Entered Name as: " + name)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputFatherHusbandName(self, fathername):
        """
        Input Father's/Husband's Name
        :param fathername: name of father or husband
        :return: self.inputFatherHusbandName
        """
        try:
            self.sendKeys(fathername, self.Father_HusbandName, "xpath")
            self.log.info("Entered Father/Husband's name: " + fathername)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseDesignation(self, designation):
        """
        choose karyakarta designation
        :param designation: designation name
        :return: self.chooseDesignation
        """
        try:
            self.clickElement(self.DesignationDropDown, "id")
            self.clickElement(designation, "text")
            self.log.info("Added a new Designation as: " + designation)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseSmartPhoneAvailability(self, hassmartphone):
        """
        choose if karyakarta has smartphone
        :param hassmartphone: yes or no
        :return: self.chooseSmartPhoneAvailability
        """
        try:
            self.clickElement(hassmartphone, "text")
            self.log.info("SmartPhone availability: " + hassmartphone)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputPhoneNumber(self, phonenumber):
        """
        input karyakarta phone number
        :param phonenumber: phone number of karyakarta
        :return: self.inputPhoneNumber
        """
        try:
            self.sendKeys(phonenumber, self.PhoneNumber, "xpath")
            self.log.info("Entered Phone Number as: " + phonenumber)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputMemberID(self, memberid):
        """
        Input Primary member id of karyakarta
        :param memberid: member id
        :return: self.inputMemberID
        """
        try:
            self.sendKeys(memberid, self.PrimaryMemberID, "xpath")
            self.log.info("Entered Primary Member ID as: " + memberid)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputAge(self, age):
        """
        Input age of karyakarta
        :param age: age
        :return: self.inputAge
        """
        try:
            self.sendKeys(age, self.Age, "xpath")
            self.log.info("Enter Age as: " + str(age))
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchInchargees(self):
        """
        fetch the list of inchargees
        :return: self.fetchInchargees
        """
        try:
            self.clickElement(self.InchargeeDropDown, "xpath")

            if self.isDisplayed("Mann ki baat", "text"):
                self.InchargeeList.append("Mann ki baat")
                self.log.info("Mann ki baat inchargee available, adding to list!")
            if self.isDisplayed("WhatsApp Group", "text"):
                self.InchargeeList.append("WhatsApp Group")
                self.log.info("WhatsApp Group inchargee available, adding to list!")
            if self.isDisplayed("Booth Program", "text"):
                self.InchargeeList.append("Booth Program")
                self.log.info("Booth Program inchargee available, adding to list!")

            self.clickElement(self.CloseButton)

            return self.InchargeeList
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseInchargee(self, inchargee):
        """
        choose inchargee of karyakarta
        :param inchargee: inchargee name
        :return: self.chooseInchargee
        """
        try:
            self.clickElement(self.InchargeeDropDown, "xpath")
            self.clickElement(inchargee, "text")
            self.log.info("Selected inchargee as: " + inchargee)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def clickSecondaryInformationButton(self):
        """
        click on fill secondary information button
        :return: self.clickSecondaryInformationButton
        """
        try:
            self.clickElement(self.SecondaryInfo, "id")
            self.log.info("Starting input secondary information")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputBloodGroup(self, bloodgroup):
        """
        input karyakarta 's blood group
        :param bloodgroup: blood group
        :return: self.inputBloodGroup
        """
        try:
            self.sendKeys(bloodgroup, self.BloodGroup, "xpath")
            self.log.info("Input Blood Group as: " + bloodgroup)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseGender(self, gender):
        """
        choose karyakarta gender
        :param gender: gender
        :return: self.chooseGender
        """
        try:
            self.clickElement(gender, "text")
            self.log.info("Selected gender as: " + gender)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputWhatsappNumber(self, whatsappnumber):
        """
        input whatsapp number of karyakarta
        :param whatsappnumber: whatsapp number
        :return: self.inputWhatsappNumber
        """
        try:
            self.sendKeys(whatsappnumber, self.WhatsAppNumber, "xpath")
            self.log.info("Entered Whatsapp Number as: " + whatsappnumber)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputSTDCode(self, stdcode):
        """
        input Karyakarta STD Code
        :param stdcode: STD Code
        :return: self.inputSTDCode
        """
        try:
            self.sendKeys(stdcode, self.STDCode, "xpath")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputLandline(self, landline):
        """
        input landline number of karyakarta
        :param landline: landline number
        :return: self.inputLandline
        """
        try:
            self.sendKeys(landline, self.LandlineNumber, "xpath")
            self.log.info("Entered Landline number as: " + landline)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchCategory(self):
        """
        fetch category list
        :return: self.fetchCategory
        :return: CategoryList
        """
        try:
            self.clickElement(self.CategoryDropDown, "xpath")

            if self.isDisplayed("GEN", "text"):
                self.CategoryList.append("GEN")
            if self.isDisplayed("OBC", "text"):
                self.CategoryList.append("OBC")
            if self.isDisplayed("SC", "text"):
                self.CategoryList.append("SC")
            if self.isDisplayed("ST", "text"):
                self.CategoryList.append("ST")
            if self.isDisplayed("Minority", "text"):
                self.CategoryList.append("Minority")
            if self.isDisplayed("Gen", "text"):
                self.CategoryList.append("Gen")
            if self.isDisplayed("Others", "text"):
                self.CategoryList.append("Others")

            self.clickElement(self.CloseButton, "id")

            return self.CategoryList
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseCategory(self, category):
        """
        choose category of karyakarta
        :param category: category
        :return: self.chooseCategory
        """
        try:
            self.clickElement(self.CategoryDropDown, "xpath")
            self.clickElement(category, "text")
            self.log.info("Selected a new Category as: " + category)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchCaste(self, CurrentCategory):
        """
        fetch caste list based on category selected
        :param CurrentCategory: category selected in previous method
        :return: self.fetchCaste
        :return: CasteList
        """
        try:
            if CurrentCategory == 'GEN':
                self.clickElement(self.CasteDropDown, "xpath")
                self.keyCode(4)
                if self.isDisplayed("Brahmin", "text"):
                    self.CasteList.append("Brahmin")
                if self.isDisplayed("Jaat", "text"):
                    self.CasteList.append("Jaat")
                if self.isDisplayed("vaish ", "text"):
                    self.CasteList.append("vaish ")
                if self.isDisplayed("Multani", "text"):
                    self.CasteList.append("Multani")
                if self.isDisplayed("Punjabi", "text"):
                    self.CasteList.append("Punjabi")
                if self.isDisplayed("RAJPUT", "text"):
                    self.CasteList.append("RAJPUT")
            elif CurrentCategory == 'OBC':
                self.clickElement(self.CasteDropDown, "xpath")
                self.keyCode(4)
                if self.isDisplayed("gurjar", "text"):
                    self.CasteList.append("gurjar")
                if self.isDisplayed("MANDAL", "text"):
                    self.CasteList.append("MANDAL")
                if self.isDisplayed("RAJPUT", "text"):
                    self.CasteList.append("RAJPUT")
            elif CurrentCategory == 'SC':
                self.clickElement(self.CasteDropDown, "xpath")
                self.keyCode(4)
                if self.isDisplayed("Valmiki", "text"):
                    self.CasteList.append("Valmiki")
            elif CurrentCategory == 'ST':
                self.clickElement(self.CasteDropDown, "xpath")
                if self.isDisplayed("No data available", "text"):
                    self.log.info("No Castes present in ST Category")
                    self.keyCode(4)
            elif CurrentCategory == 'Minority':
                self.clickElement(self.CasteDropDown, "xpath")
                if self.isDisplayed("No data available", "text"):
                    self.keyCode(4)
                    self.log.info("No Castes present in Minority Category")
            elif CurrentCategory == 'Gen':
                self.clickElement(self.CasteDropDown, "xpath")
                if self.isDisplayed("No data available", "text"):
                    self.keyCode(4)
                    self.log.info("No Castes present in Gen Category")
            elif CurrentCategory == 'Others':
                self.clickElement(self.CasteDropDown, "xpath")
                if self.isDisplayed("No data available", "text"):
                    self.keyCode(4)
                    self.log.info("No Castes present in Others Category")

            self.clickElement(self.CloseButton, "id")

            return self.CasteList
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseCaste(self, caste):
        """
        choose karyakarta 's caste
        :param caste: caste
        :return: self.chooseCaste
        """
        try:
            self.clickElement(self.CasteDropDown, "xpath")
            self.clickElement(caste, "text")
            self.log.info("Selected a new Caste as: " + caste)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def addNewCaste(self, newcaste):
        """
        add a new caste
        :param newcaste: new caste name
        :return: self.addNewCaste
        """
        try:
            self.clickElement(self.AddCaste, "id")
            self.sendKeys(newcaste, self.NewCaste, "id")
            self.clickElement(self.Submit, "id")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputEmail(self, email):
        """
        input email of karyakarta
        :param email: email
        :return: self.inputEmail
        """
        try:
            self.sendKeys(email, self.Email, "xpath")
            self.log.info("Entered Email: " + email)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseDOB(self, dob, action):
        """
        choose date of birth for karyakarta
        :param dob: DOB
        :param action: ok or cancel
        :return: self.chooseDOB
        """
        try:
            # 01 August 2005 (format for Accessibility id)
            self.clickElement(self.DOB, "xpath")
            self.clickElement(dob, "accessibility id")
            if action == "OK":
                self.clickElement(self.OK, "id")
                self.log.info("Set the DOB as: " + dob)
            else:
                self.clickElement(self.Cancel, "id")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputAddress(self, address):
        """
        input karyakarta address
        :param address: address of karyakarta
        :return: self.inputAddress
        """
        try:
            self.sendKeys(address, self.FullAddress, "xpath")
            self.log.info("Entered address as: " + address)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputVillageWard(self, villageward):
        """
        input village/ward name for karyakarta
        :param villageward: Village/Ward name
        :return: self.inputVillageWard
        """
        try:
            self.sendKeys(villageward, self.VillageWard, "xpath")
            self.log.info("Entered Village and Ward name: " + villageward)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputTehsil(self, tehsil):
        """
        input tehsil name of karyakarta
        :param tehsil: tehsil
        :return: self.inputTehsil
        """
        try:
            self.sendKeys(tehsil, self.Tehsil, "xpath")
            self.log.info("Entered Tehsil Name: " + tehsil)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseDistrict(self, district):
        """
        Choose District of Karyakarta
        :param district: district
        :return: self.chooseDistrict
        """
        try:
            self.clickElement(self.Disrict, "xpath")
            self.clickElement(district, "text")
            self.log.info("Selected district as: " + district)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputPinCode(self, pincode):
        """
        input Pin Code of karyakarta
        :param pincode: Pin Code
        :return: self.inputPinCode
        """
        try:
            self.sendKeys(pincode, self.PinCode, "xpath")
            self.log.info("Entered Pin Code as: " + pincode)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchEducationList(self):
        """
        fetch Education list
        :return: self.fetchEducationList
        :return: EducationList
        """
        try:
            self.clickElement(self.EducationDropDown, "xpath")

            if self.isDisplayed("Less than 10th", "text"):
                self.EducationList.append("Less than 10th")
            if self.isDisplayed("10th Pass", "text"):
                self.EducationList.append("10th Pass")
            if self.isDisplayed("12th Pass", "text"):
                self.EducationList.append("12th Pass")
            if self.isDisplayed("Graduate", "text"):
                self.EducationList.append("Graduate")
            if self.isDisplayed("Post Graduate", "text"):
                self.EducationList.append("Post Graduate")
            if self.isDisplayed("Diploma/ITI", "text"):
                self.EducationList.append("Diploma/ITI")
            if self.isDisplayed("PhD and above", "text"):
                self.EducationList.append("PhD and above")

            self.clickElement(self.CloseButton, "id")

            return self.EducationList
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseEducation(self, education):
        """
        Choose education of karyakarta
        :param education: education
        :return: self.chooseEducation
        """
        try:
            self.clickElement(self.EducationDropDown, "xpath")
            self.clickElement(education, "text")
            self.log.info("Selected Education Type as: " + education)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseProfession(self, profession):
        """
        Choose Profession of karyakarta
        :param profession: Profession
        :return: self.chooseProfession
        """
        try:
            self.clickElement(self.ProfessionDropDown, "xpath")
            self.clickElement(profession, "text")
            self.log.info("Selected a new profession: " + profession)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def checkBikeStatus(self, action):
        """
        check if karyakarta owns a bike
        :param action: yes or no
        :return: self.checkBikeStatus
        """
        try:
            self.clickElement(action, "text")
            self.log.info("Bike status set to: " + action)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def checkCarStatus(self, action):
        """
        check if karyakarta owns a car
        :param action: yes or no
        :return: self.checkCarStatus
        """
        try:
            self.clickElement(action, "text")
            self.log.info("Car status set to: " + action)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseVidhanSabha(self, vidhansabha):
        """
        Choose Vidhan Sabha where Karyakarta Votes
        :param vidhansabha: Vidhan Sabha Name
        :return: self.chooseVidhanSabha
        """
        try:
            self.clickElement(self.VidhanSabhaDropDown, "xpath")
            self.clickElement(vidhansabha, "text")
            self.log.info("Selected the Vidhan Sabha as: " + vidhansabha)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputBooth(self, booth):
        """
        Input booth name where karyakarta votes
        :param booth: booth number
        :return: self.inputBooth
        """
        try:
            self.sendKeys(booth, self.Booth, "xpath")
            self.log.info("Entered Booth as: " + booth)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputVoterID(self, voterid):
        """
        Input Voter ID number of karyakarta
        :param voterid: Voter ID Number
        :return: self.inputVoterID
        """
        try:
            self.sendKeys(voterid, self.VoterIDInput, "xpath")
            self.log.info("Entered Voter ID number as: " + voterid)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def uploadVoterID(self):
        """
        upload voter id from device
        :return: self.uploadVoterID
        """
        try:
            self.pushFile(self.VoterIDDestination, self.JohnDoeVoterID)
            self.clickElement("Upload File", "text")
            self.clickElement("Gallery", "text")
            self.clickElement(self.AllowButton, "id")
            self.clickElement("JohnDoeVoterID.jpg", "text")
            self.log.info("Uploaded Voter ID: JohnDoeVoterID.jpg")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputAadhaar(self, aadhaar):
        """
        input Aadhaar number of karyakarta
        :param aadhaar: Aadhaar number
        :return: self.inputAadhaar
        """
        try:
            self.sendKeys(aadhaar, self.AadhaarInput, "xpath")
            self.log.info("Entered Aadhaar Number as: " + aadhaar)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def uploadAadhaar(self):
        """
        upload aadhaar card of karyakarta from device
        :return: self.uploadAadhaar
        """
        try:
            self.pushFile(self.AadhaarDestination, self.JohnDoeAadhaar)
            self.clickElement("Upload File", "text")
            self.clickElement("Gallery", "text")
            self.clickElement(self.AllowButton, "id")
            self.clickElement("JohnDoeAadhaar.jpg", "text")
            self.log.info("Uploaded Aadhaar file: JohnDoeAadhaar.jpg")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputPannaNumber(self, pannanumber):
        """
        Input Panna Number where karyakarta votes
        :param pannanumber: Panna number
        :return: self.inputPannaNumber
        """
        try:
            self.sendKeys(pannanumber, self.PannaNumber, "xpath")
            self.log.info("Entered Panna Number: " + pannanumber)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputRationCardNumber(self, rationnumber):
        """
        Ration number of Karyakarta
        :param rationnumber: Ration Number
        :return: self.inputRationCardNumber
        """
        try:
            self.sendKeys(rationnumber, self.RationCardNumberInput, "xpath")
            self.log.info("Entered Ration card Number: " + rationnumber)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def uploadRationCard(self):
        """
        Upload karyakarta 's ration card from device
        :return: self.uploadRationCard
        """
        try:
            self.pushFile(self.RationCardDestination, self.JohnDoeRationCard)
            self.clickElement("Upload File", "text")
            self.clickElement("Gallery", "text")
            self.clickElement(self.AllowButton, "id")
            self.clickElement("JohnDoeRationCard.jpg", "text")
            self.log.info("Uploaded Ration Card: JohnDoeRationCard.jpg")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputFacebook(self, facebook):
        """
        Input Facebook ID link of karyakarta
        :param facebook: Facebook link
        :return: self.inputFacebook
        """
        try:
            self.sendKeys(facebook, "www.fb.com/username", "text")
            self.log.info("Entered Facebook Username: " + facebook)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputTwitter(self, twitter):
        """
        Input Twitter profile link of karyakarta
        :param twitter: Twitter link
        :return: self.inputTwitter
        """
        try:
            self.sendKeys(twitter, "www.twitter.com/username", "text")
            self.log.info("Entered Twitter username: " + twitter)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputInstagram(self, instagram):
        """
        Input Instagram profile link of karyakarta
        :param instagram: Instagram link
        :return: self.inputInstagram
        """
        try:
            self.sendKeys(instagram, "www.instagram.com/username", "text")
            self.log.info("Entered Instagram Username: " + instagram)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputLinkedin(self, linkedin):
        """
        Input Linkedin profile link of karyakarta
        :param linkedin: Linkedin link
        :return: self.inputLinkedin
        """
        try:
            self.sendKeys(linkedin, "www.linkedin.com/username", "text")
            self.log.info("Entered Linkedin username: " + linkedin)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchSalutation(self):
        """
        Fetch Salutation list
        :return: Salutation List
        """
        try:
            self.clickElement(self.SalutationDropDown, "xpath")

            if self.isDisplayed("Shri", "text"):
                self.SalutationList.append("Shri")
            if self.isDisplayed("Smt", "text"):
                self.SalutationList.append("Smt")
            if self.isDisplayed("Sadhvi", "text"):
                self.SalutationList.append("Sadhvi")
            if self.isDisplayed("Kumari", "text"):
                self.SalutationList.append("Kumari")
            if self.isDisplayed("SD", "text"):
                self.SalutationList.append("SD")

            self.clickElement(self.CloseButton, "id")

            return self.SalutationList
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseSalutation(self, salutation):
        """
        Choose Karyakarta 's salutation
        :param salutation: Salutation
        :return: self.chooseSalutation
        """
        try:
            self.clickElement(self.SalutationDropDown, "xpath")
            self.clickElement(salutation, "text")
            self.log.info("Entered Salution as: " + salutation)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputSubCaste(self, subcaste):
        """
        Input Sub Caste of Karyakarta
        :param subcaste: Sub Caste
        :return: self.inputSubCaste
        """
        try:
            self.sendKeys(subcaste, self.SubCaste, "xpath")
            self.log.info("Entered SubCaste: " + subcaste)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputQualification(self, qualification):
        """
        Input Karyakarta 's qualifications
        :param qualification: qualifications
        :return: self.inputQualification
        """
        try:
            self.sendKeys(qualification, self.Qualification, "xpath")
            self.log.info("Entered Qualification as: " + qualification)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def fetchReligionList(self):
        """
        fetch list of religions present
        :return: Religion List
        """
        try:
            self.clickElement(self.ReligionDropDown, "xpath")

            if self.isDisplayed("Hinduism", "text"):
                self.ReligionList.append("Hinduism")
            if self.isDisplayed("Islam", "text"):
                self.ReligionList.append("Islam")
            if self.isDisplayed("Christianity", "text"):
                self.ReligionList.append("Christianity")
            if self.isDisplayed("Buddhism", "text"):
                self.ReligionList.append("Buddhism")
            if self.isDisplayed("Jainism", "text"):
                self.ReligionList.append("Jainism")
            if self.isDisplayed("Sikhism", "text"):
                self.ReligionList.append("Sikhism")
            if self.isDisplayed("Zoroastrians", "text"):
                self.ReligionList.append("Zoroastrians")

            self.clickElement(self.CloseButton, "id")

            return self.ReligionList
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def chooseReligion(self, religion):
        """
        Choose Religion of Karyakarta
        :param religion: Religion
        :return: self.chooseReligion
        """
        try:
            self.clickElement(self.ReligionDropDown, "xpath")
            self.clickElement(religion, "text")
            self.log.info("Selected Religion as: " + religion)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def inputActiveMemberID(self, memberid):
        """
        Input Active member ID of karyakarta
        :param memberid: Member ID
        :return: self.inputActiveMemberID
        """
        try:
            self.sendKeys(memberid, self.ActiveMember, "xpath")
            self.log.info("Entered Active Member ID as: " + memberid)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def choosePartyZila(self, partyzila):
        """
        choose Party's Zila
        :param partyzila: Party Zila
        :return: self.choosePartyZila
        """
        try:
            self.clickElement(self.PartyZila, "xpath")
            self.clickElement(partyzila, "text")
            self.log.info("Selected Party Zilla as: " + partyzila)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def choosePartyMandal(self, partymandal):
        """
        Choose Party's mandal
        :param partymandal: Party's mandal
        :return: self.choosePartyMandal
        """
        try:
            self.clickElement(self.PartyMandal, "xpath")
            self.clickElement(partymandal, "text")
            self.log.info("Selected Party Mandal as: " + partymandal)
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    def clickPreviewandSubmit(self):
        """
        CLick on Preview & Submit button
        :return: self.clickPreviewandSubmit
        """
        try:
            self.clickElement(self.PreviewButton, "id")
            self.log.info("Clicked on Preview Button")
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
            traceback.print_exception(type(e), e, e.__traceback__)
