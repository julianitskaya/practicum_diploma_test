import configuration
import requests
import data

# Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)

# Функция на сохранение номера трека заказа
def get_new_order_track():
    # Создать новый заказ
    order_body = data.order_body
    response_order = post_new_order(order_body)
    # Запомнить номер трека заказа
    return response_order.json()["track"]

