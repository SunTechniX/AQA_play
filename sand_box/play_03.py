from playwright.sync_api import sync_playwright


URL = "https://example.com"

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="../my_cookie",
            headless=False, slow_mo=1000
            )
        page = browser.new_page()
        page.goto(URL)
        value = page.evaluate("localStorage.getItem('inspector_run')")
        print("Данные из cookie:", value)
        page.evaluate("localStorage.setItem('inspector_run', '2')")
