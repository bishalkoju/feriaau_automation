from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.vendor_login_page import LoginPage
from pages.vendor_dashboard_page import DashboardPage
from pages.vendor_pos_page import VendorPosPage
import os 
email = os.getenv('VENDOR_EMAIL')
password = os.getenv('VENDOR_PASSWORD')
baseurl = os.getenv('BASE_URL')

def test_manage_order(page: Page):
    base_page = BasePage(page)
    home_page = HomePage(page)
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    # Navigate to the base URL
    base_page.navigate()
    # Click on the "Vendor Portal" button to go to the login page
    home_page.click_vendor_login()
    # Perform login with valid credentials
    login_page.login(email,password)
    expect(page).to_have_url(f"{baseurl}/admin/dashboard")

    dashboard_page.click_orders_menu()
    expect(page.get_by_text("Order List")).to_be_visible()
    pos_tab = dashboard_page.click_manage_orders()
    # Assert the new tab has opened and its page is loaded
    expect(pos_tab).to_have_url(
        f"{baseurl}/admin/pos?fullscreen=true"
    )

    # Assert the POS page has loaded by checking for a specific element
    pos_page = VendorPosPage(pos_tab)

    pos_page.assert_pos_page_visible()
    pos_page.click_pos_table()
    # add 3 items to the order

    pos_page.click_add_item()
    for _ in range(3):
        pos_page.click_plus_item()
    # Click on the "Cart Summary" button to view the order summary
    pos_page.click_cart_summary()
    
