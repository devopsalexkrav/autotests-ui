from pages.base_page import BasePage
from playwright.sync_api import Page
from playwright.sync_api import expect

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header_title = page.get_by_test_id("dashboard-toolbar-title-text")

    def check_header_title(self):
        expect(self.header_title).to_be_visible()
        expect(self.header_title).to_have_text("Dashboard")