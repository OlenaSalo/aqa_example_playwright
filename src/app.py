from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage


class Application:

    def __init__(self, page, base_url=None):
         self.page = page
         self.base_url = base_url

    def login_page(self) -> LoginPage:
        return LoginPage(self.page)

    def main_page(self) -> MainPage:
        return MainPage(self.page)