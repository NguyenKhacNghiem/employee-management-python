from Connection import connection
import bcrypt
import Logging as log

cursor = connection.cursor()

def loginMenu():
    while True:
        print("******* LOGIN *******")
        username = input("Username: ")
        password = input("Password: ")

        cursor.execute(f"select password, role from account where username = '{username}'")
        row = cursor.fetchone()

        if row == None:
            print("Username or password is incorrect")
            continue
            
        hashedPassword = row[0]
        check = bcrypt.checkpw(password.encode('utf-8'), hashedPassword.encode('utf-8'))

        if check:
            print("Welcome:", username)

            # Ghi log
            log.writeLog(username, "loged in")

            account = (username, row[1]) # row[1] là role
            return account