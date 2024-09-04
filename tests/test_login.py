from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:

    def test_login_for_button_login_in_main_page(self, driver):
        driver.find_element(*StellarBurgersLocators.LOGIN_BTN_MAIN).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PLACE_ORDER_BTN))

        assert driver.find_element(*StellarBurgersLocators.PLACE_ORDER_BTN).is_displayed()

    def test_login_for_account_button(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PLACE_ORDER_BTN))

        assert driver.find_element(*StellarBurgersLocators.PLACE_ORDER_BTN).is_displayed()

    def test_login_in_registration_window(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()
        driver.find_element(*StellarBurgersLocators.REG_LNK).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_LNK_REG).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PLACE_ORDER_BTN))

        assert driver.find_element(*StellarBurgersLocators.PLACE_ORDER_BTN).is_displayed()

    def test_login_in_forgot_password_window(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()
        driver.find_element(*StellarBurgersLocators.FORGOT_PASS_LNK).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_LNK_FORGOT).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.PLACE_ORDER_BTN))

        assert driver.find_element(*StellarBurgersLocators.PLACE_ORDER_BTN).is_displayed()
