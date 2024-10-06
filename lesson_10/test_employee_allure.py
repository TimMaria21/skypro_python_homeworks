from EmployeeAPI import Employee
from EmployeeTable import EmployeeTable
import pytest
import allure

api = Employee("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")


@allure.title("Добавление нового сотрудника")
@allure.description("Тест проверяет возможность добавления новых сотрудников")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_add_new_employee():
    company_name = "school"
    descr = "klass"
    with allure.step("Создать новую компанию через БД"):
        db.create_company(company_name, descr)

    with allure.step("Получить ID новой компании через БД"):
        max_id = db.get_max_id()

    new_name = "ksenia"
    new_last_name = "Tim"
    new_email = "123qwe@mai.ru"
    id_company = max_id
    phone_number = "89173234567"
    with allure.step("Создать нового сотрудника через БД"):
        db.create_employee(new_name, new_last_name, new_email, id_company, phone_number)

    with allure.step("Получить ID нового сотрудника через БД"):
        id_employee = db.max_id_emp()

    with allure.step("Получить список сотрудников компании через ID в API"):
        list_employee = api.get_list_employee(id_company)

    with allure.step("Проверить, что поля нового сотрудника заполнены верно"):
        assert list_employee[-1]["firstName"] == new_name
        assert list_employee[-1]["phone"] == phone_number
        assert list_employee[-1]["companyId"] == id_company
        assert list_employee[-1]["lastName"] == new_last_name

    with allure.step("Удаляем компанию через БД"):
        db.delete_employee(id_employee)
    with allure.step("Удаляем сотрудника через БД"):
        db.delete_company(max_id)


@allure.title("Поиск сотрудника по id")
@allure.description("Проверка поиска сотрудника по ID")
@allure.feature("search")
@allure.severity("blocker")
def test_get_employee_by_id():
    name = "Adrenalin"
    descr = "sports club"
    with allure.step("Создать новую компанию через БД"):
        db.create_company(name, descr)

    with allure.step("Получить ID новой компании через БД"):
        max_id = db.get_max_id()

    new_name = "Rimma"
    new_last_name = "Bojko"
    new_email = "bojko1@mai.ru"
    id_company = max_id
    phone_number = "8-449-432-34-45"
    with allure.step("Создать нового сотрудника через БД"):
        db.create_employee(new_name, new_last_name, new_email, id_company, phone_number)
    id_employee = db.max_id_emp()

    with allure.step("Получить список сотрудников компании через ID в API"):
        get_info_api = api.get_employee_by_id(id_employee)

    with allure.step("Проверяем, id номер сотрудника в Апи и БД одинаковые,\
                      данные сотрудника совпадают, id компании идентичен"):
        assert get_info_api["companyId"] == id_company
        assert get_info_api["firstName"] == new_name
        assert get_info_api["phone"] == phone_number

    with allure.step("Удаляем сотрудника через БД"):
        db.delete_employee(id_employee)
    with allure.step("Удаляем компанию через БД"):
        db.delete_company(max_id)



@allure.title("Редактирование данных сотрудника")
@allure.description("Тест проверяет возможность редактирования данных сотрудника")
@allure.feature("UPDATE")
@allure.severity("blocker")
def test_change_employee_info():
    name = "New"
    descr = "user"
    with allure.step("Создать новую компанию через БД"):
        db.create_company(name, descr)
    with allure.step("Получить ID новой компании через БД"):
        max_id = db.get_max_id()

    new_name = "Rimma"
    new_last_name = "Bojko"
    new_email = "bojko1@mai.ru"
    id_company = max_id
    phone_number = "8-449-432-34-45"
    with allure.step("Создать нового сотрудника через БД"):
        db.create_employee(new_name, new_last_name, new_email, id_company, phone_number)
    id_employee = db.max_id_emp()

    with allure.step("Редактировать данные сотрудника"):
        db.edit_employee_info("Olya", "Markes", "mark1@ya.com", "+79293459987", id_company, id_employee)
    update_api = api.get_employee_by_id(id_employee)

    with allure.step("Проверить,что поля сотрудника заполнены верно и изменены"):
        assert update_api["firstName"] == "Olya"
        assert update_api["id"] == id_employee
        assert update_api["email"] == "mark1@ya.com"
        assert update_api["isActive"] == True
    
    with allure.step("Удаляем сотрудника через БД"):
        db.delete_employee(id_employee)
    with allure.step("Удаляем компанию через БД"):
        db.delete_company(max_id)



@allure.title("Удаление сотрудника по id")
@allure.description("Проверка удаления сотрудника")
@allure.feature("DELETE")
@allure.severity("blocker")
def test_delete_employee():
    name = "klab"
    descr = "bar"
    with allure.step("Создать новую компанию через БД"):
        db.create_company(name, descr)

    with allure.step("Получить ID новой компании через БД"):
        max_id = db.get_max_id()

    new_name = "Platon"
    new_last_name = "Artik"
    new_email = "art@mai.ru"
    id_company = max_id
    phone_number = "89173432117"
    with allure.step("Создать нового сотрудника через БД"):
        db.create_employee(new_name, new_last_name, new_email, id_company, phone_number)
    max_id_emp = db.max_id_emp()

    with allure.step("Удаляем сотрудника через БД"):
        db.delete_employee(max_id_emp)

    number_of_employees = api.get_list_employee(max_id)
    with allure.step("Проверить удаление сотрудника в компании"):
        assert len(number_of_employees) == 0
        
    with allure.step("Удаляем компанию через БД"):
        db.delete_company(max_id)

