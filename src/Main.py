from Management import Management # from file nào import cái gì đó (ở đây là Class)
import Login as login
import Logging as log # dùng ghi log

def main():
    account = login.loginMenu()
    username = account[0]
    role = account[1]

    management = Management(username)
    
    while True:
        print("*********** EMPLOYEE MANAGEMENT ***********")
        print("***   1. Add new employee (for admin)   ***")
        print("***   2. Update employee (for admin)    ***")
        print("***   3. Delete employee (for admin)    ***")
        print("***   4. View employee                  ***")
        print("***   5. Search employee                ***")
        print("***   6. Calculate salary (for admin)   ***")
        print("***   7. Sort list                      ***")
        print("***   8. Export data to CSV             ***")
        print("***   9. View account (for admin)       ***")
        print("***   0. Exit                           ***")
        print("*******************************************")

        while True:
            try:
                choice = int(input("Choose: "))
                break
            except:
                print("Please enter a number")
        
        if choice == 0:
            log.writeLog(username, "loged out")
            print("Bye!")
            break
        elif choice == 1:
            if role == "admin":
                management.add()
            else:
                print("You are not admin!")
        elif choice == 2:
            if role == "admin":
                management.update()
            else:
                print("You are not admin!")
        elif choice == 3:
            if role == "admin":
                management.delete()
            else:
                print("You are not admin!")
        elif choice == 4:
            management.view()
        elif choice == 5:
            management.search()
        elif choice == 6:
            if role == "admin":
                management.showSalary()
            else:
                print("You are not admin!")
        elif choice == 7:
            management.sort()
        elif choice == 8:
            management.exportCSV()
        elif choice == 9:
            if role == "admin":
                management.viewAccount()
            else:
                print("You are not admin!")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

























