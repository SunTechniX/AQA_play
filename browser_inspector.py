from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_URL = "https://example.com/"

def inspect_page(url: str, browser_type: str = "chromium",
                 headless: bool = True) -> dict:
    with sync_playwright() as drv:
        match browser_type:
            case "chromium": brow_ = drv.chromium
            case "firefox": brow_ = drv.firefox
            case "webkit": brow_ = drv.webkit
            case _: brow_ = drv.chromium
        browser = brow_.launch(headless=headless)
        page_ = browser.new_page()
        page_.set_default_timeout(7000)
        page_.goto(url)
        di = {"url": url,
              "browser": browser_type,
              "title": page_.title(),
              "success": True,
              "viewport": page_.viewport_size,  # {'width': ..., 'height': ...}
              "url_final": page_.url,  # финальный URL (после редиректов)
              }
        browser.close()
    return di

#  Программа стартует ЗДЕСЬ!
if __name__ == "__main__":

    # 🌐24x02. Функция-обёртка с возвратом данных
    # b = "chromium"
    # d = inspect_page(BASE_URL, browser_type=b, headless=False)
    # print(f"[{b}] {d['title']}")
    # print(d)

    path_ = Path("output/screenshots/")
    path_.mkdir(parents=True, exist_ok=True)
    dt = datetime.now().strftime("%Y_%m_%d__%H-%M-%S")
    filename = path_ / f"chromium_{dt}.png"

    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False)
        # print("Начало работы браузера")
        page_ = browser.new_page()
        page_.set_default_timeout(7000)
        page_.goto(BASE_URL)
        page_.screenshot(path=filename)

        # 🌐24x01. Базовый запуск и заголовок
        html_page_title = page_.get_by_role("heading").inner_text()
        print(f"Заголовок: {html_page_title}")