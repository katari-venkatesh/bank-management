from random import randint
import mysql.connector

# MySQL Database Connection Details

conn = mysql.connector.connect(host='localhost', database='bank', user='root', password='Venky@2003')

# Establishing a connection to the MySQL database
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS accounts (account_number INT PRIMARY KEY, customer_name VARCHAR(255), age INT, mobile_number BIGINT, balance Float(10))")
conn.commit()

print("WELCOME TO Venky's BANK..")
account_num = randint(11111, 99999)
cursor.execute("SELECT account_number FROM accounts")
result = cursor.fetchall()
list_account_numbers = [row[0] for row in result]
cursor.execute("select * from accounts")
info = cursor.fetchall()


class BankingProcess():
    def create_account(self):
        global balance
        customer_name = input("enter your name:-")
        age = int(input("enter your age(above 18):-"))
        mobile_number = int(input("enter your mobile number(should be 10 digits):-"))
        if customer_name.isalpha():
            balance = float(input("enter initial deposit amount:-"))

            # Inserting data into the MySQL database
            cursor.execute(
                "INSERT INTO accounts (account_number, customer_name, age, mobile_number, balance) VALUES (%s, %s, %s, %s, %s)",
                (account_num, customer_name, age, mobile_number, balance))

            conn.commit()

            print("\nyour account has been created successfully...!")
            print("your account number:-", account_num)
        else:
            print("check your name")

    def access_existing_account(self):
        def withdraw():
            account_number = int(input("enter your account number:-"))
            for i in range(len(info)):
                if (account_number == info[i][0]):
                    amount = float(input("enter how much amount you want to withdraw:-"))
                    if (amount < info[i][4]):
                        print("\nyour Amount withdraw successfully..!")
                        balance = info[i][4] - amount

                    # Updating the balance in the MySQL database
                    cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s",
                                   (balance, account_number))
                    conn.commit()

                    print("\nyour available balance:-", balance)
                    break
            else:
                print("your account number is invalid")

        def deposit():
            account_number = int(input("enter your account number:-"))
            for i in range(len(info)):
                if (account_number == info[i][0]):
                    amount = float(input("enter how much amount you want to deposit:-"))
                    print("\n your Amount is successfully deposited.")
                    balance = info[i][4] + amount

                    # Updating the balance in the MySQL database
                    cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s",
                                   (balance, account_number))
                    conn.commit()

                    print("\nyour available balance:-", balance)
                    break
            else:
                print("your account number is invalid")

        def display_available_balance():
            account_number = int(input("enter your account number:-"))
            for i in range(len(info)):
                if (account_number == info[i][0]):
                    balance = info[i][4]
                    print("your available balance:-", balance)
                    break
            else:
                print("your account number is invalid")

        def to_go_previous_menu():
            obj1.bank()

        def menu():
            print("\n1.withdraw")
            print("2.deposit")
            print("3.display available balance")
            print("4.go to previous menu")
            choice1 = int(input("enter your choice(1,2,3,4):-"))
            if choice1 == 1:
                withdraw()
                quit()
            elif choice1 == 2:
                deposit()
                quit()
            elif choice1 == 3:
                display_available_balance()
                quit()
            else:
                to_go_previous_menu()
                obj1.bank()

        menu()


class BankStatement():
    def bank(self):
        print("1.validating user account")
        print("2.exit")
        choice = int(input("enter your choice(1,2):-"))
        if (choice == 1):
            input_user = input("do you have an account in this bank(yes/no):-").lower()
            if (input_user == 'no'):
                obj2.create_account()
                quit()
            else:
                obj2.access_existing_account()
                obj1.bank()
        else:
            print("Thanks for visiting..")
            quit()


# Creating 'accounts' table in MySQL database if it doesn't exist

obj1 = BankStatement()
obj2 = BankingProcess()
obj1.bank()
