from selenium.webdriver.common.by import By


class BasePageLocators(object):
    login_link = (By.CSS_SELECTOR, "#login_link")
    text_on_login_page = (By.CSS_SELECTOR, "#login_form h2")


class LoginPageLocators(object):
    email_register = (By.CSS_SELECTOR, "#id_registration-email")
    email_login = (By.CSS_SELECTOR, "#id_login-username")
    password_register = (By.CSS_SELECTOR, "#id_registration-password1")
    password_register_confirm = (By.CSS_SELECTOR, "#id_registration-password2")
    password_login = (By.CSS_SELECTOR, "#id_login-password")
    register_button = (By.CSS_SELECTOR, "#register_form .btn")
    login_button = (By.CSS_SELECTOR, "#login_form .btn")
    registration_successful_msg = (By.CSS_SELECTOR, ".alertinner.wicon")
    login_successful_msg = (By.CSS_SELECTOR, ".alertinner.wicon")


class ProductPageLocators(object):
    product_name_in_success_msg = (By.CSS_SELECTOR, ".alertinner strong")
    product_price_in_success_msg = (By.CSS_SELECTOR, ".alertinner p strong")
    add_to_basket_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    basket_button = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn")
    text_on_basket_page = (By.CSS_SELECTOR, ".page-header h1")
    success_message = (By.CSS_SELECTOR, '#messages .alert .alertinner')