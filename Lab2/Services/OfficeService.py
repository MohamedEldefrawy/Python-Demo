from Model.DbConnection import DatabaseConnection


class OfficeService:
    __db = DatabaseConnection.db

    def create_office(self, office):
        __cursor = self.__db.cursor()
        __cursor.execute(
            f"insert into offices(name) values ('{office.name}')"
        )
        result = self.__db.commit()
        return result

    def get_offices(self):
        __cursor = self.__db.cursor()
        __cursor.execute(
            f"select * from offices"
        )
        result = __cursor.fetchall()
        return result

    def get_office(self, office_name):
        __cursor = self.__db.cursor()
        __cursor.execute(
            f"select * from offices where name = {office_name}"
        )

        result = self.__cursor.fetchall()
        return result

    def update_office(self, office):
        __cursor = self.__db.cursor()

        __cursor.execute(
            f"update offices set name = {office.name} where id =  {office.id}"
        )

    def remove_office(self, office_id):
        __cursor = self.__db.cursor()
        __cursor.execute(
            f"delete from offices where id= {office_id}"
        )
        result = self.__db.commit()
        return result

    def get_employees(self, office_id):
        __cursor = self.__db.cursor()
        __cursor.execute(
            f"select * from employees e inner join offices o on e.office_id = o.id where office_id = {office_id}"
        )
