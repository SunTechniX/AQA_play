import pytest
from playwright.sync_api import sync_playwright

from tests.data import BASE_URL


@pytest.fixture
def page():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(timeout=5_000)
        page_ = browser.new_page()
        page_.goto(BASE_URL)
        yield page_
