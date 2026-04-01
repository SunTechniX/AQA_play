from playwright.sync_api import sync_playwright


# URL = "file:///AQA_01.html"
URL = "file:///D:/Data/py_code/EDU_zone/AQA/AQA_play/AQA_01.html"

if __name__ == "__main__":
    with (sync_playwright() as p):
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(URL)
        element_text = page.locator("[name='record'] li:nth-child(1)")
        text1 = element_text.text_content()
        text2 = element_text.inner_text()
        text3 = page.text_content("[name='record'] li:nth-child(1)")
        print(f"{text1}\n{text2}\n{text3}")

        field3 = page.locator("input[type='text']")
        field3.fill("Any Text")
        field3.input_value()


        field = page.locator("input[type='text']")
        print(f"Поле 1: '{field.input_value()}'")
        field.fill("Урок 27")
        field.type("Продолжение")
        print(f"Поле 2: '{field.input_value()}'")
        txt_area = page.locator("textarea")
        print(f"Область 1: '{txt_area.input_value()}'")
        txt_area.fill("Урок -27-")
        txt_area.type("Продолжение")
        print(f"Область 2: '{txt_area.input_value()}'")
