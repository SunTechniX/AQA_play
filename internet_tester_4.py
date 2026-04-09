from playwright.sync_api import sync_playwright, Page
import pytest

class Any1:

    @property
    def var(self):
        res = 12 + 1
        return res

c = Any1()
print(c.var)


BASE_URL = "https://the-internet.herokuapp.com/"

@pytest.fixture
def page():  # -> Page
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False)
        page_ = browser.new_page()
        page_.goto(BASE_URL)

        # временно выйти из функции, сохранив состояние
        yield page_
        # мой код
        # my_test_code(page_)

        # вернёмся в это точку после того, как отработаем в моём коде

        page_.wait_for_timeout(3000)
        browser.close()
        # конец

def test_01(page: Page):
    print(f"{type(page)}")
    el = page.get_by_role("link", name="Form Authentication")
    el.click()


def test_02(page):
    el = page.get_by_role("link", name="Form Authentication")
    el.click()


if __name__ == '__main__':
    page_ = page()
    print(f"{type(page_)}")
    el = page_.get_by_role("link", name="Form Authentication")
    el.click()
