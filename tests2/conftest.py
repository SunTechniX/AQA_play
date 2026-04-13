import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://the-internet.herokuapp.com/"


@pytest.fixture
def page():
    with sync_playwright() as drv:
        browser = drv.firefox.launch(headless=False)
        # print("Начало работы браузера")
        page_ = browser.new_page()
        page_.set_default_timeout(7000)
        page_.goto(BASE_URL)
        yield page_
        browser.close()
        # print("Завершение работы браузера")

