from employee import Company
import pytest

api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "Scholl"
    descr = "education"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0

def test_add_new_employee():
    name = "Scholl 2126"
    descr = "education"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee("Mariya", "Timofeeva", "Alexandrovna", new_id, "qwerty@gmail.com", "url", "895434211", True)
    assert new_employee["id"] > 0
    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == "Mariya"
    assert resp[0]["lastName"] == "Timofeeva"
    assert resp[0]["phone"] == "895434211"
    assert resp[0]["isActive"] == True


def test_get_employee_by_id():
    name = "Adrenalin"  
    descr = "sports club"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee("Dina", "Pavlova", "Ivanovna", new_id, "pocz@gmail.com", "url", "89154342112", True)
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "Dina"
    assert get_info["lastName"] == "Pavlova"
    assert get_info["phone"] == "89154342112"
    assert get_info["companyId"] == new_id


def test_change_employee_info():
    name = "Knowledge is power"
    descr = "tutor"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee("Anna", "Timofeeva", "Alexandrovna", new_id, "qwerty@gmail.com", "url", "895434211", True)
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, "Ivanova", "newemeil1@mail.ru", "url", "89633211223", True)
    assert update["id"] == id_employee
    assert update["email"] == "newemeil1@mail.ru"
    assert update["isActive"] == True
    