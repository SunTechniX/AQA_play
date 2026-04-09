from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://demoqa.com"
SELECT = "/select-menu"


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(f"{BASE_URL}{SELECT}")

        dropdown_menu = page.locator("#withOptGroup")
        dropdown_list = dropdown_menu.get_by_role("option")
        dropdown_menu.click()
        print(dropdown_list.count())
        print(dropdown_list.all_text_contents())
