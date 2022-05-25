import re

from Person import Person


class Employee(Person):
    __id = 0
    __email = ""
    --work_mood = ""
    __salary = 0
    __is_manager = False
    __office_id = 0

    @property
    def office_id(self):
        return self.office_id

    @office_id.setter
    def office_id(self, value):
        self.office_id = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def email(self):
        return self.email

    @email.setter
    def id(self, value):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, value):
            self.__email = value
        else:
            print("Invalid Email")

    @property
    def work_mood(self):
        return self.work_mood

    @work_mood.setter
    def id(self, value):
        self.work_mood = value

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def id(self, value):
        if value >= 1000:
            self.salary = value
        else:
            print("salary must be at least 1000")

    @property
    def is_manager(self):
        return self.is_manager

    @is_manager.setter
    def is_manager(self, value):
        self.is_manager = value


@property
def is_manager(self):
    return self.is_manager


@is_manager.setter
def is_manager(self, value):
    self.is_manager = value


def __init__(self, full_name, money, sleep_mode, health_rate, id, email, word_mood, salary, is_manager):
    super().__init__(full_name, money, sleep_mode, health_rate)
    self.__id = id
    self.__email = email
    self.work_mood = word_mood
    self.__salary = salary
    self.__is_manager = is_manager


@staticmethod
def send_email(to, subject, body, receiver):
    with open('email.txt', 'a') as email:
        email.write(f"""
             to : {to}
             subject : {subject}
             body : {body}
             receiver name : {receiver}
             ==========================================    
            """)


def work(self, hours):
    if hours < 8:
        print(f"{self.full_name} is lazy")
    elif hours > 7:
        print(f"{self.full_name} is tired")
    else:
        print(f"{self.full_name} is happy")
