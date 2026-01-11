import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page

@pytest.fixture
def registration_page(chromium_page: Page):
    return RegistrationPage(chromium_page)

@pytest.fixture
def dashboard_page(chromium_page: Page):
    return DashboardPage(chromium_page)