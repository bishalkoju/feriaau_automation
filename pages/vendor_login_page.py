from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Define locators here 
        self.email_input = page.get_by_placeholder('Enter your email address')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator(':text("PROCEED")')

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        