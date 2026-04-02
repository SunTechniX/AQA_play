import time

from playwright.sync_api import expect

from tests.conftest import page
from tests.data import BASE_URL, USR_DYN_LOAD2, TEXT_TO_FIND, LINK_LOGIN, \
    LINK_SECURE, TITLE_FORM, TITLE_CHECKBOXES, TITLE_DROPDOWN, TITLE_INPUTS, \
    TITLE_HOVERS, TITLE_JS_ALERTS, TITLE_FILE_UPLOAD, LINK_DROPDOWN, OPTION_0, \
    OPTION_1, OPTION_2, NUMBER_123, NUMBER_456, TEXT_NAME_USER1, \
    BUTTON_JS_ALERTS, MSG_CLICK_JS_ALLERT, FILE_NAME
from tests.helpers import assert_text_in_url, \
    assert_selected
from tests.login_page import LoginPage
from tests.main_page import MainPage


class TestLoc:

    def test_task_01(self, page):
        main_page = MainPage(page)
        assert_text_in_url(main_page.page.url, TEXT_TO_FIND)
        loc_h1 = main_page.loc_h1
        text_h1 = loc_h1.text_content()
        assert TEXT_TO_FIND in text_h1, \
            f"Не тот заголовок!\n" \
            f"Ожидание: '{TEXT_TO_FIND}' в заголовке\n" \
            f"Актуальный текст заголовка: '{text_h1}'"
        print(f"\nT1: ✅ Сайт доступен. Заголовок: '{text_h1}'")


    def test_task_02(self, page):
        main_page = MainPage(page)
        link_form = main_page.navigate_to_example(TITLE_FORM)
        assert_text_in_url(link_form, LINK_LOGIN)
        print(f"\nT2: ✅ Перешли в: Form Authentication | URL: {link_form}")


    def test_task_03(self, page):
        login_page = LoginPage(page)
        login_page.login_process()
        assert_text_in_url(page.url, LINK_SECURE)
        print(f"\nT3: ✅ Успешный вход! URL: {page.url}")


    def test_task_04(self, page):
        login_page = LoginPage(page)
        login_page.login_process()
        btn_logout = page.locator(".button[href='/logout']")
        btn_logout.click()
        assert_text_in_url(page.url, LINK_LOGIN)
        print(f"\nT4: ✅ Успешный выход! URL: {page.url}")


    def test_task_05(self, page):
        link_form = navigate_to_example(page, TITLE_CHECKBOXES)
        chkbox1 = page.locator("//form[@id='checkboxes']/input[1]")
        chkbox2 = page.locator("//form[@id='checkboxes']/input[2]")

        assert not chkbox1.is_checked(), "Чекбокс 1 ОТМЕЧЕН!"
        assert chkbox2.is_checked(), "Чекбокс 2 НЕ отмечен!"

        # chkbox1.click()
        # chkbox2.click()

        chkbox1.check()
        chkbox2.uncheck()

        print(f"\nT5: ✅ Checkbox 1: checked={chkbox1.is_checked()}\n"
              f"\nT5: ✅ Checkbox 2: checked={chkbox2.is_checked()}")


    def test_task_06(self, page):
        link_form = navigate_to_example(page, TITLE_DROPDOWN)
        assert_text_in_url(link_form, LINK_DROPDOWN)
        selected_option = page.locator("[selected='selected']")
        assert_selected(OPTION_0, selected_option.inner_text())

        drop_list = page.locator("#dropdown")
        drop_list.select_option("1")
        assert_selected(OPTION_1, selected_option.inner_text())

        drop_list.select_option("2")
        assert_selected(OPTION_2, selected_option.inner_text())

        print(f"\n✅ Выбрано: {selected_option.inner_text()}")


    def test_task_07(self, page):
        link_form = navigate_to_example(page, TITLE_INPUTS)
        field = page.locator("input[type='number']")
        field.fill(NUMBER_123)
        assert_selected(NUMBER_123, field.input_value())

        field.clear()
        field.fill(NUMBER_456)
        assert_selected(NUMBER_456, field.input_value())

        print(f"\n✅ Введено: {field.input_value()}")


    def test_task_08(self, page):
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
        assert_selected(TEXT_NAME_USER1, fig_caption.inner_text())

        print(f"\n✅ Навели на изображение. Текст: '{fig_caption.inner_text()}'")


    def test_task_09(self, page):

        def accept_dialog(dialog):
            return dialog.accept()

        link_form = navigate_to_example(page, TITLE_JS_ALERTS)
        btn_js_alerts = page.get_by_role("button", name=BUTTON_JS_ALERTS)
        btn_js_alerts.click()
        time.sleep(3)
        page.on("dialog", accept_dialog)
        # page.on("dialog", lambda d: d.accept())
        result = page.locator("#result")
        assert_selected(MSG_CLICK_JS_ALLERT, result.inner_text())

        print(f"\n✅ Alert принят. Сообщение: '{result.inner_text()}'")


    def test_task_10(self, page):
        link_form = navigate_to_example(page, TITLE_FILE_UPLOAD)

        #file_upload = Path(__file__).parent / FILE_NAME

        field_file_upload = page.locator("#file-upload")
        # field_file_upload.set_input_files(file_upload)
        field_file_upload.set_input_files(FILE_NAME)

        btn_upload = page.locator("#file-submit")
        btn_upload.click()

        uploaded_files = page.locator("#uploaded-files")
        assert FILE_NAME in uploaded_files.inner_text(), \
            f"Файл '{FILE_NAME}' отсутствует в списке загруженных файлов!"

        print(f"\n✅ Файл загружен: '{uploaded_files.inner_text()}'")


    def test_task_11(self, page):
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
