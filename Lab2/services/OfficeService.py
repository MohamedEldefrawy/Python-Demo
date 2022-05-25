from Model.DbConnection import DatabaseConnection


class OfficeService:
    __cursor = DatabaseConnection.cursor

    def create_office(self, office):
        self.__cursor.execute(
            f"insert into offices(name) values ({office.name})"
        )

    def get_offices(self):
        self.__cursor.execute(
            f"select * from offices"
        )

    def get_office(self, office_name):
        self.__cursor.execute(
            f"select * from offices where name = {office_name}"
        )

    def update_office(self, office):
        self.__cursor.execute(
            f"update offices set name = {office.name} where id =  {office.id}"
        )

    def remove_office(self, office_id):
        self.__cursor.execute(
            f"delete from offices where id= {office_id}"
        )

    def get_employees(self, office_id):
        self.__cursor.execute(
            f"select * from employees e inner join offices o on e.office_id = o.id where office_id = {office_id}"
        )
