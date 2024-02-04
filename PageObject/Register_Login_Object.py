from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Registration_page_objects:

    ########## Register Page Objects #########
    HomePage_dropDownOpen = (By.XPATH,"//span[normalize-space()='My Account']")
    Register_page_Validation = (By.XPATH,"//p[contains(text(),'If you already have an account with us, please log')]")
    click_on_registration = (By.XPATH,"//a[normalize-space()='Register']")
    First_Name_InputXpath = (By.XPATH,"//input[@id='input-firstname']")
    Last_Name_InputXpath = (By.XPATH,"//input[@id='input-lastname']")
    Email_Id_InputXpath = (By.XPATH,"//input[@id='input-email']")
    Password_InputXpath = (By.XPATH,"//input[@id='input-password']")
    Yes_Radio_Button_ClickXpath = (By.XPATH,"//input[@id='input-newsletter-yes']")
    ClickOn_PrivacyP_ButtonXpath = (By.XPATH,"//input[@name='agree']")
    ClickOn_Register_Button_Xpath = (By.XPATH,"//button[normalize-space()='Continue']")
    AfterRegisterPage_Validation_Check = (By.XPATH,"")

    ######## Login Page Objects #######
    click_on_login = (By.XPATH,"//a[normalize-space()='Login']")
    validation_login_page = (By.XPATH,"//h2[normalize-space()='Returning Customer']")
    login_email_id = (By.XPATH,"//input[@id='input-email']")
    login_password = (By.XPATH,"//input[@id='input-password']")
    login_buttonClick = (By.XPATH,"//button[normalize-space()='Login']")
    AfterLogin_Validation_Check = (By.XPATH,"//h2[normalize-space()='My Account']")

    HomePageClick = (By.XPATH,"")

    def __init__(self,driver):
        self.driver = driver

############## ------------ Registration Page -----------###########
    def Click_Dropdown(self):
        self.driver.find_element(*Registration_page_objects.HomePage_dropDownOpen).click()

    def Click_Register_Account(self):
        self.driver.find_element(*Registration_page_objects.click_on_registration).click()

    def User_First_Name(self,first_name):
        self.driver.find_element(*Registration_page_objects.First_Name_InputXpath).send_keys(first_name)

    def Enter_Last_Name(self,last_name):
        self.driver.find_element(*Registration_page_objects.Last_Name_InputXpath).send_keys(last_name)

    def Enter_E_Mail(self,Email):
        self.driver.find_element(*Registration_page_objects.Email_Id_InputXpath).send_keys(Email)

    def Enter_Password(self,Pass):
        self.driver.find_element(*Registration_page_objects.Password_InputXpath).send_keys(Pass)

    def click_yes_radio(self):
        self.driver.find_element(*Registration_page_objects.Yes_Radio_Button_ClickXpath).click()

    def click_privacy_policy_button(self):
        self.driver.find_element(*Registration_page_objects.ClickOn_PrivacyP_ButtonXpath).click()

    def click_registerButton(self):
        self.driver.find_element(*Registration_page_objects.ClickOn_Register_Button_Xpath).click()

    def RegisterPage_Validation(self):
        try:
            self.driver.find_element(*Registration_page_objects.Register_page_Validation)
            return 'Registration Page Open'

        except:
            return 'Registration Page Not Open'

    ############------ Login Page ---------##############

    def click_login(self):
        self.driver.find_element(*Registration_page_objects.click_on_login).click()

    def loginpage_validation(self):
        try:
            self.driver.find_element(*Registration_page_objects.validation_login_page)
            return 'login page Open pass'
        except:
            return 'login page Not Open fail'

    def login_page_Email(self,email):
        self.driver.find_element(*Registration_page_objects.login_email_id).send_keys(email)

    def login_pass(self,password):
        self.driver.find_element(*Registration_page_objects.login_password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Registration_page_objects.login_buttonClick).click()

    def afterloginClick_validationPage(self):
        try:
            self.driver.find_element(*Registration_page_objects.AfterLogin_Validation_Check)
            return 'Login Pass'

        except:
            return 'Login Fail'

    def GoHomePage(self):
        self.driver.find_element(*Registration_page_objects.HomePageClick).click()






















