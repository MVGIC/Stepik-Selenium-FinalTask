from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_TO_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "div > h1")
    PRODUCT_PRICE = (By.TAG_NAME, "div > .price_color:nth-child(2)")
    PRODUCT_ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    CART_PRICE_AFTER_ADDING_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
