class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate_to_example(self, example_name: str):
        link = self.page.get_by_text(example_name)
        link.click()
        return self.page.url
