BASE_URL = 'https://www.google.com'


class BasePage:

    def open(self, url):
        self.url = url


class AnyPage(BasePage):

    def __init__(self, name):
        self.loki_01 = ...
        self.loki_02 = ...

    def get_loki_001_text(self):
        return self.loki_01.text_content()

    def super_open(self, end_point: str):
        self.open(BASE_URL + end_point)


def test_any_01():
    any_page = AnyPage('any')
    any_page.super_open('/inv')
