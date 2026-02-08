from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    def click_continue(self):
        self.click(LoginLocators.CONTINUE,2)

    def enter_username(self, username):
        self.type(LoginLocators.USERNAME, username)

    def enter_password(self, password):
        self.type(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON, 2)

    def get_dashboard_header(self):
        return self.driver.find_element(*LoginLocators.DASHBOARD_HEADER).text
