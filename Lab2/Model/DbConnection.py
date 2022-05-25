import mysql.connector


class DatabaseConnection:
    __db = mysql.connector.connect(
        host="localhost",
        user="modafro",
        password="12345678",
        database="python_demo"
    )

    @property
    def db(self):
        return DatabaseConnection.__db
