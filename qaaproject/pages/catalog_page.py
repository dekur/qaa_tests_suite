from .base_page import BasePage
from .locators import ProductPageLocators


class CatalogPage(BasePage):

        def click_on_add_to_basket_button(self):
            button1 = self.browser.find_element(*ProductPageLocators.add_to_basket_button)
            button1.click()

        def check_success_message(self):
            element = self.browser.find_element(*ProductPageLocators.product_name_in_success_msg)
            assert element.text == "Coders at Work"
            element = self.browser.find_element(*ProductPageLocators.product_price_in_success_msg)
            assert element.text == "19,99 £"

        def should_not_be_success_message(self):
            assert self.is_not_element_present(*ProductPageLocators.success_message)

        def should_be_success_message(self):
            assert self.browser.find_element(*ProductPageLocators.success_message)

        def click_on_basket_button(self):
            button1 = self.browser.find_element(*ProductPageLocators.basket_button)
            button1.click()

        def should_be_on_basket_page(self):
            element = self.browser.find_element(*ProductPageLocators.text_on_basket_page)
            assert element.text == "Корзина"



