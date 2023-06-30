import allure
from playwright.sync_api import Page, expect


class MainPage:


    def __init__(self, page: Page):
        self.page = page


    @allure.step("Open main page")
    def navigate(self, url):
        self.page.goto(url)

    @allure.step("Verify the brand name")
    def verify_the_brand_name(self, brand_name):
        expect(self.page.locator("//a[@href='/admin/']")).to_have_text(brand_name)
