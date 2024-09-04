from locators import StellarBurgersLocators
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructor:

    def test_constructor_sauces(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_LIST))

        sauces_list = driver.find_element(*StellarBurgersLocators.SAUCES_LIST)
        driver.execute_script("arguments[0].scrollIntoView();", sauces_list)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.GALACTIC_SAUCE_ICON))
        driver.find_element(*StellarBurgersLocators.GALACTIC_SAUCE_ICON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.GALACTIC_SAUCE_CAL))

        assert driver.find_element(*StellarBurgersLocators.GALACTIC_SAUCE_CAL).is_displayed()


    def test_constructor_toppings(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_LIST))

        toppings_list = driver.find_element(*StellarBurgersLocators.TOPPINGS_LIST)
        driver.execute_script("arguments[0].scrollIntoView();", toppings_list)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BEAF_METEOR_ICON))
        driver.find_element(*StellarBurgersLocators.BEAF_METEOR_ICON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BEAF_METEOR_CAL))

        assert driver.find_element(*StellarBurgersLocators.BEAF_METEOR_CAL).is_displayed()

    def test_constructor_bread(self, driver):
        driver.find_element(*StellarBurgersLocators.ACC_BTN).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_FLD).send_keys(Data.LOGIN)
        driver.find_element(*StellarBurgersLocators.LOGIN_PASS_FLD).send_keys(Data.PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.SAUCES_LIST))

        toppings_list = driver.find_element(*StellarBurgersLocators.TOPPINGS_LIST)
        driver.execute_script("arguments[0].scrollIntoView();", toppings_list)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.BEAF_METEOR_ICON))

        bread_list = driver.find_element(*StellarBurgersLocators.BREAD_LIST)
        driver.execute_script("arguments[0].scrollIntoView();", bread_list)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.CRATER_BREAD_ICON))
        driver.find_element(*StellarBurgersLocators.CRATER_BREAD_ICON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(StellarBurgersLocators.CRATER_BREAD_CAL))

        assert driver.find_element(*StellarBurgersLocators.CRATER_BREAD_CAL).is_displayed()
