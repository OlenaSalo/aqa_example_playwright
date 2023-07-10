class BasePage:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

    def navigate(self, endpoint):
        url = self.base_url + endpoint
        self.page.goto(url)


