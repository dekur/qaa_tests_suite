import pytest
from pages.catalog_page import CatalogPage
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.product
def test_user_can_add_product_to_basket(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()


@pytest.mark.product
def test_user_can_see_success_message(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.check_success_message()


@pytest.mark.product
def test_correct_success_message(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.check_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.should_not_be_success_message()


@pytest.mark.other
def test_user_should_see_login_or_register_link_on_product_page(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.should_be_login_or_register_link()


@pytest.mark.other
def test_user_can_go_to_login_page_from_product_page(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.should_be_login_or_register_link()
    page.click_on_login_or_register()
    page.should_be_on_login_page()


@pytest.mark.other
def test_user_can_go_to_basket(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.click_on_basket_button()
    page.should_be_on_basket_page()