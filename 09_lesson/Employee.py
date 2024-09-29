import requests


class Employee:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='leonardo', password='leads'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + "/auth/login", json=creds)
        return resp.json()["userToken"]

    def create_company(self, name, descr):
        company = {
            "name": name,
            "description": descr
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + "/company", json=company, headers=my_headers)
        return resp.json()

    def get_list_employee(self, id):
        my_params = {
            "company": id
        }
        resp = requests.get(self.url + "/employee", params=my_params)
        return resp.json()

    def add_new_employee(self, first_name, last_name, \
                         middle_name, new_id, email, url, phone, is_active):
        employee = {
            "id": 0,
            "firstName": first_name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": new_id,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": "2024-06-12T18:54:13.783Z",
            "isActive": is_active
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + "/employee", \
                             headers=my_headers, json=employee)
        return resp.json()

    def get_employee_by_id(self, id):
        resp = requests.get(self.url + "/employee/" + str(id))
        return resp.json()

    def update_employee_info(self, id, last_name, \
                             email, url, phone, is_active):
        user_info = {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": is_active,
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + "/employee/" + str(id), \
                              headers=my_headers, json=user_info)
        return resp.json()
