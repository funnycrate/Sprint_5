from locators import StellarBurgersLocators
from helpers import Helpers
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_registration_correct_password(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()
        driver.find_element(*StellarBurgersLocators.REG_LNK).click()

        driver.find_element(*StellarBurgersLocators.REG_NAME_FLD).send_keys(Data.NAME)
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_FLD).send_keys(Helpers.generate_email())
        driver.find_element(*StellarBurgersLocators.REG_PASS_FLD).send_keys(Helpers.generate_password())

        driver.find_element(*StellarBurgersLocators.REG_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.REG_LNK))

        assert driver.find_element(*StellarBurgersLocators.ACC_BTN).is_displayed()

    def test_registration_incorrect_password(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()
        driver.find_element(*StellarBurgersLocators.REG_LNK).click()

        driver.find_element(*StellarBurgersLocators.REG_NAME_FLD).send_keys(Data.NAME)
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_FLD).send_keys(Helpers.generate_email())
        driver.find_element(*StellarBurgersLocators.REG_PASS_FLD).send_keys(Data.PASSWORD_ERROR)
        driver.find_element(*StellarBurgersLocators.REG_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PASS_ERR_MSG))

        assert driver.find_element(*StellarBurgersLocators.PASS_ERR_MSG).is_displayed()
