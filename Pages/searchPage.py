

class SearchPage():

    def __init__(self, driver):
        self.driver = driver
        self.search_box_id = "js--search"
        self.search_btn_xpath = "//*[@id='js--main-header']/div/div/div[2]/div/form/div/div/button"
        self.book_author_name_class = "book-author"


    def enter_search_text(self, text):
        self.driver.find_element_by_id(self.search_box_id ).clear()
        self.driver.find_element_by_id(self.search_box_id ).send_keys(text)

    def click_search_btn(self):
        self.driver.find_element_by_xpath(self.search_btn_xpath).click()

    def book_author_name(self):
        author_name = self.driver.find_element_by_class_name(self.book_author_name_class)
        return author_name