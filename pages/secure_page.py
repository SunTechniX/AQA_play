from pages.base_page import BasePage


class SecurePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.btn_logout = page.get_by_role("link", name="Logout")

    def logout(self):
        self.btn_logout.click()
