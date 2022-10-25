from selenium.webdriver.common.by import By

class LoginPageBurger:

    email_field = (By.XPATH, "(//*[contains(@class,'text input__textfield')])[1]")

    password_field = (By.XPATH, "(//*[contains(@class,'text input__textfield')])[2]")

    sign_in_button = (By.XPATH, "//*[contains(@class,'button_button__33qZ0')]")

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()