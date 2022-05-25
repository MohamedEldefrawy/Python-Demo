class Office:
    __name = ""
    __id = 0
    __employees = []

    def __init__(self, office_id, name, employees):
        self.__id = office_id
        self.__name = name
        self.__employees = employees

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def employees(self):
        return self.employees

    @employees.setter
    def employees(self, value):
        self.employees = value

    def employee(self, employee_id):
        return self.__employees[employee_id]

    def fire(self, employee_id):
        selected_employee = self.employee(employee_id)
        self.__employees.remove(selected_employee)

    def hire(self, employee):
        self.__employees.append(employee)
