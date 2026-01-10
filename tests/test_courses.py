from playwright.sync_api import Page, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
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
