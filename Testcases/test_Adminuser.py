import pytest
from selenium import webdriver

from Pages.sysuserdetails import UserDetails
from Testcases.BaseTest import BaseTest
from CommonUtil.readconfigfile import Readconfig, Read2
from Pages.Loginpage import Login
from webdriver_manager.chrome import ChromeDriverManager


class Test_001(BaseTest):

    baseurl = Read2.getappurl()

    def test_TC02(self):
        self.driver.get(self.baseurl)
        self.syspage = UserDetails(self.driver)
        self.syspage.userdetail()
