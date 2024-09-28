from Employee import Employee
from EmployeeTable import EmployeeTable
import pytest

api = Employee("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")


def test_add_new_employee():
    company_name = "school"
    descr = "klass"
    db.create_company(company_name, descr)
    max_id = db.get_max_id()
    new_name = "ksenia"
    new_last_name = "Tim"
    new_email = "123qwe@mai.ru"
    id_company = max_id
    phone_number = "89173234567"
    db.create_employee(new_name, new_last_name, \
                       new_email, id_company, phone_number)
    id_employee = db.max_id_emp()

    list_employee = api.get_list_employee(id_company)
    assert list_employee[-1]["firstName"] == new_name
    assert list_employee[-1]["phone"] == phone_number
    assert list_employee[-1]["companyId"] == id_company
    assert list_employee[-1]["lastName"] == new_last_name

    db.delete_employee(id_employee)
    db.delete_company(max_id)


def test_get_employee_by_id():
    name = "Adrenalin"
    descr = "sports club"
    db.create_company(name, descr)
    max_id = db.get_max_id()

    new_name = "Rimma"
    new_last_name = "Bojko"
    new_email = "bojko1@mai.ru"
    id_company = max_id
    phone_number = "8-449-432-34-45"
    db.create_employee(new_name, new_last_name, \
                       new_email, id_company, phone_number)
    id_employee = db.max_id_emp()
    get_info_api = api.get_employee_by_id(id_employee)
    assert get_info_api["companyId"] == id_company
    assert get_info_api["firstName"] == new_name
    assert get_info_api["phone"] == phone_number

    db.delete_employee(id_employee)
    db.delete_company(max_id)


def test_change_employee_info():
    name = "New"
    descr = "user"
    db.create_company(name, descr)
    max_id = db.get_max_id()

    new_name = "Rimma"
    new_last_name = "Bojko"
    new_email = "bojko1@mai.ru"
    id_company = max_id
    phone_number = "8-449-432-34-45"
    db.create_employee(new_name, new_last_name, \
                       new_email, id_company, phone_number)
    id_employee = db.max_id_emp()
    db.edit_employee_info("Olya", "Markes", "mark1@ya.com", \
                          "+79293459987", id_company, id_employee)
    update_api = api.get_employee_by_id(id_employee)

    assert update_api["firstName"] == "Olya"
    assert update_api["id"] == id_employee
    assert update_api["email"] == "mark1@ya.com"
    assert update_api["isActive"] == True

    db.delete_employee(id_employee)
    db.delete_company(max_id)


def test_delete_employee():
    name = "klab"
    descr = "bar"
    db.create_company(name, descr)
    max_id = db.get_max_id()
    new_name = "Platon"
    new_last_name = "Artik"
    new_email = "art@mai.ru"
    id_company = max_id
    phone_number = "89173432117"
    db.create_employee(new_name, new_last_name, \
                       new_email, id_company, phone_number)
    max_id_emp = db.max_id_emp()
    db.delete_employee(max_id_emp)

    number_of_employees = api.get_list_employee(max_id)
    assert len(number_of_employees) == 0
    db.delete_company(max_id)
