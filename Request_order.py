import Configuration
import data
import requests
def create_new_order(order_body): #Создание заказа
    return requests.post(Configuration.URL+Configuration.CREATE_NEW_ORDER, json=order_body)

def get_track_number():# Получение трек номера
    new_order = create_new_order(data.order_body)
    order_track = str(new_order.json()['track'])
    return order_track

def order_track_info():
    return requests.get(Configuration.URL+Configuration.ORDER_TRACK_INFO+'?t='+get_track_number())

track_info = order_track_info()
