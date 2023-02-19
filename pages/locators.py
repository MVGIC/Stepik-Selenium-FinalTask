from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_TO_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
