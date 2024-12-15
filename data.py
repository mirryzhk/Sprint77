class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    ORDER_URL = '/orders'
    GET_ORDER_ID_URL = '/orders/track'
    ACCEPT_ORDER_URL = '/orders/accept'
    COURIER_URL = '/courier'
    LOGIN_COURIER_URL = '/courier/login'

class TestData:
    standart_courier = ['datauser', 'datapass', 'dataname']
    payload_order = {
        "firstName": "Владимир",
        "lastName": "Владимирович",
        "address": "г. Москва, ул. Южная, д. 27",
        "metroStation": 7,
        "phone": "+79999999999",
        "rentTime": 3,
        "deliveryDate": "2024-12-12",
        "comment": "Позвонить за 2 часа",
        "color": []
    }

    colors = ['', '["BLACK"]', '["GREY"]', '["BLACK", "GREY"]']
