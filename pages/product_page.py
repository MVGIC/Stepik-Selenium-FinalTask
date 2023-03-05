from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_to_add(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_TO_ADD)

    def add_to_basket_product(self):
        button_to_add = self.browser.find_element(*ProductPageLocators.BUTTON_TO_ADD)
        button_to_add.click()

    def find_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def find_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_product_name_in_basket(self, product_name):
        assert product_name == self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE).text, "The name is not equal"

    def should_be_product_price_in_basket(self, product_price):
        assert product_price == self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE_AFTER_ADDING_MESSAGE).text, "The price is not equal"
