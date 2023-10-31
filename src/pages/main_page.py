import allure
from playwright.sync_api import Page, expect

class MainPage():

    def __init__(self, page: Page) -> None:
        self.page = page

    @allure.step("Open page")
    def open_page(self):
        self.page.goto("/")

    @allure.step("Assert the brand name")
    def should_have_the_navigate_name(self, brand_name):
        expect(self.page.get_by_role("link", name=brand_name)).to_be_visible()


