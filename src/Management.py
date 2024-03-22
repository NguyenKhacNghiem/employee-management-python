from Connection import connection
from Account import Account
from Developer import Developer
from Tester import Tester
import locale # dùng để format number
import Logging as log # dùng ghi log

cursor = connection.cursor()

locale.setlocale(locale.LC_ALL, 'vi_VN')

class Management:
    def __init__(self, username):
        self.employees = []
        self.username = username

    def add(self):
        print("1. Developer")
        print("2. Tester")
        print("0. Back")

        while True:
            try:
                position = int(input("Choose position: "))
                break
            except:
                print("Please enter a number")
            
        if position == 0:
            return
        
        if position < 0 or position > 2:
            print("Invalid choice")
            return

        name = input("Enter name: ")
        address = input("Enter address: ")

        while True:
            try:
                base_salary = int(input("Enter base salary: "))
                break
            except:
                print("Please enter a number")

        while True:
            try:
                age = int(input("Enter age: "))
                break
            except:
                print("Please enter a number")

        gender = input("Enter gender (Male/ Female): ")
        
        while True:
            try:
                exp_year = int(input("Enter exp year: "))
                break
            except:
                print("Please enter a number")

        cursor.execute(f"select format_id({position}) from dual")
        row = cursor.fetchone()
        id = row[0]

        sql = "insert into employee values (:id, :name, :address, :base_salary, :age, :gender, :exp_year)"
        values = (id, name, address, base_salary, age, gender, exp_year)

        cursor.execute(sql, values)
        connection.commit()

        if position == 1: # For Developer
            primary_language = input("Enter primary language: ")

            sql = "insert into developer values (:id, :primary_language)"
            values = (id, primary_language)
        else:             # For Tester
            type = input("Enter type (Manual, Automation): ")

            sql = "insert into tester values (:id, :type)"
            values = (id, type)

        cursor.execute(sql, values)
        connection.commit()

        print("1 record added successfully")
        log.writeLog(self.username, f"add new employee whose id = {id}") # ghi log

    def update(self):
        self.handleView(1)
        id = input("Enter the id of an employee you want to update: ")

        cursor.execute(f"select count(*) from employee where id = '{id}'")
        row = cursor.fetchone()
        count = row[0]

        if count <= 0:
            print("Employee not found")
            return

        name = input("Enter new name: ")
        address = input("Enter new address: ")
        
        while True:
            try:
                base_salary = int(input("Enter new base salary: "))
                break
            except:
                print("Please enter a number")

        while True:
            try:
                age = int(input("Enter new age: "))
                break
            except:
                print("Please enter a number")

        gender = input("Enter new gender (Male/ Female): ")

        while True:
            try:
                exp_year = int(input("Enter new exp year: "))
                break
            except:
                print("Please enter a number")

        sql = "update employee set name = :name, address = :address, base_salary = :base_salary, age = :age, gender = :gender, exp_year = :exp_year where id = :id"
        values = (name, address, base_salary, age, gender, exp_year, id)

        cursor.execute(sql, values)
        connection.commit()

        if "D" in id: # For Developer
            primary_language = input("Enter new primary language: ")

            sql = "update developer set primary_language = :primary_language where id = :id"
            values = (primary_language, id)
        else:         # For Tester
            type = input("Enter new type (Manual, Automation): ")

            sql = "update tester set type = :type where id = :id"
            values = (type, id)
        
        cursor.execute(sql, values)
        connection.commit()

        print("1 record updated successfully")
        log.writeLog(self.username, f"update an employee whose id = {id}") # ghi log

    def delete(self):
        self.handleView(1)
        id = input("Enter the id of an employee you want to delete: ")

        cursor.execute(f"select count(*) from employee where id = '{id}'")
        row = cursor.fetchone()
        count = row[0]

        if count <= 0:
            print("Employee not found")
            return
        
        sql = f"delete from developer where id = '{id}'" if "D" in id else f"delete from tester where id = '{id}'"
        cursor.execute(sql)
        connection.commit()

        sql = f"delete from employee where id = '{id}'"
        cursor.execute(sql)
        connection.commit()

        print("1 record deleted successfully")
        log.writeLog(self.username, f"delete an employee whose id = {id}") # ghi log

    def view(self):
        while True:
            print("1. View all")
            print("2. View developer")
            print("3. View tester")
            print("0. Back")

            while True:
                try:
                    choice = int(input("Choose: "))
                    break
                except:
                    print("Please enter a number")

            if choice == 0:
                break
            elif choice == 1 or choice == 2 or choice == 3:
                self.handleView(choice)
            else:
                print("Invalid choice")

    def handleView(self, choice):
        self.employees.clear()

        if choice == 1:
            self.getAllEmployees()
        elif choice == 2:
            cursor.execute("select e.*, d.primary_language from employee e join developer d on e.id = d.id")
            rows = cursor.fetchall()
            for r in rows:
                self.employees.append(Developer(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))
        elif choice == 3:
            cursor.execute("select e.*, t.type from employee e join tester t on e.id = t.id")          
            rows = cursor.fetchall()
            for r in rows:
                self.employees.append(Tester(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))
        
        print("There are", len(self.employees), "records: ")
        print(f'{"ID":<4} {"Name":<12} {"Address":<20} {"Base Salary":<11} {"Age":<3} {"Gender":<6} {"Exp Year":<8} {"Primary Language/ Type":<10}')
        for e in self.employees:
            print(e)
        
        log.writeLog(self.username, "view employee list") # ghi log

    def search(self):
        while True:
            print("1. Search by id")
            print("2. Search by name")
            print("3. Search by address")
            print("4. Search by base_salary")
            print("5. Search by age")
            print("6. Search by gender")
            print("7. Search by primary_language (for Developer)")
            print("8. Search by type (for Tester)")
            print("0. Back")

            while True:
                try:
                    choice = int(input("Choose: "))
                    break
                except:
                    print("Please enter a number")

            if choice == 0:
                break
            elif choice == 1:
                self.handleSearch("id")
            elif choice == 2:
                self.handleSearch("name")
            elif choice == 3:
                self.handleSearch("address")
            elif choice == 4:
                self.handleSearch("base_salary")
            elif choice == 5:
                self.handleSearch("age")
            elif choice == 6:
                self.handleSearch("gender")
            elif choice == 7:
                self.handleSearch("primary_language")
            elif choice == 8:
                self.handleSearch("type")
            else:
                print("Invalid choice")

    def handleSearch(self, criteria):
        keyword = input("Enter " + criteria + ": ").lower()

        self.employees.clear()

        if criteria == "primary_language":
            cursor.execute(f"""select e.*, d.primary_language 
                               from employee e join developer d on e.id = d.id
                               where lower(d.primary_language) = '{keyword}'""")
            rows = cursor.fetchall()
            for r in rows:
                self.employees.append(Developer(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))
        elif criteria == "type":
            cursor.execute(f"""select e.*, t.type
                               from employee e join tester t on e.id = t.id
                               where lower(t.type) = '{keyword}'""")
            rows = cursor.fetchall()
            for r in rows:
                self.employees.append(Tester(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))
        else:
            cursor.execute(f"""select e.*, d.primary_language
                               from employee e join developer d on e.id = d.id
                               where lower(e.{criteria}) = '{keyword}'""")
            rows = cursor.fetchall()
            for r in rows:
                self.employees.append(Developer(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

            cursor.execute(f"""select e.*, t.type
                               from employee e join tester t on e.id = t.id
                               where lower(e.{criteria}) = '{keyword}'""")
            rows = cursor.fetchall()
            for r in rows:
                self.employees.append(Tester(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

        print("There are", len(self.employees), "records: ")
        print(f'{"ID":<4} {"Name":<12} {"Address":<20} {"Base Salary":<11} {"Age":<3} {"Gender":<6} {"Exp Year":<8} {"Primary Language/ Type":<10}')
        for e in self.employees:
            print(e)
        
        log.writeLog(self.username, "search employee") # ghi log
        
    def showSalary(self):
        self.employees.clear()

        self.getAllEmployees()

        if len(self.employees) <= 0:
            print("List is empty!")
        else:
            sum = 0

            for e in self.employees:
                sum += e.calculateSalary()
            
                formatted = locale.format_string("%d", e.calculateSalary(), grouping=True)
                print(f"{e.id} - {e.name}: {formatted}đ")
            
            avg = sum / len(self.employees)
            formatted = locale.format_string("%d", avg, grouping=True)
            print(f"Average salary: {formatted}đ")

            log.writeLog(self.username, "view calculate salary") # ghi log

    def sort(self):
        self.employees.clear()

        while True:
            print("1. Sort by name asc")
            print("2. Sort by name desc")
            print("3. Sort by age asc")
            print("4. Sort by age desc")
            print("5. Sort by base salary asc")
            print("6. Sort by base salary desc")
            print("7. Sort by exp year asc")
            print("8. Sort by exp year desc")
            print("0. Back")

            while True:
                try:
                    choice = int(input("Choose: "))
                    break
                except:
                    print("Please enter a number")
            
            if choice == 0:
                break

            if choice < 0 or choice > 8:
                print("Invalid choice")
                continue

            criteria = ""
            if choice == 1:
                criteria = "name asc"
            elif choice == 2:
                criteria = "name desc"
            elif choice == 3:
                criteria = "age asc"
            elif choice == 4:
                criteria = "age desc"
            elif choice == 5:
                criteria = "base_salary asc"
            elif choice == 6:
                criteria = "base_salary desc"
            elif choice == 7:
                criteria = "exp_year asc"
            elif choice == 8:
                criteria = "exp_year desc"

            cursor.execute(f"select e.*, d.primary_language from employee e join developer d on e.id = d.id order by e.{criteria}")
            rows = cursor.fetchall()
            for r in rows:
                self.employees.append(Developer(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

            cursor.execute(f"select e.*, t.type from employee e join tester t on e.id = t.id order by e.{criteria}")
            rows = cursor.fetchall()
            for r in rows:
                self.employees.append(Tester(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

            print("There are", len(self.employees), "records: ")
            print(f'{"ID":<4} {"Name":<12} {"Address":<20} {"Base Salary":<11} {"Age":<3} {"Gender":<6} {"Exp Year":<8} {"Primary Language/ Type":<10}')
            for e in self.employees:
                print(e)
            
            log.writeLog(self.username, "sort employee list") # ghi log

    def exportCSV(self):
        self.employees.clear()
        self.getAllEmployees()
        
        f = open("employees.csv", "w")
        
        f.write("ID, Name, Address, Base Salary, Age, Gender, Exp Year, Primary Language/ Type\n")
        for e in self.employees:
            f.write(f"{e.id}, {e.name}, {e.address}, {e.base_salary}, {e.age}, {e.gender}, {e.exp_year}, ")

            if isinstance(e, Developer):
                f.write(f"{e.primary_language}\n")
            else:
                f.write(f"{e.type}\n")

        print("Export to CSV successfully")
        f.close()

        log.writeLog(self.username, "export employee list to CSV") # ghi log

    def getAllEmployees(self):
        cursor.execute("select e.*, d.primary_language from employee e join developer d on e.id = d.id")
        rows = cursor.fetchall()
        for r in rows:
            self.employees.append(Developer(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))
            
        cursor.execute("select e.*, t.type from employee e join tester t on e.id = t.id")          
        rows = cursor.fetchall()
        for r in rows:
            self.employees.append(Tester(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

    def viewAccount(self):
        cursor.execute("select username, role from account")
        rows = cursor.fetchall()

        accounts = []
        for r in rows:
            accounts.append(Account(r[0], "********", r[1]))

        print(f'{"Username":<10} {"Password":<10} {"Role":<10}')
        for a in accounts:
            print(a)
        
        log.writeLog(self.username, "view account list") # ghi log









