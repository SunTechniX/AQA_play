from playwright.sync_api import sync_playwright, expect

BASE_URL = "https://github.com/"

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="gh_cookie", headless=False, slow_mo=1000
            )
        page = browser.new_page()
        page.goto(BASE_URL)
        page.set_default_timeout(7_000)

        # link_sign_in = page.get_by_role("link", name="Sign in")
        # field_login = page.get_by_role("textbox", name="Username or email address")
        # field_password = page.get_by_role("textbox", name="Password")
        # btn_sign_in = page.get_by_role("button", name="Sign in", exact=True)
        #
        # link_sign_in.click()
        # field_login.fill("SunTechniX")
        # field_password.fill("Senatra8#")
        # btn_sign_in.click()

        # page.pause()

    # ---------------------
