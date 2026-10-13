from playwright.sync_api import Page
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.orders_menu_button = page.get_by_role("link", name="Orders")
        self.manage_orders_button = page.get_by_text("Manage Order")

    def click_orders_menu(self):
        self.orders_menu_button.click()
    def click_manage_orders(self):
        with self.page.expect_popup() as popup_info:
            self.manage_orders_button.click()
        return popup_info.value

