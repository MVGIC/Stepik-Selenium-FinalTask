from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_TO_CHECK_BASKET = (By.CSS_SELECTOR, ".btn-group > .btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    PRODUCT_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, ".row:nth-of-type(1) .col-sm-6")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_INPUT_REGISTRATION_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_TO_REGISTER = (By.NAME, "registration_submit")


class ProductPageLocators():
    BUTTON_TO_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "div > h1")
    PRODUCT_PRICE = (By.TAG_NAME, "div > .price_color:nth-child(2)")
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_PRICE_AFTER_ADDING_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
