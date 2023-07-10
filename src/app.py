from playwright.sync_api import Page

from src.pages.base_page import BasePage
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage


class Application:

    def __init__(self, page, base_url=None):
         self.page = page
         self.base_url = base_url

    def login_page(self):
        return LoginPage(self.page, self.base_url)

    def main_page(self):
        return MainPage(self.page, self.base_url)