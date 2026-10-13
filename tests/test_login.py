from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.vendor_login_page import LoginPage
import os 
email = os.getenv('VENDOR_EMAIL')
password = os.getenv('VENDOR_PASSWORD')
baseurl = os.getenv('BASE_URL')
def test_successful_login(page: Page):
    base_page = BasePage(page)
    home_page = HomePage(page)
    login_page = LoginPage(page)
   # Navigate to the base URL 
    base_page.navigate()
    # Click on the "Vendor Portal" button to go to the login page
    home_page.click_vendor_login()
    # Perform login with valid credentials
    login_page.login(email,password)
    expect(page).to_have_url(f"{baseurl}/admin/dashboard")