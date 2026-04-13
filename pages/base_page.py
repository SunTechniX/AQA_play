class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate_to_example(self, example_name: str):
        el_form_auth = self.page.get_by_role("link", name=example_name)
        el_form_auth.click()
        return self.page.url

    def assert_text_in_url_print(self, text_expected: str, msg: str = ""):
        assert text_expected in self.page.url, "Не та страница!"
        print(f"\n{msg}URL: {self.page.url}")

    def assert_subtext_in_text(self, subtext: str, text: str, msg: str = ""):
        assert subtext in text, \
            f"{msg}'{text}' не содержит '{subtext}'"
