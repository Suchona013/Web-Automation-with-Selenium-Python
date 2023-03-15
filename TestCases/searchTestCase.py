

from Pages.searchPage import SearchPage
from TestCases.detailsTestCase import DetailsPageTestcase
import time
from selenium.webdriver import ActionChains


class SearchTestcase():

    def __init__(self, driver):
        self.driver = driver
        self.search = SearchPage(driver)
        self.details = DetailsPageTestcase(driver)

    def search_text(self, driver):
        self.search.enter_search_text("মেঘ বলেছে যাব যাব")
        self.search.click_search_btn()
        self.author_name = self.search.book_author_name()
        assert (self.author_name.text == "হুমায়ূন আহমেদ")
        time.sleep(2)
        self.details.click_view_details_page()
        time.sleep(5)
        self.details.read_book()




