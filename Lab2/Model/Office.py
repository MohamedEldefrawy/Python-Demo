class Office:
    __name = ""
    __id = 0
    __employees = []

    def __init__(self, name):
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        self.__employees = value

    def employee(self, employee_id):
        return self.__employees[employee_id]

    def fire(self, employee_id):
        selected_employee = self.employee(employee_id)
        self.__employees.remove(selected_employee)

    def hire(self, employee):
        self.__employees.append(employee)
