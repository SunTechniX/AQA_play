import pytest
# from playwright.sync_api import Page

@pytest.fixture
def logged_in_page(page):
    page.goto("https://example.com/login")
    page.fill("#email", "admin@example.com")
    page.fill("#password", "secret123")
    page.click("text=Войти")
    return page  # ← этот объект будет доступен в тесте

def test_admin_panel(logged_in_page):
    logged_in_page.goto("/admin")
    assert logged_in_page.locator("text=Админ-панель").is_visible()
