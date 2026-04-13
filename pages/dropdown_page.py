from pages.base_page import BasePage


class DropdownPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.dropdown = page.locator("#dropdown")
        self.select_1 = page.locator("#dropdown option:nth-child(1)")

    def check_select_option_default(self):
        select_1_text = self.select_1.inner_text()
        self.assert_subtext_in_text("Please select an option",
                                    select_1_text, "Элемент ")

    def click_dropdown(self):
        self.dropdown.click()
