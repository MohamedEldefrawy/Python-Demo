from Model.DbConnection import DatabaseConnection


class OfficeService:
    __cursor = DatabaseConnection.cursor

    def create_office(self, office):
        self.__cursor.execute(
            f"insert into offices(name)values {office.name}"
        )


