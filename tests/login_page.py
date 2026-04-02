import os

from dotenv import load_dotenv

from tests.base_page import BasePage
from tests.data import TITLE_FORM


load_dotenv()


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def login_process(self):
        self.navigate_to_example(TITLE_FORM)
        field_username = self.page.locator("#username")
        field_password = self.page.locator("#password")
        env_username = os.getenv("USER")
        env_password = os.getenv("PASS")
        field_username.fill(env_username)
        field_password.fill(env_password)
        btn_login = self.page.locator("//button/i[contains(@class, 'sign-in')]")
        btn_login.click()
