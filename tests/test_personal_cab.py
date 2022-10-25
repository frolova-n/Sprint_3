from locators import Authorization
from locators import BurgerLocators
from methods import LoginPageBurger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_personal_cab_1(driver):
    driver.find_element(*Authorization.personal_cab_button).click()
    assert driver.find_element(*Authorization.entry_button).text == 'Войти'
    driver.quit()


def test_personal_cab_2(driver):
    driver.find_element(*Authorization.login_button).click()
    login_page = LoginPageBurger(driver)
    login_page.login("nataliafrolova3678@ya.ru", "000018")
    driver.find_element(*Authorization.personal_cab_button).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(Authorization.orders_history_button))
    assert driver.find_element(*Authorization.orders_history_button).text == 'История заказов'
    driver.quit()


def test_constructor(driver):
    driver.find_element(*Authorization.login_button).click()
    login_page = LoginPageBurger(driver)
    login_page.login("nataliafrolova3678@ya.ru", "000018")
    driver.find_element(*Authorization.personal_cab_button).click()
    driver.find_element(*BurgerLocators.constructor_button).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(BurgerLocators.assemble_a_burger_header))
    assert driver.find_element(*BurgerLocators.assemble_a_burger_header).text == 'Соберите бургер'
    driver.quit()


def test_logo_Burger(driver):
    driver.find_element(*Authorization.login_button).click()
    login_page = LoginPageBurger(driver)
    login_page.login("nataliafrolova3678@ya.ru", "000018")
    driver.find_element(*Authorization.personal_cab_button).click()
    driver.find_element(*BurgerLocators.logo_Burger).click()
    assert driver.find_element(*Authorization.make_an_order_button).text == 'Оформить заказ'
    driver.quit()


def test_logout_personal_cab(driver):
    driver.find_element(*Authorization.login_button).click()
    login_page = LoginPageBurger(driver)
    login_page.login("nataliafrolova3678@ya.ru", "000018")
    driver.find_element(*Authorization.personal_cab_button).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Authorization.logout_button))
    driver.find_element(*Authorization.logout_button).click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located(Authorization.entry_button))
    assert driver.find_element(*Authorization.entry_button).text == 'Войти'
    driver.quit()