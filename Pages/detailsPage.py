

class DetailsPage():

    def __init__(self, driver):
        self.driver = driver
        self.book_div_id = "front-list-recentlySoldProducts"
        self.book_card_class_name = "book-list-wrapper"
        self.read_book_xpath ="//*[@id='js--add-to-cart-button']"


    def view_details(self):
        self.driver.find_element_by_class_name(self.book_card_class_name).click()
        '''
        #for list of book, which one to pick
        self.book_div =self.driver.find_element_by_id(self.book_div_id)
        self.book_list = self.book_div.find_element_by_class_name(self.book_card_class_name)
        print(len(self.book_list))
        self.book_details = self.book_list[book_no].click()
        '''

    def click_read_book_btn(self):
        self.driver.find_element_by_xpath(self.read_book_xpath).click()