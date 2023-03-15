import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

from Pages.loginPage import LoginPage
from TestCases.loginTestCases import LoginTestcase
from TestCases.searchTestCase import SearchTestcase
from TestCases.detailsTestCase import DetailsPageTestcase
import unittest





class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        url ="https://www.rokomari.com/book"
        cls.driver.get(url)
        time.sleep(5)
        cls.driver.maximize_window()


    def test_LoginTestcase(self):
        #self.driver.get("https://www.rokomari.com/book")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='js--main-header']/div/div/div[3]/div/div[2]/a").click() #sign in button
        time.sleep(2)
        #self.login1 = LoginPage(self.driver)

        self.login = LoginTestcase(self.driver)
        self.login.login_invalid_case1()
        time.sleep(2)
        #self.login.login_invalid_case2()
        time.sleep(3)

        self.login.login_valid()


        #self.driver.find_element_by_xpath("//*[@id='js--search']").click()

    def test_SearchTestcase(self):
        self.search = SearchTestcase(self.driver)
        self.search.search_text(self.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")





