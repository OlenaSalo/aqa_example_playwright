import allure
from playwright.sync_api import Page, expect

from src.pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, page, base_url):
        super().__init__(page, base_url)


    @allure.step("Verify the brand name")
    def verify_the_brand_name(self, brand_name):
        expect(self.page.locator("//a[@href='/admin/']")).to_have_text(brand_name)
