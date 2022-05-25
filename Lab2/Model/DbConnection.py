import mysql.connector


class DatabaseConnection:
    __db = mysql.connector.connect(
        host="localhost",
        user="modafro",
        password="12345678",
        database="python_demo"
    )

    __cursor = __db.cursor()

    @property
    def cursor(self):
        self.__cursor
