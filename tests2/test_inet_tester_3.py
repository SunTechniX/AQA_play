import os

from dotenv import load_dotenv

from data.data_names import TITLE, TITLE_FORM_AUTH, TITLE_DROPDOWN, \
    PAGE_LOGIN
from pages.dropdown_page import DropdownPage
from pages.inputs_page import InputsPage
from pages.secure_page import SecurePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


load_dotenv()


def test_01(page):
    """ 🌐26x01: Базовый вход на сайт """
    # print("-- Начало Тест-кейс 1")
    main_page = MainPage(page)
    el_head_text = main_page.el_head.inner_text()
    main_page.assert_subtext_in_text(TITLE, el_head_text, "Заголовок ")


def test_02(page):
    """ 🌐26x02: Навигация по ссылкам """
    main_page = MainPage(page)
    main_page.navigate_to_example(TITLE_FORM_AUTH)
    main_page.assert_text_in_url_print(PAGE_LOGIN,
                                      "✅ Перешли в: Form Authentication | ")


def test_03(page):
    """ 🌐26x03: Форма логина (Fill + Click) """
    main_page = MainPage(page)
    main_page.navigate_to_example(TITLE_FORM_AUTH)
    login_page = LoginPage(page)
    env_username = os.environ.get("USER")
    env_password = os.environ.get("PASS")
    login_page.login_process(env_username, env_password)
    login_page.assert_text_in_url_print("/secure", "✅ Успешный вход! ")


def test_04(page):
    """
    🌐26x04: Выход из системы (Logout)

    :param: page - фикстура браузер + страница
    :return: None
    """
    test_03(page)
    lk_page = SecurePage(page)
    lk_page.logout()
    lk_page.assert_text_in_url_print(PAGE_LOGIN, "✅ Успешный выход! ")


def test_06(page):
    main_page = MainPage(page)
    main_page.navigate_to_example(TITLE_DROPDOWN)
    dropdown_page = DropdownPage(page)
    dropdown_page.check_select_option_default()
    dropdown_page.click_dropdown()


def test_07(page):
    main_page = MainPage(page)
    main_page.navigate_to_example("Inputs")
    inputs_page = InputsPage(page)
    inputs_page.field.fill("123")
    inputs_page.page.wait_for_timeout(2000)
    inputs_page.field.clear()
    inputs_page.page.wait_for_timeout(2000)
