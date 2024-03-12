import time

from selenium.webdriver.common.by import By

from AirbnbSeleniumGridProject.infra.base_page import BasePage


class AirbnbBasePage(BasePage):
    FILTER_BUTTON = (By.XPATH, "//button[@data-testid='category-bar-filter-button']")
    WORD_BUTTON = (By.XPATH, "//button[@aria-label='בחירת שפה ומטבע']")
    CHECK_IN_BUTTON = (By.XPATH, "//div[contains(@class, 'lmukvak') and contains(text(), \"צ'ק-אין\")]")
    CHECK_OUT_BUTTON = (By.XPATH, "//div[contains(@class, 'lmukvak') and contains(text(), \"צ'ק-אאוט\")]")
    WHO_BUTTON = (By.XPATH, "//div[contains(@class, 'lmukvak') and contains(text(), \"מי\")]")
    SEARCH_BUTTON = (By.CLASS_NAME, "bhtghtc")
    LEFT_ARROW = (By.XPATH, "//button[@aria-label='דף הקטגוריות הבא']")
    CATEGORY_TYPE = (By.XPATH, "//*[@id='categoryScroller']/div/div/div/div[3]/div/div/div/div/label[9]/div/span")

    def __init__(self, driver):
        super().__init__(driver)
        self.filter_button = self._driver.find_element(*self.FILTER_BUTTON)
        self.word_button = self._driver.find_element(*self.WORD_BUTTON)
        self.check_in_button = self._driver.find_element(*self.CHECK_IN_BUTTON)
        self.check_out_button = self._driver.find_element(*self.CHECK_OUT_BUTTON)
        self.who_button = self._driver.find_element(*self.WHO_BUTTON)
        self.search_button = self._driver.find_element(*self.SEARCH_BUTTON)
        self.left_arrow = self._driver.find_element(*self.LEFT_ARROW)
        self.category_type = self._driver.find_element(*self.CATEGORY_TYPE)

    def press_filter_btn(self):
        try:
            self.filter_button.click()
            time.sleep(2)
        except AttributeError:
            print("Filter button not found or is not clickable.")

    def press_word_btn(self):
        try:
            self.word_button.click()
            time.sleep(2)
        except AttributeError:
            print("word button not found or is not clickable.")

    def press_check_in_btn(self):
        try:
            self.check_in_button.click()
            time.sleep(2)
        except AttributeError:
            print("checkin button not found or is not clickable.")

    def press_check_out_btn(self):
        try:
            self.check_out_button.click()
            time.sleep(2)
        except AttributeError:
            print("checkout button not found or is not clickable.")

    def press_who_btn(self):
        try:
            self.who_button.click()
            time.sleep(2)
        except AttributeError:
            print("checkout button not found or is not clickable.")

    def press_search_btn(self):
        try:
            self.search_button.click()
            time.sleep(2)
        except AttributeError:
            print("search button not found or is not clickable.")

    def press_arrow_left(self):
        try:
            self.left_arrow.click()
            time.sleep(2)
            print("arrow")
        except AttributeError:
            print("Filter button not found or is not clickable.")

    def press_category_type(self):
        try:
            self.category_type.click()
            time.sleep(2)
            print("category")
        except AttributeError:
            print("Filter button not found or is not clickable.")

    def choose_house_from_category_flow(self):
        self.press_arrow_left()
        time.sleep(3)
        self.press_category_type()
        time.sleep(3)

