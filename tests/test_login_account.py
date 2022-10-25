from locators import Authorization
from methods import LoginPageBurger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_account(driver):
    driver.find_element(*Authorization.login_button).click()
    login_page = LoginPageBurger(driver)
    login_page.login("nataliafrolova3678@ya.ru", "000018")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Authorization.make_an_order_button))
    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'
    driver.quit()


def test_login_personal_cab(driver):
    driver.find_element(*Authorization.personal_cab_button).click()
    login_page = LoginPageBurger(driver)
    login_page.login("nataliafrolova3678@ya.ru", "000018")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Authorization.make_an_order_button))
    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'
    driver.quit()


def test_login_reg_form(driver):
    driver.find_element(*Authorization.personal_cab_button).click()
    driver.find_element(*Authorization.registration_form_button).click()
    driver.find_element(*Authorization.login_registration_form_button).click()
    login_page = LoginPageBurger(driver)
    login_page.login("nataliafrolova3678@ya.ru", "000018")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Authorization.make_an_order_button))
    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'
    driver.quit()


def test_login_password_recovery_button(driver):
    driver.find_element(*Authorization.login_button).click()
    driver.find_element(*Authorization.recovery_password_button).click()
    driver.find_element(*Authorization.login_registration_form_button).click()
    login_page = LoginPageBurger(driver)
    login_page.login("nataliafrolova3678@ya.ru", "000018")
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Authorization.make_an_order_button))
    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'
    driver.quit()