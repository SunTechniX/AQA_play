from playwright.sync_api import sync_playwright


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
        print(f"{txth1.text_content()=}")
        print(f"{txth1.inner_text()=}")
        browser.close()

