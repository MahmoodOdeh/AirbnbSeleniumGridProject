from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class AirbnbSearchPage(BasePage):
    DATE_TO_CHECKIN = (By.XPATH, "//div[@data-testid='calendar-day-03/18/2024']")
    DATE_TO_CHECKOUT = (By.XPATH, "//div[@data-testid='calendar-day-03/31/2024']")

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.date_to_check_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.DATE_TO_CHECKIN))
        self.date_to_check_out = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.DATE_TO_CHECKOUT))

    def press_date_to_check_in(self):
        self.date_to_check_in.click()

    def press_date_to_check_out(self):
        self.date_to_check_out.click()
