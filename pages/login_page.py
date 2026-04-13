from pages.base_page import BasePage



class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.field_username = self.page.locator("#username")
        self.field_password = self.page.locator("#password")
        self.btn_login = self.page.get_by_role("button", name="Login")

    def fill_field_username(self, username):
        self.field_username.fill(username)

    def fill_field_password(self, password):
        self.field_password.fill(password)

    def login_process(self, username, password):
        self.fill_field_username(username)
        self.fill_field_password(password)
        self.btn_login.click()

    def login_process_fail_1(self, username):
        self.fill_field_username(username)
        self.btn_login.click()

    def login_process_fail_2(self, password):
        self.fill_field_password(password)
        self.btn_login.click()
