from playwright.sync_api import Page

from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage


class Application:

    def __init__(self, page: Page):
        self.page = page

    # def load(self, url):
    #     self.page.goto(url)

    def login_page(self):
        return LoginPage(self.page)

    def main_page(self):
        return MainPage(self.page)