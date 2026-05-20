# from playwright.sync_api import Page

def test_login(browser, context, page):
    page.goto("https://example.com/login")
    page.fill("#email", "user@example.com")
    page.click("text=Войти")
    # → browser, context, page созданы автоматически
