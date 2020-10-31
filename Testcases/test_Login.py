import pytest
from selenium import webdriver

from Pages.sysuserdetails import UserDetails
from Testcases.BaseTest import BaseTest
from CommonUtil.readconfigfile import Readconfig
from Pages.Loginpage import Login
from webdriver_manager.chrome import ChromeDriverManager


class Test_001(BaseTest):

    baseurl = Readconfig.getAppurl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()


    def test_TC01(self):
        self.driver.get(self.baseurl)
        self.lpage = Login(self.driver)
        self.lpage.do_login(self.username,self.password)

    def test_TC02(self):
        self.syspage = UserDetails(self.driver)
        self.syspage.userdetail()