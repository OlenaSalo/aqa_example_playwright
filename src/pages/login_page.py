import allure
from playwright.sync_api import Page

from src.pages.componets.authoritation import AuthorizationComponent
from src.utils import parse_json


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.auth = AuthorizationComponent()

    @allure.step("Open page")
    def open_page(self):
        self.page.goto("admin/")


    @allure.step("Login user")
    def login_user(self, user_role):
        user: dict = parse_json("account.json")[user_role]
        self.page.get_by_text("Log in").click()
        self.page.get_by_placeholder("Email").fill(user['username'])
        self.page.get_by_placeholder("Password").fill(user['password'])
        self.page.locator(".SignupButton").click()