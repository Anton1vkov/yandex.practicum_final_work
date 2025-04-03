import requests
import urls
import data

# Функция создания заказа и сохранения номера трека заказа

def post_new_orders():
    req = requests.post(urls.URL + urls.CREATE_ORDERS,
                        json=data.orders_body).json()["track"]
    return req


# Функция получения заказа по треку заказа

def get_info():
    track = post_new_orders()
    req = requests.get(urls.URL + urls.INFO + str(track))
    return req