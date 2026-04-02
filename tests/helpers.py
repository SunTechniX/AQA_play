def assert_text_in_url(page_url: str, text_in: str, ):
    assert text_in in page_url, \
        f"Не та страница!\n" \
        f"Ожидание: '{text_in}' в url\n" \
        f"Факт: '{page_url}'"


def assert_selected(selected_option, selected_text):
    assert selected_option in selected_text, \
        f"\nОжидался текст: '{selected_option}'\n" \
        f"На странице оказался текст: '{selected_text}'"
