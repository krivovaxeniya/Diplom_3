import allure
import requests
import random
import string
from data import Data


@allure.step('Используется метод регистрации нового пользователя, который возвращает список из email, пароля и имени')
def register_new_user_and_return_user_info():
    user_info = {}
    payload = {
        "email": f'krivova_webtest_5@mail.ru',
        "password": '123456789',
        "name": 'Xeniya'}
    response_registration = requests.post(f'{Data.site_main_page}{Data.endpoint_register}', data=payload)
    if response_registration.status_code == 200:
        user_info = {"email": payload.get('email'),
                     "password": payload.get('password'),
                     "name": payload.get('name'),
                     "token": response_registration.json()["accessToken"]}
    return user_info


@allure.step('Используется метод получения списка ингредиентов, откуда произвольно выбираются два элемента и '
             'добавляются в список')
def get_ingredients():
    response = requests.get(f'{Data.site_main_page}{Data.endpoint_ingredients}')
    ingredients = response.json()['data']
    random_ingr_id_1 = random.choice(list(ingredients))['_id']
    random_ingr_id_2 = random.choice(list(ingredients))['_id']
    random_ingr_list = [random_ingr_id_1, random_ingr_id_2]
    return random_ingr_list


@allure.step('Используются методы создания нового пользователя и получения списка ингредиентов, для нового '
             'пользователя создается заказ с выбранными ингредиентами')
def create_user_and_create_order():
    user_data = register_new_user_and_return_user_info()
    ingredient_list = get_ingredients()
    payload = {"ingredients": ingredient_list}
    response = requests.post(f'{Data.site_main_page}{Data.endpoint_order}',
                             headers={'Authorization': user_data.get("token")}, data=payload)
    user_data["order_number"] = response.json()["order"]["number"]
    return user_data
