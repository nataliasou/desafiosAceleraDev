from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8

    @abstractmethod
    def calc_bonus(self):
        pass

    @abstractmethod
    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary*0.15

    def get_hours(self):
        return self.hours

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, departamento):
        self.__departament.name = departamento


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def get_sales(self):
        return self.__sales

    def put_sales(self, add_sale):
        self.__sales = add_sale + self.__sales

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, departamento):
        self.__departament.name = departamento

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_hours(self):
        return self.hours
