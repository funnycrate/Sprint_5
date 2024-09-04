from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestFromPcToConstructor():

    def test_from_pc_to_constructor(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()

        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()
        driver.find_element(*StellarBurgersLocators.CONSTR_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BREAD_LIST))

        assert driver.find_element(*StellarBurgersLocators.BREAD_LIST).is_displayed()

    def test_from_pc_to_constructor_use_logo(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()

        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()
        driver.find_element(*StellarBurgersLocators.LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BREAD_LIST))

        assert driver.find_element(*StellarBurgersLocators.BREAD_LIST).is_displayed()