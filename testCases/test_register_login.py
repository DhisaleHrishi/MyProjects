from Utilities.Readproperties_Config_Data_Registration import registration_readConfig
from PageObject.Register_Login_Object import Registration_page_objects
from Utilities.Logger import Login_Class
import time

class Test_Registration_login:

    Home_PageUrl = registration_readConfig.Home_PageUrl()
    First_Name = registration_readConfig.FirstName()
    Last_Name = registration_readConfig.LastName()
    Email_Id = registration_readConfig.E_MailID()
    Password = registration_readConfig.Pass_word()

    log = Login_Class.log_generator()

    def test_register_user(self,setup):
        self.driver = setup
        self.log.info(f"{self.Home_PageUrl}  Home Page Url Open")
        self.driver.get(self.Home_PageUrl)
        self.Rp = Registration_page_objects(self.driver)
        self.log.info("Checking Home Page Title Validation ")

        if self.driver.title == "Your Store":
            self.log.info("Home Page Open")
            self.driver.save_screenshot("C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Screenshot\\HomePage_Open.png")
            self.log.info("Click On DropDown ")
            self.Rp.Click_Dropdown()
            self.log.info("Clicking On Register Account DropDwon Option")
            self.Rp.Click_Register_Account()
            time.sleep(2)
            self.log.info("Validation Of Registration Page Open Or Not!")
            if self.Rp.RegisterPage_Validation() == "Registration Page Open":
                self.log.info("Register Account Page Open")
                self.driver.save_screenshot("C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Screenshot\\Registration_PageOpen.png")
                self.log.info("Maximize_window")
                self.driver.maximize_window()
                self.log.info("Enter Input Value First Name")
                self.Rp.User_First_Name(self.First_Name)
                self.log.info("Enter Input Value Last Name")
                self.Rp.Enter_Last_Name(self.Last_Name)
                self.log.info("Enter Input Value Email ID")
                self.Rp.Enter_E_Mail(self.Email_Id)
                self.log.info("Enter Input Value Password")
                self.Rp.Enter_Password(self.Password)
                self.log.info("Clicking On Yes Radio Button")
                time.sleep(2)
                self.Rp.click_yes_radio()
                self.log.info("Click On prvacy policy check box ")
                self.Rp.click_privacy_policy_button()
                self.log.info("Click On Register Account Button !")
                self.Rp.click_registerButton()
                assert True

            else:
                self.driver.save_screenshot("C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Screenshot\\RegistrationPage_Open.png")
                self.log.info("Register Page Not Open!")
                assert False
        else:
            self.driver.save_screenshot("C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Screenshot\\HomePageNot_Open.png")
            self.log.info("Home Page Not Open!")
            self.driver.close()

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.Home_PageUrl)
        self.log.info(f"{self.Home_PageUrl} Home Page URL")
        self.lp = Registration_page_objects(self.driver)

        self.lp.Click_Dropdown()
        self.log.info("Click DropDown Option...")
        self.lp.click_login()
        self.log.info("Click On Login Option")
        if self.lp.loginpage_validation() == "login page Open pass":
            self .driver.save_screenshot("C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Screenshot\\loginPageOpenpass.png")

            self.lp.login_page_Email(self.Email_Id)
            self.log.info(f"{self.Email_Id} This Email ID Entering" )
            self.lp.login_pass(self.Password)
            self.log.info(f"{self.Password} This Password Entering ")
            self.lp.click_login_button()
            self.log.info("Click On Login Button ")
            time.sleep(2)

            if self.lp.afterloginClick_validationPage() == "Login Pass":
                self.log.info("Login Page Validation ")
                self.driver.save_screenshot(
                    "C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Screenshot\\login_pass.png")
                assert True
            else:
                self.driver.save_screenshot(
                    "C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Screenshot\\login_fail.png")

                assert False
            self.lp.GoHomePage()
            self.log.info("Home Page Icon Click To Shopping!")

        else:
            self .driver.save_screenshot("C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Screenshot\\loginPageOpenfail.png")
            assert False






































