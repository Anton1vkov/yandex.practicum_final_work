# Антон Ивков, 28А когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

# Проверка, что код ответа равен 200

def test_create_orders_code_200():
    assert sender_stand_request.get_info().status_code == 200