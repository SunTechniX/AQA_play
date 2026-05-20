from pages.base_page import BasePage


class HoversLoc(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.img1 = self.page.locator("//div[@class='figure'][1]/img")
        self.txt1 = self.page.locator("//div[@class='figure'][1]/div[@class='figcaption']/h5")
