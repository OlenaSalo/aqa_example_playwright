import allure

from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)

    @allure.step("Open page")
    def navigate(self):
        super().navigate("/admin/")


    @allure.step("Login user")
    def login_user(self, **user):
        self.page.locator("//input[@name='username']").fill(user['username'])
        self.page.locator("//input[@name='password']").fill(user['password'])
        self.page.locator("//input[@value='Log in']").click()