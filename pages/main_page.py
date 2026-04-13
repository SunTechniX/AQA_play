from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.el_head = page.get_by_role("heading", name="to the-internet")
