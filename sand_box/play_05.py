from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://the-internet.herokuapp.com/"
USR_DYN_LOAD2 = "/dynamic_loading/2"

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
            )
        page = browser.new_page()
        page.goto(f"{BASE_URL}{USR_DYN_LOAD2}")

        btn_start2 = page.get_by_role("button", name="Start")
        btn_start2.click()

        finish_text2 = page.locator("#finish")

        expect(finish_text2).to_be_visible(timeout=3000)
        # finish_text2.wait_for(state="visible", timeout=3000)
        expect(finish_text2).to_contain_text("Worl")

        txt = finish_text2.inner_text()
        assert "Hello World" in txt
        print(txt, finish_text2.is_visible())