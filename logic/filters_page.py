from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from infra.base_page import BasePage


class AirbnbFilterPage(BasePage):
    MINIMUM_FIELD = (By.XPATH,
                     "//label[@class='it3ysxn atm_mk_h2mmj6 atm_am_kb7nvz atm_l8_idpfg4 dir dir-ltr' and @for='price_filter_min']")

    MAXIMUM_FIELD = (By.XPATH,
                     "//label[@class='it3ysxn atm_mk_h2mmj6 atm_am_kb7nvz atm_l8_idpfg4 dir dir-ltr' and @for='price_filter_max']")

    SHOW_BUTTON = (By.XPATH, "//a[contains(@class, 'l1ovpqvx') and contains(text(), 'נכסים')]")
    CLEAR_BUTTON = (By.XPATH, "//button[contains(@class, 'l1ovpqvx') and contains(text(), 'ניקוי הכול')]")
    MAX_PRICE_BUTTON = (By.XPATH, "//button[contains(@class, 'l1ovpqvx') and @aria-label='מחיר מקסימלי']")
    NAVIGATE_BAR = (By.XPATH, "//div[contains(@class, 'h18af07h')]/button[@aria-label='מחיר מינימלי']")

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.min_field = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.MINIMUM_FIELD))
        self.max_field = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.MAXIMUM_FIELD))
        self.show_button = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.SHOW_BUTTON))
        self.clear_button = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable(self.CLEAR_BUTTON))
        self.navigate_bar = WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable(self.NAVIGATE_BAR))

    def minimum_fill(self, text):
        actions = ActionChains(self._driver)
        actions.double_click(self.min_field).perform()
        self.min_field.send_keys(text)
        self.minimum_price_value = text

    def maximum_fill(self, text):
        actions = ActionChains(self._driver)
        actions.click(self.max_field).click(self.max_field).click(self.max_field).perform()
        self.max_field.send_keys(text)
        self.maximum_price_value = text

    def press_show_btn(self):
        self.show_button.click()

    def press_clear_btn(self):
        self.clear_button.click()

    def navigate_press(self):
        ActionChains(self._driver).click_and_hold(self.navigate_bar).move_by_offset(200, 0).release().perform()

    def get_minimum_price_value(self):
        return self.minimum_price_value

    def get_maximum_price_value(self):
        return self.maximum_price_value
