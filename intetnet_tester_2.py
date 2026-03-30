import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


load_dotenv()

URL = "https://the-internet.herokuapp.com/"
TEXT_TO_FIND = "the-internet"
TEXT_LOGIN = "/login"
TEXT_SECURE = "/secure"
TEXT_FORM = "Form Authentication"
TEXT_CHECKBOXES = "Checkboxes"


def navigate_to_example(example_name: str):
    link = page.get_by_text(example_name)
    link.click()
    return page.url


def assert_text_in_url(page_url: str, text_in: str, ):
    assert text_in in page_url, \
        f"Не та страница!\n" \
        f"Ожидание: '{text_in}' в url\n" \
        f"Факт: '{page_url}'"


if __name__ == "__main__":
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)

        # Task 01
        assert_text_in_url(page.url, TEXT_TO_FIND)
        loc_h1 = page.locator("h1.heading")
        text_h1 = loc_h1.text_content()
        assert TEXT_TO_FIND in text_h1, \
            f"Не тот заголовок!\n" \
            f"Ожидание: '{TEXT_TO_FIND}' в заголовке\n" \
            f"Актуальный текст заголовка: '{text_h1}'"
        print(f"T1: ✅ Сайт доступен. Заголовок: '{text_h1}'")

        # Task 02
        link_form = navigate_to_example(TEXT_FORM)
        assert_text_in_url(link_form, TEXT_LOGIN)
        print(f"T2: ✅ Перешли в: Form Authentication | URL: {link_form}")

        # Task 03
        field_username = page.locator("#username")
        field_password = page.locator("#password")
        env_username = os.getenv("USER")
        env_password = os.getenv("PASS")
        field_username.fill(env_username)
        field_password.fill(env_password)

        btn_login = page.locator("//button/i[contains(@class, 'sign-in')]")
        btn_login.click()
        assert_text_in_url(page.url, TEXT_SECURE)
        print(f"T3: ✅ Успешный вход! URL: {page.url}")

        # Task 04
        btn_logout = page.locator(".button[href='/logout']")
        btn_logout.click()
        assert_text_in_url(page.url, TEXT_LOGIN)
        print(f"T4: ✅ Успешный выход! URL: {page.url}")

        # Task 05
        page.goto(URL)
        link_form = navigate_to_example(TEXT_CHECKBOXES)
        chkbox1 = page.locator("//form[@id='checkboxes']/input[1]")
        chkbox2 = page.locator("//form[@id='checkboxes']/input[2]")

        assert not chkbox1.is_checked(), "Чекбокс 1 ОТМЕЧЕН!"
        assert chkbox2.is_checked(), "Чекбокс 2 НЕ отмечен!"

        # chkbox1.click()
        # chkbox2.click()

        chkbox1.check()
        chkbox2.uncheck()

        print(f"T5: ✅ Checkbox 1: checked={chkbox1.is_checked()}\n"
              f"T5: ✅ Checkbox 2: checked={chkbox2.is_checked()}")
