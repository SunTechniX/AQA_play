from playwright.sync_api import expect

from pages.HoversPage.HoversLoc import HoversLoc


class HoversSteps(HoversLoc):

    def move_cursor_hover_img1(self):
        self.img1.hover()
