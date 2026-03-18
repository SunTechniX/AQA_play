import re
import time
from pathlib import Path

from playwright.sync_api import sync_playwright


# URL = "https://www.example.com"
URL = "https://yandex.ru"
VIEW_PORT_1 = {'width': 900, 'height': 500}


def get_safe_name(url: str) -> str:
    return re.sub(r'[^\w\-_]', '_', url)  # безопасное имя

def inspect_page(url: str, browser_type: str = "chromium",
                 headless: bool = True, screenshot: bool = False,
                 retries: int = 1, timeout=600) -> dict:
    info = {}
    success_run = False
    for i in range(retries):
        try:
            with sync_playwright() as p:
                # browser = p.chromium.launch_persistent_context(
                #     headless=False,
                #     user_data_dir='user_data_1',
                #     viewport=VIEW_PORT_1
                #     )
                match browser_type:
                    case "chromium":
                        browser = p.chromium.launch(
                            headless=headless, slow_mo=1000, timeout=timeout,
                            )
                    case "firefox":
                        browser = p.firefox.launch(
                            headless=headless, slow_mo=1000, timeout=timeout,
                            )
                    case _:
                        browser = p.chromium.launch(
                            headless=headless, channel="chrome", slow_mo=1000,
                            timeout=timeout
                            )
                page = browser.new_page()

                # Время загрузки страницы
                start = time.perf_counter()
                start_ = time.monotonic()
                response = page.goto(url)
                page.wait_for_load_state("load")
                load_time = round(time.perf_counter() - start, 2)
                load_time_ = round(time.monotonic() - start_, 2)

                info = {"url": url,
                        "browser": browser_type,
                        "title": page.title(),
                        "status": response.status,
                        "success": None,
                        "viewport": page.viewport_size,  # {'width': ..., 'height': ...}
                        "url_final": page.url,  # финальный URL (после редиректов)
                        "load_time": f"{load_time} | {load_time_}"
                        }
                if screenshot:
                    screen_dir = Path("output/screenshots/")
                    screen_dir.mkdir(parents=True, exist_ok=True)
                    safe_name = get_safe_name(url)
                    screen_file = f"{browser_type}_{safe_name}.png"
                    screen_path = screen_dir / screen_file
                    page.screenshot(path=screen_path, full_page=True)
                    info["screenshot"] = screen_path

                browser.close()
                success_run = True
        except Exception as e:
            if i == retries - 1:
                info["error"] = str(e)

    info["success"] = success_run
    return info

if __name__ == "__main__":
    ipage = inspect_page(url=URL, browser_type="chromium",  # "chromium",
                         headless=False,  screenshot=False,
                         retries=3, timeout=550)  # 550 - на грани
    if not ipage["success"]:
        print(f"❌ Ошибка: {ipage['error']}")
    else:
        print(f"[{ipage['browser']}] {ipage['title']}\n"
              f"Status: {ipage['status']}\n"
              f"Viewport: {ipage['viewport']}\n"
              f"Финальный URL: {ipage['url_final']}\n"
              f"Загрузка: {ipage['load_time']}c")
        if 'screenshot' in ipage:
            print(f"📸 Скриншот: {ipage['screenshot']}")
