
from Pages.detailsPage import DetailsPage
from selenium.webdriver import ActionChains

class DetailsPageTestcase():


    def __init__(self, driver):
        self.driver = driver
        self.details = DetailsPage(driver)

    def click_view_details_page(self):
        self.details.view_details()
        ##for list of book, which one to pick
        #self.details.view_details(0)
        '''
        self.move_to_btn= self.details.view_details_btn()
        self.actions = ActionChains(self.driver)
        #self.details.click_view_details_btn()
        self.actions.move_to_element(self.move_to_btn).click().perform()
        '''

    def read_book(self):
        self.details.click_read_book_btn()
