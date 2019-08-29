from page_objects.base_elements.base_page import BasePage
from page_objects.base_elements.base_page_elements import InputElement, BaseElement


class LoginInput(InputElement):
    selector = '#user_email'


class PasswordInput(InputElement):
    selector = '#user_password'


class LoginButton(BaseElement):
    selector = '#new_user > div:nth-child(9) > input'


class LoginPage(BasePage):
    login_input = LoginInput()
    password_input = PasswordInput()
    login_button = LoginButton()

    def login(self, login, password):
        self.login_input = login
        self.password_input = password
        self.login_button.click()
