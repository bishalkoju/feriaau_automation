from playwright.sync_api import Page
import os

class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")

    def navigate(self, path: str = ""):
        self.page.goto(f"{self.base_url}{path}")
