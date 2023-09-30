import configuration
import requests
import sender_stand_request

# Функция на получение данных о заказе по треку заказа
def get_order_details():
    track = sender_stand_request.get_new_order_track()
    params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER, params=params)

# Тест. При поиске заказа по треку возвращается код 200
def test_get_order_details():
    response_order = get_order_details()
    assert response_order.status_code == 200

# Юлия Кальницкая, 08а когорта - Финальный проект. Инженер по тестированию плюс

