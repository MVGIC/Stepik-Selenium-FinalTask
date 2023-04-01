from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_REGISTRATION)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_REGISTRATION)
        password_input.send_keys(password)
        password_input_repeat = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_REGISTRATION_REPEAT)
        password_input_repeat.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.BUTTON_TO_REGISTER)
        registration_button.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
