﻿## Вторая часть практического блока финального проекта Яндекс Практикум
#### Задание 1. Проверить, отображается ли созданный заказ в базе данных.
#### Задание 2. Убедиться, что в базе данных статусы заказов записываются корректно.
#### Задание 3. Проверить получение кода ответа 200 при запросе информации о заказе по его трек-номеру через API Яндекс.Самокат
![alt text](image-1.png)
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполняется командой pytest

### Используемые ручки:

- Получить заказ по его номеру ("/v1/orders/track?=")
- Создать заказ ("/api/v1/orders")
