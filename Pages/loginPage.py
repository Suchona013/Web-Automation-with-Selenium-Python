

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_name = "j_username"
        self.password_textbox_name = "j_password"
        #self.login_btn_xpath = "/html/body/div[3]/div/section/div[2]/div[2]/form/button"
        self.login_btn_xpath = "// *[ @ id = 'loginForm'] / button"
        #self.login_btn_class = "btn btn-block"
        self.error_msg_for_wrong_email_pass_xpath = "//*[@id='js--message']/p"
        self.error_msg_empty_email = "//*[@id='loginForm']/div[1]/div/p"
        self.error_msg_empty_pass = "//*[@id='loginForm']/div[2]/div/p"
        self.close_wrong_email_pass_msg = "//*[@id='js--message']/button/span"



    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_name).clear()
        self.driver.find_element_by_id(self.email_textbox_name).send_keys(email)


    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_name).clear()
        self.driver.find_element_by_id(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()
        #self.driver.find_element_by_class_name(self.login_btn_class).click()

    def error_msg_email(self):
        self.msg1 = self.driver.find_element_by_xpath(self.error_msg_empty_email)
        return self.msg1
        #self.email_msg = self.msg1.text
        #print(self.email_msg)

    def error_msg_pass(self):
        self.msg2 = self.driver.find_element_by_xpath(self.error_msg_empty_pass)
        return self.msg2
        #self.msg = self.driver.find_element_by_xpath(self.error_msg_for_wrong_email_pass_xpath)
        #self.error_msg_for_wrong_email_pass = self.msg.text

    def error_msg(self):
        self.msg = self.driver.find_element_by_xpath(self.error_msg_for_wrong_email_pass_xpath)
        return self.msg

    def close_error_msg(self):
        self.driver.find_element_by_xpath(self.close_wrong_email_pass_msg).click()
