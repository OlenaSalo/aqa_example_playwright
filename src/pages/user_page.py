from playwright.sync_api import Page


class UserPage():

    def __init__(self, page: Page):
        self.page = page

