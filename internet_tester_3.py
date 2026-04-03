from playwright.sync_api import sync_playwright

BASE_URL = "https://the-internet.herokuapp.com/"


with sync_playwright() as drv:
    browser = drv.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL)
    page.wait_for_timeout(200)
