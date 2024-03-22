from Employee import Employee

class Tester(Employee):
    def __init__(self, id, name, address, base_salary, age, gender, exp_year, type):
        super().__init__(id, name, address, base_salary, age, gender, exp_year)
        self.type = type
    
    def __str__(self):
        return f"{self.id:<4} {self.name:<12} {self.address:<20} {self.base_salary:<11} {self.age:<3} {self.gender:<6} {self.exp_year:<8} {self.type:<10}"

    def calculateSalary(self):
        if self.exp_year < 2:
            return self.base_salary
        elif self.exp_year >= 2 and self.exp_year <= 5:
            return self.base_salary + 300000*self.exp_year
        else:
            return self.base_salary + 700000*self.exp_year