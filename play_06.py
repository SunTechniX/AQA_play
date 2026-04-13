from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://demoqa.com"
SELECT = "/select-menu"


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(f"{BASE_URL}{SELECT}")

        dropdown_menu = page.locator("#withOptGroup")
        dropdown_list = page.locator("#withOptGroup").get_by_role("option")
        assert dropdown_list.count() == 0, "кол-во элементов не 0"
        dropdown_menu.click()
        assert dropdown_list.count() == 6, \
            "Кол-во элементов отличается от ожидаемого"
        print(dropdown_menu.count(), dropdown_list.count())
        print(dropdown_list.all_text_contents())
        items = dropdown_list.all()
        filtered = dropdown_list.filter(has_text="Group 1, option 1")
        print(filtered.count())
        print(filtered.all_text_contents())
        filtered.first.click()

