from tests.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.loc_h1 = self.page.locator("h1.heading")
