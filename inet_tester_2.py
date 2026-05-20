from playwright.sync_api import sync_playwright


URL = "https://the-internet.herokuapp.com/"


def deco(f_test):
    def wrapper():
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False, slow_mo=1000
            )
            page = browser.new_page()
            page.goto(URL)
            res = f_test(page)
            browser.close()
        return res

    return wrapper


def navigate_to_example(page, example_name: str) -> str:
    page.locator(f"text={example_name}").click()
    return page.url


@deco
def test_001(page):
    # Task 01
    title_tab = page.title()
    loc_h1 = page.get_by_text("Welcome to the-internet")
    title_h1 = loc_h1.text_content()
    assert "the-internet" in title_h1, "Не тот заголовок"
    print(f"Сайт доступен.\n"
          f"Заголовок закладки браузера: '{title_tab}'\n"
          f"Заголовок на странице: '{title_h1}'")

@deco
def test_002(page):
    # Task 02
    # current_url = navigate_to_example("Form Authentication")
    page.get_by_role("link", name="Form Authentication").click()
    current_url = page.url
    assert "/login" in current_url, "Не тот URL"
    print(f"Перешли в: Form Authentication | URL: {current_url}")

@deco
def test_003(page):
    navigate_to_example(page, "Form Authentication")
    # Task 03
    el_user = page.get_by_label("username")
    #el_user = page.locator("#username")
    el_pass = page.get_by_label("password")

    el_user.type("tomasanders")
    el_user.type("After TEXT")
    el_user.fill("tomsmith")
    el_pass.type("SuperSecretPassword!", delay=10)

    btn = page.get_by_role("button", name="Login")
    btn_name1 = btn.inner_text()
    btn_name2 = btn.text_content()
    btn.click()
    print(f"{btn_name1=} {btn_name2=}")

    assert "/secure" in page.url, "Не тот URL"
    print(f"✅ Успешный вход! URL: {page.url}")

def test_004():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto(URL)

        # Task 04
        page.get_by_role("link", name="Logout").click()
        assert "/login" in page.url
        print(f"✅ Успешный выход! URL: {page.url}")
        browser.close()

def test_005():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, slow_mo=1000
        )
        page = browser.new_page()
        page.goto(URL)

        # Task 05
        page.goto(URL)
        current_url = navigate_to_example("Checkboxes")

        chkbox1 = page.locator("#checkboxes input:nth-child(1)")
        chkbox2 = page.locator("#checkboxes input:nth-child(3)")
        print(f"{chkbox1.is_visible()=}")
        print(f"{chkbox1.is_enabled()=}")
        print(f"{chkbox1.is_checked()=}")
        print(f"{chkbox2.is_checked()=}")

        chkbox1.check()
        chkbox2.uncheck()

        print(f"✅ Checkbox 1: checked={chkbox1.is_checked()}")
        print(f"✅ Checkbox 2: checked={chkbox2.is_checked()}")
        browser.close()


def test_000_mobile():
    with sync_playwright() as drv:
        print("\n".join(list(drv.devices.keys())))


if __name__ == "__main__":
    test_001()
    test_002()
    test_003()
