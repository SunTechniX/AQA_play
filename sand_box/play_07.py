from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://the-internet.herokuapp.com/"

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.set_default_timeout(3_000)
        page.goto(f"{BASE_URL}/add_remove_elements/")

        btn_add = page.get_by_role("button", name="Add Element")
        # for _ in range(5):
        #     btn_add.click()

        btns_with_name_delete = page.locator("//button[text()='Delete']")
        expect(btns_with_name_delete).not_to_be_visible()
        btns_with_name_delete.first.click()
        # assert btns_with_name_delete.count()
