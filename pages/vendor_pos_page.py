from unicodedata import name

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
class VendorPosPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
#        locators for POS page elements
        self.assert_text = page.get_by_role("heading", name="Tables")
        self.search_input = page.get_by_role("textbox", name="Search table, guest, or zone…")
        self.first_table_button = page.locator("div.grid.grid-cols-2.gap-3.pt-4.sm\:grid-cols-3.md\:grid-cols-4.lg\:grid-cols-5.xl\:grid-cols-6").locator("div").nth(0)
        # add item locator
        self.add_item_button = page.locator("button").filter(has_text="Add").first
        self.plus_item_button = page.locator('button:has(svg.lucide-plus)').nth(0)
        #cart summary button locator
        self.cart_summary_button = page.get_by_role("button", name="View order summary")
    
        #self.pos_menu_button = page.get_by_role("link", name="POS")
        #self.manage_pos_button = page.get_by_text("Manage POS")

    def assert_pos_page_visible(self):
        expect(self.assert_text).to_be_visible()
    def click_pos_table(self):
        self.first_table_button.click()
    def click_add_item(self):
        self.add_item_button.click()
    def click_plus_item(self):
        self.plus_item_button.click()
    def click_cart_summary(self):
        self.cart_summary_button.click()
 