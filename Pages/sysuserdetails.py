from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class UserDetails(BasePage):

    mousehoverAdmin = (By.XPATH,"//b[contains(text(),'Admin')]")
    mousehoverMnt = (By.XPATH,"//a[@id='menu_admin_UserManagement']")
    clickuser = (By.XPATH,"//a[@id='menu_admin_viewSystemUsers']")


    def __init__(self,driver):
        super().__init__(driver)

    def userdetail(self):
        self.mousehover(self.mousehoverAdmin,self.mousehoverMnt,self.clickuser)