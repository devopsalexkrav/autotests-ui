from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    registration_button = page.get_by_test_id("registration-page-registration-button")

    expect(email_input).to_be_visible()
    email_input.fill("user.name@gmail.com")

    expect(username_input).to_be_visible()
    username_input.fill("username")

    expect(password_input).to_be_visible()
    password_input.fill("password")

    expect(registration_button).to_be_visible()
    registration_button.click()

    context.storage_state(path="auth_state.json")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth_state.json")
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    header_courses = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(header_courses).to_be_visible()
    expect(header_courses).to_have_text("Courses")
    

    label_no_results = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(label_no_results).to_be_visible()
    expect(label_no_results).to_have_text("There is no results")

    icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_be_visible()

    label_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(label_description).to_be_visible()
    expect(label_description).to_have_text("Results from the load test pipeline will be displayed here")    
