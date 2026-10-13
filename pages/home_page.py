from pages.base_page import BasePage
from playwright.sync_api import Page
class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.vendor_login_button = page.get_by_role("link", name="Vendor Portal")
        # self.customer_login_button = page.locator("#customer-login-button")
        # self.register_button = page.locator("#register-button")

    def click_vendor_login(self):
        self.vendor_login_button.click()


# Backward compatibility alias for typo
HomaPage = HomePage
