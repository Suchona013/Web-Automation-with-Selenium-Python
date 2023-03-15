from Pages.loginPage import LoginPage
import time

#driver = webdriver.Chrome(executable_path="D:\\driver\\version-98\\chromedriver.exe")


class LoginTestcase():

    def __init__(self, driver):
        self.driver = driver

    def login_valid(self):

        self.login = LoginPage(self.driver)

        self.login.enter_email("wohiy63254@asoflex.com")
        self.login.enter_password("Ab1234567")

        self.login.click_login()
        time.sleep(5)
    def login_invalid_case1(self):

        self.login = LoginPage(self.driver)
        self.login.enter_email("")
        self.login.enter_password("")
        self.login.click_login()
        time.sleep(2)
        self.email_msg = self.login.error_msg_email()
        #self.tt= self.driver.find_element_by_xpath("//*[@id='loginForm']/div[1]/div/p")
        #print(self.email_msg.text)
        assert(self.email_msg.text == "This field is required!")
        print("True", "This field is required!", "message is showing for empty email field")

        self.password_msg = self.login.error_msg_pass()
        assert (self.password_msg.text == "This field is required!")
        print("True", "This field is required!", "message is showing for empty password field")

    def login_invalid_case2(self):

        self.login = LoginPage(self.driver)
        self.login.enter_email("abc@gmail.com")
        self.login.enter_password("abcabc")
        #time.sleep(7)
        self.login.click_login()
        time.sleep(2)
        #self.tt= self.driver.find_element_by_xpath("//*[@id='js--message']/p")
        #print("nnnnn", self.tt.text)
        self.error_msg = self.login.error_msg()
        assert (self.error_msg.text == "Wrong email/phone or password")
        print("True", "Wrong email/phone or password", "message is showing for incorrect email, password")
        self.login.close_error_msg()