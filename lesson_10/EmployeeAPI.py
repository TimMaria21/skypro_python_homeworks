import requests
import allure
from typing import Tuple
from typing import Dict, Any


class Employee:

    def __init__(self, url: str) -> None:
        self.url = url


    @allure.step("API.Получение токена авторизации {user}:{password}")
    def get_token(self, user: str='leonardo', password: str='leads') -> str:
        """
        Получение токена авторизации
        :params user(str): логин 
        :params password(str): пароль 

        :return: str: token
        """
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + "/auth/login", json=creds)
        return resp.json()["userToken"]


    @allure.step("api.Создание компании {name}:{description}")
    def create_company(self, name: str, description: str) -> Dict[str, Any]:
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + "/company", json=company, headers=my_headers)
        return resp.json()


    @allure.step("api.Получение списка сотрудников компании {companyId}")
    def get_employees_list(self, companyId: int) -> Dict[str, Any]:
        my_params = {
            "company": companyId
        }
        resp = requests.get(self.url + "/employee", params=my_params)
        return resp.json()


    @allure.step("api.Добавление нового сотрудника {firstName}:{lastName}:{middleName}:{companyId}: \
                 {email}:{url}:{phone}:{birthdate}:{isActive}")
    def add_new_employee(self, first_name: str, last_name: str, middle_name: str, new_id: int, email: str, url: str, \
                         phone: int, birthdate: str ='2024-06-12T18:54:13.783Z', is_active: bool = True) -> Dict[str, Any]:
        employee = {
            "id": 0,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": new_id,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": is_active
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + "/employee", \
                             headers=my_headers, json=employee)
        return resp.json()


    @allure.step("api.Получение сотрудника по {id}")
    def get_employee_by_id(self, id: int) -> Dict[str, Any]:
        resp = requests.get(self.url + "/employee/" + str(id))
        return resp.json()


    @allure.step("api.Редактирование сотрудника {new_lastName}:{new_email}:{new_url}:{new_phone}:{new_isActive}:{id}")
    def update_employee_info(self, last_name: str, email: str, url: str, phone: int, is_active: bool, id: int) -> Dict[str, Any]:
        user_info = {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": is_active,
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + "/employee/" + str(id), headers=my_headers, json=user_info)
        return resp.json()
