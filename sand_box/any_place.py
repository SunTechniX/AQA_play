
with allure.step("Проверка статуса 403 Forbidden"):
    assert response.status_code == 403

check_status(403, " Forbidden")


@allure.step("Проверка статуса {expected_status}{msg}"):
def check_status(expected_status: int = 200, msg: str = ""):
    assert response.status_code == expected_status



