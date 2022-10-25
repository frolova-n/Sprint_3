from selenium.webdriver.common.by import By


class BurgerLocators:

    sauses_button = (By.XPATH, '//*[@class="text text_type_main-default" and text() = "Соусы"]')

    buns_button = (By.XPATH, '//*[@class="text text_type_main-default" and text() = "Булки"]')

    stuffing_button = (By.XPATH, '//*[@class="text text_type_main-default" and text() = "Начинки"]')

    fluorescent_bun_button = (By.XPATH, "//*[text()= 'Флюоресцентная булка R2-D3']")

    meat_of_immortal_clams_button = (By.XPATH, "//*[text()= 'Мясо бессмертных моллюсков Protostomia']")

    spicyx_sause_button = (By.XPATH, "//*[text()= 'Соус Spicy-X']")

    constructor_button = (By.XPATH, "(//*[@class='AppHeader_header__link__3D_hX'])[1]")

    assemble_a_burger_header = (By.XPATH, "//*[contains(@class, 'mb-5 mt-10')]")

    logo_Burger = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']")

class Authorization:

    registration_form_button = (By.XPATH, "(//*[@class='Auth_link__1fOlj'])[1]")

    name_registration_form_field = (By.XPATH, "(//*[contains(@class,'text input__textfield')])[1]")

    email_registration_form_field = (By.XPATH, "(//*[contains(@class,'text input__textfield')])[2]")

    password_registration_form_field = (By.XPATH, "(//*[contains(@class,'text input__textfield')])[3]")

    register_button = (By.XPATH, "//*[contains(@class,'button_button__33qZ0')]")

    wrong_password_header = (By.XPATH, "//*[@class='input__error text_type_main-default']")

    login_registration_form_button = (By.XPATH, "//*[@class='Auth_link__1fOlj']")

    login_button = (By.XPATH, "//*[contains(@class,'button_button__33qZ0')]")

    email_field = (By.XPATH, "(//*[contains(@class,'text input__textfield')])[1]")

    password_field = (By.XPATH, "(//*[contains(@class,'text input__textfield')])[2]")

    entry_button = (By.XPATH, "//*[contains(@class,'button_button__33qZ0') and text() = 'Войти']")

    recovery_password_button = (By.XPATH, "(//*[@class='Auth_link__1fOlj'])[2]")

    make_an_order_button = (By.XPATH, "//*[contains(@class,'button_button__33qZ0 button_button_type_primary__1O7Bx') and text() = 'Оформить заказ']")

    personal_cab_button = (By.XPATH, "//*[@class='AppHeader_header__nav__g5hnF']/a[@class='AppHeader_header__link__3D_hX']")

    orders_history_button = (By.XPATH, "//*[contains(@class,'Account_link__2ETsJ') and text() = 'История заказов']")

    logout_button = (By.XPATH, "//*[contains(@class,'Account_button__14Yp3')]")