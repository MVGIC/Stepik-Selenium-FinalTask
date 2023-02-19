from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_button_to_add(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_TO_ADD)

    def add_to_basket_item(self):
        button_to_add = self.browser.find_element(*ProductPageLocators.BUTTON_TO_ADD)
        button_to_add.click()

    def should_be_product_name(self):
        assert "The shellcoder's handbook" in self.browser.find_element(
            *ProductPageLocators.ADD_MESSAGE).text, "The name is not equal"

    def should_be_price(self):
        assert "9,99 £" in self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text, "The price is not equal"
