class Person:
    __full_name = ""
    __money = 0
    __sleep_mood = ""
    __health_rate = 0

    def __init__(self, full_name, money, sleep_mode, health_rate):
        self.__full_name = full_name
        self.__money = money
        self.__sleep_mood = sleep_mode
        self.__health_rate = health_rate

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = full_name

    @property
    def money(self):
        return self.money

    @money.setter
    def money(self, value):
        self.money = value

    @property
    def sleep_mood(self):
        return self.__sleep_mood

    @sleep_mood.setter
    def sleep_mood(self, value):
        self.__sleep_mood = value

    @property
    def health_rate(self):
        return self.__health_rate

    @health_rate.setter
    def health_rate(self, value):
        if 0 < value < 100:
            self.__health_rate = value
        else:
            print("Heart rate must be between 0 and 100")

    @health_rate.deleter
    def health_rate(self):
        pass

    def sleep(self, hours):
        if hours < 7:
            self.__sleep_mood = "tired"
            print(f"{self.full_name} is {self.__sleep_mood}")
        elif hours > 7:
            self.__sleep_mood = "lazy"
            print(f"{self.full_name} is {self.__sleep_mood}")
        else:
            self.__sleep_mood = "happy"
            print(f"{self.full_name} is {self.__sleep_mood}")

    def eat(self, meals):
        if meals == 1:
            self.__health_rate = 50
            print(f"{self.full_name} =  {self.__health_rate}")
        elif meals == 75:
            self.__health_rate = 50
            print(f"{self.full_name} =  {self.__health_rate}")
        elif meals == 3:
            self.__health_rate = 100
            print(f"{self.full_name} =  {self.__health_rate}")

    def buy(self, items):
        while items > 0:
            self.__money -= 10
