from .pages.product_page import ProductPage
import pytest

promos = [("?promo=offer0"),
         ("?promo=offer1"),
         ("?promo=offer2"),
         ("?promo=offer3"),
         ("?promo=offer4"),
         ("?promo=offer5"),
         ("?promo=offer6"),
         ("?promo=offer7"),
         ("?promo=offer8"),
         ("?promo=offer9")]



@pytest.mark.parametrize('promo', promos)
def test_guest_can_add_product_to_basket(browser, promo):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{}".format(promo)
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message()
    page.should_be_product_title_in_meessage()
    page.should_be_message_cart_price()
    #page.should_be_cart_price()
