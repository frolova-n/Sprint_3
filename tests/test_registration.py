from locators import Authorization
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_registration(driver):
    driver.find_element(*Authorization.login_button).click()
    driver.find_element(*Authorization.registration_form_button).click()
    driver.find_element(*Authorization.name_registration_form_field).send_keys("Наталья")
    driver.find_element(*Authorization.email_registration_form_field).send_keys("nataliafrolova3678@ya.ru")
    driver.find_element(*Authorization.password_registration_form_field).send_keys("000018")
    driver.find_element(*Authorization.register_button).click()
    WebDriverWait(driver, 3).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()


def test_wrong_password(driver):
    driver.find_element(*Authorization.login_button).click()
    driver.find_element(*Authorization.registration_form_button).click()
    driver.find_element(*Authorization.name_registration_form_field).send_keys("Наталья")
    driver.find_element(*Authorization.email_registration_form_field).send_keys("nataliafrolov32435@ya.ru")
    driver.find_element(*Authorization.password_registration_form_field).send_keys("00001")
    driver.find_element(*Authorization.register_button).click()
    WebDriverWait(driver, 3)
    assert driver.find_element(*Authorization.wrong_password_header).text == 'Некорректный пароль'
    driver.quit()