import allure
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.sql import text
from sqlalchemy.engine import ResultProxy
from typing import List, Tuple, Any


class EmployeeTable():
    __scripts = {
        "select": "select * from company where deleted_at is NULL",
        "insert new": text("insert into company(\"name\",\"description\") \
                           values (:company_name, :descr)"),
        "select_by_id": text("select * from company where id = :select_id"),
        "delete by id": text("delete from company where id =:id_to_delete"),
        "get_max_id": "select MAX(id) from company",
        "max_id_emp": "select MAX(id) from employee",
        "get_employee": text('select * from employee where \
                             "company_id" = :id_company'),
        "create_employee": text(
            'insert into employee ("first_name", "last_name", \
            "email", "company_id", "phone") \
            VALUES (:new_name, :new_last_name, \
            :new_email, :id_company, :phone_number)'
        ),
        "delete_employee": text(
            'delete from employee where "id" = :to_delete_employee'
        ),
        "get_employee_by_id": text('select * from employee \
                                   where "id" = :id_employee'),
        "edit_employee_info": text(
            "UPDATE employee SET first_name = :first_name_employee, \
            last_name = :last_name_employee, email = :email_employee, \
            phone = :phone_employee, company_id = :id_company \
            WHERE id = :id_employee"
        ),
    }

    def __init__(self, connection_string: str) -> None:
        self.__db: Engine = create_engine(connection_string)


    @allure.step("БД. Получие списка компаний.")
    def get_company(self) -> list:
        """
        Получение списка компаний через отправку запроса в базу данных.
        Returns:
            list: Список компаний
        """
        query = self.__db.execute(self.__scripts["select"])
        allure.attach(str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT)
        return query.fetchall()
       

    @allure.step("БД.Создание компании {name}:{description}")
    def create_company(self, name: str, description: str) -> None:
        query: ResultProxy = self.__db.execute(self.__scripts["insert new"], company_name=name, descr=description)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)


    @allure.step("БД. Получение компании по id номеру - {id}")
    def get_company_by_id(self, id: int) -> list:
        query: ResultProxy =  self.__db.execute(self.__scripts["select_by_id"], select_id=id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()


    @allure.step("БД. Удаление компании по {id}")
    def delete_company(self, id: int) -> None:
        query: ResultProxy = self.__db.execute(self.__scripts["delete by id"], id_to_delete=id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        



    @allure.step("БД. Получение максимального {id} компании")
    def get_max_id(self) -> int:
        """Получить id номер последней созданной компании
        через отправку запроса в базу данных.

        Returns:
            int: id номер последней созданной компании
        """
        return self.__db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]


    @allure.step("БД. Получение списка сотрудников компании {company_id}")
    def get_employee(self, company_id: int) -> List[Tuple[Any]]:
        query: ResultProxy = self.__db.execute(self.__scripts["select"], id=company_id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()


    @allure.step("БД. Удаление сотрудника по {id}")
    def delete_employee(self, id: int) -> None:
        query: ResultProxy = self.__db.execute(self.__scripts['delete_employee'], to_delete_employee=id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
    


    @allure.step("БД.Создание сотрудника {first_name}:{last_name}:{middle_name}:{phone}:{email} \
                 :{birthdate}:{avatar_url}:{company_id}:{is_active}")
    def create_employee(self, first_name: str, last_name: str, middle_name: str, phone: int, email: str, \
                           birthdate: str, avatar_url: str, company_id: int, is_active: bool) -> None:
        query: ResultProxy = self.__db.execute(
            self.__scripts["create_employee"], 
            first_name=first_name, 
            last_name=last_name,
            middle_name=middle_name, 
            phone=phone, 
            email=email, 
            birthdate=birthdate,
            avatar_url=avatar_url, 
            company_id=company_id, 
            is_active=is_active)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
    
    
    @allure.step("БД. Получить информацию о сотруднике по его id номеру")
    def get_employee_by_id(self, employee_id: int) -> list:
        """Получить информацию о сотруднике по его id номеру
        через отправку запроса в базу данных

        Args:
            employee_id (int): id номер сотрудника

        Returns:
            list: список сотрудников
        """
        return self.__db.execute(
            self.__scripts["get_employee_by_id"], id_employee=employee_id
        ).fetchall()
    
       

    @allure.step("БД. Получение сотрудника с максимальным ID")
    def max_id_emp(self) -> int:
        """Получить id номер последней созданной компании
        через отправку запроса в базу данных.

        Returns:
            int: id номер последней созданной компании
        """
        return self.__db.execute(self.__scripts["max_id_emp"]).fetchall()[0][0]



    @allure.step("БД. Редактирование сотрудника {employeeId}:{new_lastName}:{new_email}:{new_url}:{new_phone}:{new_isActive}")
    def edit_employee_info(self, employeeId: int, new_lastName: str, new_email: str, new_url: \
                           str, new_phone: int, new_isActive: bool) -> None:
        query: ResultProxy = self.__db.execute(
            self.__scripts['edit_employee_info'],
            employeeId=employeeId,
            new_lastName=new_lastName,
            new_email=new_email,
            new_url=new_url,
            new_phone=new_phone,
            new_isActive=new_isActive
            )
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
