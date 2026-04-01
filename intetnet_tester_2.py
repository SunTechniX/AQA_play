import time
import os
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect

load_dotenv()

BASE_URL = "https://the-internet.herokuapp.com"
USR_DYN_LOAD2 = "/dynamic_loading/2"

TEXT_TO_FIND = "the-internet"
LINK_LOGIN = "/login"
LINK_SECURE = "/secure"

TITLE_FORM = "Form Authentication"
TITLE_CHECKBOXES = "Checkboxes"
TITLE_DROPDOWN = "Dropdown"
TITLE_INPUTS = "Inputs"
TITLE_HOVERS = "Hovers"
TITLE_JS_ALERTS = "JavaScript Alerts"
TITLE_FILE_UPLOAD = "File Upload"
TITLE_DYN_LOAD = "Dynamic Loading"

LINK_DROPDOWN = "/dropdown"
OPTION_0 = "Please select an option"
OPTION_1 = "Option 1"
OPTION_2 = "Option 2"
NUMBER_123 = "123"
NUMBER_456 = "456"
TEXT_NAME_USER1 = "name: user1"
BUTTON_JS_ALERTS = "Click for JS Alert"
MSG_CLICK_JS_ALLERT = "You successfully clicked an alert"

FILE_NAME = "test_upload.txt"


def navigate_to_example(page, example_name: str):
    link = page.get_by_text(example_name)
    link.click()
    return page.url


def assert_text_in_url(page_url: str, text_in: str, ):
    assert text_in in page_url, \
        f"Не та страница!\n" \
        f"Ожидание: '{text_in}' в url\n" \
        f"Факт: '{page_url}'"


def _assert_selected(selected_option, selected_text):
    assert selected_option in selected_text, \
        f"\nОжидался текст: '{selected_option}'\n" \
        f"На странице оказался текст: '{selected_text}'"


def test_task_01():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        assert_text_in_url(page.url, TEXT_TO_FIND)
        loc_h1 = page.locator("h1.heading")
        text_h1 = loc_h1.text_content()
        assert TEXT_TO_FIND in text_h1, \
            f"Не тот заголовок!\n" \
            f"Ожидание: '{TEXT_TO_FIND}' в заголовке\n" \
            f"Актуальный текст заголовка: '{text_h1}'"
        print(f"T1: ✅ Сайт доступен. Заголовок: '{text_h1}'")


def test_task_02():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_FORM)
        assert_text_in_url(link_form, LINK_LOGIN)
        print(f"T2: ✅ Перешли в: Form Authentication | URL: {link_form}")


def test_task_03():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        field_username = page.locator("#username")
        field_password = page.locator("#password")
        env_username = os.getenv("USER")
        env_password = os.getenv("PASS")
        field_username.fill(env_username)
        field_password.fill(env_password)

        btn_login = page.locator("//button/i[contains(@class, 'sign-in')]")
        btn_login.click()
        assert_text_in_url(page.url, LINK_SECURE)
        print(f"T3: ✅ Успешный вход! URL: {page.url}")


def test_task_04():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        btn_logout = page.locator(".button[href='/logout']")
        btn_logout.click()
        assert_text_in_url(page.url, LINK_LOGIN)
        print(f"T4: ✅ Успешный выход! URL: {page.url}")

def test_task_05():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_CHECKBOXES)
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


def test_task_06():

    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_DROPDOWN)
        assert_text_in_url(link_form, LINK_DROPDOWN)
        selected_option = page.locator("[selected='selected']")
        _assert_selected(OPTION_0, selected_option.inner_text())

        drop_list = page.locator("#dropdown")
        drop_list.select_option("1")
        _assert_selected(OPTION_1, selected_option.inner_text())

        drop_list.select_option("2")
        _assert_selected(OPTION_2, selected_option.inner_text())

        print(f"✅ Выбрано: {selected_option.inner_text()}")


def test_task_07():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_INPUTS)
        field = page.locator("input[type='number']")
        field.fill(NUMBER_123)
        _assert_selected(NUMBER_123, field.input_value())

        field.clear()
        field.fill(NUMBER_456)
        _assert_selected(NUMBER_456, field.input_value())

        print(f"✅ Введено: {field.input_value()}")


def test_task_08():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_HOVERS)
        field = page.locator("input[type='number']")

        figures_xpath = page.locator("//div[@class='figure']")
        figures_css = page.locator(".figure")
        print(f"{figures_xpath.count()} {figures_css.count()}")
        # figure = page.locator(".figure:nth-child(3)")
        figure = page.locator("//div[@class='figure'][1]")
        # figure = figures_css.all()[0]
        figure = figures_css.first
        fig_caption = figure.locator(".figcaption h5")
        figure.hover()
        assert fig_caption.is_visible(), f"Текст '{TEXT_NAME_USER1}' не видим"
        _assert_selected(TEXT_NAME_USER1, fig_caption.inner_text())

        print(f"✅ Навели на изображение. Текст: '{fig_caption.inner_text()}'")


def test_task_09():

    def accept_dialog(dialog):
        return dialog.accept()

    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_JS_ALERTS)
        btn_js_alerts = page.get_by_role("button", name=BUTTON_JS_ALERTS)
        btn_js_alerts.click()
        time.sleep(3)
        page.on("dialog", accept_dialog)
        # page.on("dialog", lambda d: d.accept())
        result = page.locator("#result")
        _assert_selected(MSG_CLICK_JS_ALLERT, result.inner_text())

        print(f"✅ Alert принят. Сообщение: '{result.inner_text()}'")


def test_task_10():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(BASE_URL)

        link_form = navigate_to_example(page, TITLE_FILE_UPLOAD)

        #file_upload = Path(__file__).parent / FILE_NAME

        field_file_upload = page.locator("#file-upload")
        # field_file_upload.set_input_files(file_upload)
        field_file_upload.set_input_files(FILE_NAME)

        btn_upload = page.locator("#file-submit")
        btn_upload.click()


def test_task_11():
    with (sync_playwright() as drv):
        browser = drv.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        # page.goto(BASE_URL)
        #
        # navigate_to_example(page, TITLE_DYN_LOAD)
        #
        # # navigate_to_example(page,
        # #                     "Example 1: Element on page that is hidden")
        # # btn_start = page.locator("#start")
        # # btn_start.click()
        #
        # # finish_text = page.locator("#finish")
        # # txt = finish_text.inner_text()
        # # print(txt, finish_text.is_visible())
        #
        # navigate_to_example(page,
        #                     "Example 2: Element rendered after the fact")
        # # btn_start2 = page.locator("#start")
        page.goto(f"{BASE_URL}{USR_DYN_LOAD2}")

        btn_start2 = page.get_by_role("button", name="Start")
        btn_start2.click()

        finish_text2 = page.locator("#finish")
        expect(finish_text2).to_be_visible()
        expect(finish_text2).to_contain_text("Worl")
        txt = finish_text2.inner_text()
        assert "Hello World" in txt
        print(txt, finish_text2.is_visible())


if __name__ == "__main__":
    test_task_11()
