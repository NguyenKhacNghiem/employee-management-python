from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name, address, base_salary, age, gender, exp_year):
        self.id = id
        self.name = name
        self.address = address
        self.base_salary = base_salary
        self.age = age
        self.gender = gender
        self.exp_year = exp_year

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def calculateSalary(self):
        pass