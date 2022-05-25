from Model.DbConnection import DatabaseConnection


class EmployeeService:
    __cursor = DatabaseConnection.cursor

    def create_employee(self, employee):
        self.__cursor.execute(
            "insert into employees(full_name, money, sleep_mood, heart_rate, work_mood, email, salary, is_manager, office_id)"
            f"values ({employee.name, employee.money, employee.sleep_mood, employee.health_rate, employee.work_mood, employee.email, employee.salary, employee.is_manager, employee.office_id})"
        )

    def get_employees(self):
        self.__cursor.execute(
            f"select * from employees"
        )

    def get_employee(self, employee_id):
        self.__cursor.execute(
            f"select * from employees where id = {employee_id}"
        )
