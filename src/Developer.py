from Employee import Employee

class Developer(Employee):
    def __init__(self, id, name, address, base_salary, age, gender, exp_year, primary_language):
        super().__init__(id, name, address, base_salary, age, gender, exp_year)
        self.primary_language = primary_language
    
    def __str__(self):
        return f"{self.id:<4} {self.name:<12} {self.address:<20} {self.base_salary:<11} {self.age:<3} {self.gender:<6} {self.exp_year:<8} {self.primary_language:<10}"
    
    def calculateSalary(self):
        if self.exp_year < 2:
            return self.base_salary
        elif self.exp_year >= 2 and self.exp_year <= 5:
            return self.base_salary + 500000*self.exp_year
        else:
            return self.base_salary + 1000000*self.exp_year