import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, sync_playwright


load_dotenv()

BASE_URL = "https://the-internet.herokuapp.com/"
TITLE = "the-internet"
TITLE_FORM_AUTH = "Form Authentication"


@pytest.fixture
def page():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False)
        # print("Начало работы браузера")
        yield browser.new_page()
        browser.close()
        # print("Завершение работы браузера")


def navigate_to_example(page, example_name: str):
    el_form_auth = page.get_by_role("link", name=example_name)
    el_form_auth.click()
    return page.url


def assert_text_in_url_print(page, text_expected: str, msg: str = ""):
    assert text_expected in page.url, "Не та страница!"
    print(f"\n{msg}URL: {page.url}")


def test_01(page):
    # 🌐26x01: Базовый вход на сайт
    # print("-- Начало Тест-кейс 1")
    page.goto(BASE_URL)
    page.wait_for_timeout(200)

    el_head = page.get_by_role("heading", name="to the-internet")
    el_head_text = el_head.inner_text()

    # if TITLE not in el_head_text:
    #     raise f"Заголовок '{el_head_text}' не содержит '{TITLE}'"
    assert TITLE in el_head_text, \
        f"Заголовок '{el_head_text}' не содержит '{TITLE}'"
    # print("== Завершение Тест-кейс 1")


def test_02(page):
    # 🌐26x02: Навигация по ссылкам
    page.goto(BASE_URL)
    navigate_to_example(page, TITLE_FORM_AUTH)
    assert_text_in_url_print(page, "/login",
                             "✅ Перешли в: Form Authentication | ")


def test_03(page):
    # 🌐26x03: Форма логина (Fill + Click)
    page.goto(BASE_URL)
    navigate_to_example(page, TITLE_FORM_AUTH)
    field_username = page.locator("#username")
    field_password = page.locator("#password")
    env_username = os.environ.get("USER")
    env_password = os.environ.get("PASS")
    field_username.fill(env_username)
    field_password.fill(env_password)
    btn_login = page.get_by_role("button", name="Login")
    btn_login.click()
    assert_text_in_url_print(page, "/secure",
                             "✅ Успешный вход! ")

# if __name__ == "__main__":
#     t_01()
