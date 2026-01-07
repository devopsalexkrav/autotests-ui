from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    registration_button = page.get_by_test_id("registration-page-registration-button")

    expect(registration_button).to_be_visible()
    expect(registration_button).to_be_disabled()

    expect(email_input).to_be_visible()
    email_input.fill("user.name@gmail.com")

    expect(username_input).to_be_visible()
    username_input.fill("username")

    expect(password_input).to_be_visible()
    password_input.fill("password")

    expect(registration_button).to_be_enabled()