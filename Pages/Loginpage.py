from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class Login(BasePage):

    Username = (By.ID,"txtUsername")
    Password = (By.ID,"txtPassword")
    Loginbtn = (By.ID,"btnLogin")
    welcomeicon = (By.ID,"welcome")


    def __init__(self,driver):
        super().__init__(driver)

    def enterusername(self,username):
        self.do_sendkeys(self.Username,username)

    def enterpassword(self,password):
        self.do_sendkeys(self.Password, password)

    def loginlink(self):
        self.do_clicks(self.Loginbtn)

    def isdis(self):
        icon = self.is_eledisplayed(self.welcomeicon)
        return icon

    def do_login(self,username,password):
        self.do_sendkeys(self.Username,username)
        self.do_sendkeys(self.Password,password)
        self.do_clicks(self.Loginbtn)