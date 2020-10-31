from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_clicks(self,by_locator):
        ele = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        ele.click()

    def do_sendkeys(self,by_locator,text_to_enter):
        ele = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        ele.send_keys(text_to_enter)

    def is_eledisplayed(self,by_locator):
        isdis = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return isdis.is_displayed()

    def mousehover(self,by_locator1,by_locator2,by_locator3):
        actions = ActionChains(self.driver)
        actions.move_to_element(by_locator1).move_to_element(by_locator2).move_to_element(by_locator3).click().perform()

