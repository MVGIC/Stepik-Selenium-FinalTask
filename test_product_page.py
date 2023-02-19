from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_to_add()
    page.add_to_basket_item()
    page.solve_quiz_and_get_code()
    page.should_be_product_name()
    page.should_be_price()
