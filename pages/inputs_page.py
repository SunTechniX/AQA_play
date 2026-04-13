from pages.base_page import BasePage


class InputsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.field = self.page.locator("input[type='number']")
