import time

from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class AirbnbWhoPage(BasePage):
    PLUS_FOR_ADULT = (By.XPATH,
                      "//button[contains(@class, 'bv4zwx4') and contains(@aria-label, 'העלאת הערך') and contains(@data-testid, 'stepper-adults-increase-button')]")
    MINUS_FOR_ADULT = (By.XPATH,
                       "//button[contains(@class, 'bv4zwx4') and contains(@aria-label, 'הורדת הערך') and contains(@data-testid, 'stepper-adults-decrease-button')]")

    PLUS_FOR_CHILDREN = (By.XPATH,
                         "//button[contains(@class, 'bv4zwx4') and contains(@aria-label, 'העלאת הערך') and contains(@data-testid, 'stepper-children-increase-button')]")

    MENUS_FOR_CHILDREN = (By.XPATH,
                          "//button[contains(@class, 'bv4zwx4') and contains(@aria-label, 'הורדת הערך') and contains(@data-testid, 'stepper-children-decrease-button')]")

    PLUS_FOR_BABIES = (By.XPATH,
                       "//button[contains(@class, 'bv4zwx4') and contains(@aria-label, 'העלאת הערך') and contains(@data-testid, 'stepper-infants-increase-button')]")

    MENUS_FOR_BABIES = (By.XPATH,
                        "//button[contains(@class, 'bv4zwx4') and contains(@aria-label, 'הורדת הערך') and contains(@data-testid, 'stepper-infants-decrease-button')]")

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.plus_for_adult = self._driver.find_element(*self.PLUS_FOR_ADULT)
        self.menus_for_adult = self._driver.find_element(*self.MINUS_FOR_ADULT)
        self.plus_for_children = self._driver.find_element(*self.PLUS_FOR_CHILDREN)
        self.menus_for_children = self._driver.find_element(*self.MENUS_FOR_CHILDREN)
        self.plus_for_babies = self._driver.find_element(*self.PLUS_FOR_BABIES)
        self.menus_for_babies = self._driver.find_element(*self.MENUS_FOR_BABIES)

    def press_plus_for_adult(self):
        self.plus_for_adult.click()

    def press_menus_for_adult(self):
        self.menus_for_adult.click()

    def press_plus_for_children(self):
        self.plus_for_children.click()

    def press_menus_for_children(self):
        self.menus_for_children.click()

    def press_plus_for_babies(self):
        self.plus_for_babies.click()

    def press_menus_for_babies(self):
        self.menus_for_babies.click()

    def select_generation_flow(self):
        self.press_menus_for_adult()
        self.press_menus_for_adult()
        self.press_menus_for_adult()
        self.press_plus_for_babies()
        self.press_menus_for_babies()
        self.press_plus_for_children()
        self.press_plus_for_children()
        self.press_menus_for_children()
