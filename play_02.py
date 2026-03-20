from playwright.sync_api import sync_playwright, expect


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
            )
        page = browser.new_page()
        page.goto("https://www.example.com")
        # print(page.title())
        txt = page.locator("#dn-default h1")
        txth1 = page.locator("text=Example Domain")
        txth1.all_inner_texts()
        expect(txth1).to_have_text("Example Domain")
        print(f"{txth1.text_content()=}")
        print(f"{txth1.inner_text()=}")
        browser.close()

