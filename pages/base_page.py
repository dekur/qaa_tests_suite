from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators
from .locators import LoginPageLocators


class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        self.browser.find_element(how, what)

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_or_register_link(self):
        assert self.browser.find_element(*BasePageLocators.login_link)

    def click_on_login_or_register(self):
        login_or_register_button = self.browser.find_element(*BasePageLocators.login_link)
        login_or_register_button.click()

    def should_be_on_login_page(self):
        element = self.browser.find_element(*BasePageLocators.text_on_login_page)
        assert element.text == "Войти"

    def write_email_register(self):
        email_register_input = self.browser.find_element(*LoginPageLocators.email_register)
        email_register_input.send_keys("test12757354341334@gmail.com")

    def write_incorrect_email_register(self):
        email_register_input = self.browser.find_element(*LoginPageLocators.email_register)
        email_register_input.send_keys("test12757354341334")

    def write_password_register(self):
        password_register_input = self.browser.find_element(*LoginPageLocators.password_register)
        password_register_input.send_keys("gggg12357354163425")

    def confirm_password_register(self):
        confirm_password_register_input = self.browser.find_element(*LoginPageLocators.password_register_confirm)
        confirm_password_register_input.send_keys("gggg12357354163425")

    def click_on_register(self):
        register_button = self.browser.find_element(*LoginPageLocators.register_button)
        register_button.click()

    def registration_successful(self):
        element = self.browser.find_element(*LoginPageLocators.registration_successful_msg)
        assert element.text == "Спасибо за регистрацию!"

    def registration_unsuccessful(self):
        element = self.browser.find_element(*LoginPageLocators.registration_successful_msg)
        assert element.text == "Спасибо за регистрацию!"

    def write_email_login(self):
        email_login_input = self.browser.find_element(*LoginPageLocators.email_login)
        email_login_input.send_keys("test12757354341334@gmail.com")

    def write_password_login(self):
        password_login_input = self.browser.find_element(*LoginPageLocators.password_login)
        password_login_input.send_keys("gggg12357354163425")

    def click_on_login(self):
        login_button = self.browser.find_element(*LoginPageLocators.login_button)
        login_button.click()

    def login_successful(self):
        element = self.browser.find_element(*LoginPageLocators.login_successful_msg)
        assert element.text == "Рады видеть вас снова"
