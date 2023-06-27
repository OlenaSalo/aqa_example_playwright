from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, base_url):
         self.page.goto(base_url + "/admin/")

    def login_user(self, **user):
        self.page.locator("//input[@name='username']").fill(user['username'])
        self.page.locator("//input[@name='password']").fill(user['password'])
        self.page.locator("//input[@value='Log in']").click()