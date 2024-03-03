from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.base_page import BasePage


class AirbnbWorldPage(BasePage):
    WORLD_BUTTON = (By.XPATH,
                    "//a[contains(@class, '_1ejyijmy') and div[contains(text(), 'English')] and div[contains(text(), 'United States')]][1]")

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.language_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.WORLD_BUTTON))

    def press_language_btn(self):
        try:
            self.language_button.click()
            print("english")
        except AttributeError:
            print("English language button not found or is not clickable.")

    def get_page_title(self):
        return self._driver.title
