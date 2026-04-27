from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://the-internet.herokuapp.com/"

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.wait_for_load_state("networkidle", timeout=10_000)
        page.set_default_timeout(7_000)
        page.goto(f"{BASE_URL}/checkboxes")

        cbh = page.locator("#checkboxes")
        # cb = page.locator("input[type='checkbox']")
        # cb = page.locator("//input[@type='checkbox']")
        # Ищем input, после которого идёт текст "checkbox 1"
        cb = page.locator(
            "//input[@type='checkbox'][following-sibling::text()[contains(., 'checkbox 1')]]"
            )
        cb_text = page.locator(
            "//input[@type='checkbox'][1]/following-sibling::text()[1]"
            )
        print(cbh.inner_text())
        print(cb.count())
        print(f"'{cb_text.inner_text()=}'")
        expect(cb.first).not_to_be_empty(timeout=1_000)
        cb.check()
        assert cb.is_checked()
