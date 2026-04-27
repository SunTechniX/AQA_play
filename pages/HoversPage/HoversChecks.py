from playwright.sync_api import expect

from pages.HoversPage.HoversLoc import HoversLoc


class HoversChecks(HoversLoc):

    def wait_for_text_under_img1(self, txt: str):
        # text_fact = self.txt1.text_content().strip()
        # assert text_fact == txt, "Alarm"
        expect(self.txt1).to_have_text(txt)

    def check_visible_text_under_img1(self):
        expect(self.txt1).to_be_visible()
        # self.txt1.wait_for(state="visible")
