import pytest
from pages.catalog_page import CatalogPage


link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.mark.xfail
def test_user_can_register(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.write_email_register()
    page.write_password_register()
    page.confirm_password_register()
    page.click_on_register()
    page.registration_successful()


@pytest.mark.xfail
def test_user_cant_register_with_incorrect_email(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.write_incorrect_email_register()
    page.write_password_register()
    page.confirm_password_register()
    page.click_on_register()
    page.registration_unsuccessful()


@pytest.mark.login
def test_user_can_login(browser):
    page = CatalogPage(browser, link)
    page.open()
    page.write_email_login()
    page.write_password_login()
    page.click_on_login()
    page.login_successful()
