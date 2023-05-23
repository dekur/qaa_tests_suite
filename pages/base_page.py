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
        button1 = self.browser.find_element(*BasePageLocators.login_link)
        button1.click()

    def should_be_on_login_page(self):
        element = self.browser.find_element(*BasePageLocators.text_on_login_page)
        assert element.text == "Войти"

    def write_email_register(self):
        input1 = self.browser.find_element(*LoginPageLocators.email_register)
        input1.send_keys("test12757354341334@gmail.com")

    def write_incorrect_email_register(self):
        input1 = self.browser.find_element(*LoginPageLocators.email_register)
        input1.send_keys("test12757354341334")

    def write_password_register(self):
        input1 = self.browser.find_element(*LoginPageLocators.password_register)
        input1.send_keys("gggg12357354163425")

    def confirm_password_register(self):
        input1 = self.browser.find_element(*LoginPageLocators.password_register_confirm)
        input1.send_keys("gggg12357354163425")

    def click_on_register(self):
        button1 = self.browser.find_element(*LoginPageLocators.register_button)
        button1.click()

    def registration_successful(self):
        element = self.browser.find_element(*LoginPageLocators.registration_successful_msg)
        assert element.text == "Спасибо за регистрацию!"

    def registration_unsuccessful(self):
        element = self.browser.find_element(*LoginPageLocators.registration_successful_msg)
        assert element.text == "Спасибо за регистрацию!"

    def write_email_login(self):
        input1 = self.browser.find_element(*LoginPageLocators.email_login)
        input1.send_keys("test12757354341334@gmail.com")

    def write_password_login(self):
        input1 = self.browser.find_element(*LoginPageLocators.password_login)
        input1.send_keys("gggg12357354163425")

    def click_on_login(self):
        button1 = self.browser.find_element(*LoginPageLocators.login_button)
        button1.click()

    def login_successful(self):
        element = self.browser.find_element(*LoginPageLocators.login_successful_msg)
        assert element.text == "Рады видеть вас снова"
