from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogout:

    def test_logout_from_account(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()

        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGOUT_BTN))

        driver.find_element(*StellarBurgersLocators.LOGOUT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.REG_LNK))

        assert driver.find_element(*StellarBurgersLocators.REG_LNK).is_displayed()
