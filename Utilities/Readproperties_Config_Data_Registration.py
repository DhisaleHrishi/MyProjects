import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\GURUDEV\\PycharmProjects\\OpenCart_Project\\Configuration\\config.ini")


class registration_readConfig:

    @staticmethod
    def Home_PageUrl():
        R_Url = config.get('registration_login info','Home_page_Url')
        return R_Url

    @staticmethod
    def FirstName():
        U_Name = config.get('registration_login info','First_Name')
        return U_Name
    @staticmethod
    def LastName():
        L_Name = config.get('registration_login info','Last_Name')
        return L_Name
    @staticmethod
    def E_MailID():
        E_mail = config.get('registration_login info','Email_Id')
        return E_mail
    @staticmethod
    def Pass_word():
        P_word = config.get('registration_login info','Password')
        return P_word

