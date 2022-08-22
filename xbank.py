
'''     BANK MANAGEMENT SYSTEM      '''
import mysql.connector as c

class bank:

    con = c.connect(host='localhost',
                    user='root',
                    password='admin123',
                    )
    cur = con.cursor()

    @staticmethod
    def create_database():  #func to create a database
        bank.cur.execute("create database xbank")
        bank.cur.execute("use xbank")
        bank.cur.execute("create table user(name varchar(30), age int, address varchar(50), account varchar(20), amount int)")
        bank.con.commit()

'''             PLL STARTS HERE            '''
ob=bank()
if ob.con. is_connected():  #check if the connection is connected or not.
    print("connected with database.")
else:
    print("not connected with database.")

try:    #check if the func is already exists or not.
    ob.create_database()    #calling function to create a database
except: pass
bank.cur.execute("use xbank")
print("********** WELCOME TO THE XBANK **********")
while True:
    print(">>> Data Base <<<")
    ch = input("1 - OPEN ACCOUNT\n2 - CASH DEPOSIT \n3 - CASH WITHDRAWAL\n4 - ACCOUNT DETAILS\n0 - EXIT\nENTER YOUR CHOICE:")
    if ch == '1':   # open account
        name = input("enter the name:")
        age = int(input("enter the age:"))
        address = input("enter the address:")
        account = input("enter the account no:")
        amount = 0
        bank.cur.execute(f"insert into user values('{name}', {age}, '{address}', '{account}', {amount})")
        bank.con.commit()
        print("DETAILS ADDED SUCCESSFULLY!")

    elif ch == '2':     #cash deposite
        ac = input("enter the account no:")
        bank.cur.execute(f"select amount from user where account = {ac}")
        data = bank.cur.fetchone()  #getting the amount in variable
        data = list(data)   #convering into list type
        print("AVAIABLE BALANCE=",data[0])
        amount = int(input("enter the amount:"))    #amount to be deposit
        amount = amount + data[0] # entered amount +  previous balance
        bank.cur.execute(f"update user set amount = {amount} where account = {ac}")    #update the new balance.
        bank.con.commit()
        print("CASH DEPOSITED SUCCESSFULLY!")

        ''' SHOW AVAILABLE BALANCE'''
        bank.cur.execute(f"select amount from user where account = {ac}")
        data = bank.cur.fetchone()  #getting the amount in variable
        data = list(data)   #convering into list type
        print("AVAIABLE BALANCE=",data[0])

    elif ch == '3':
        ac = input("enter the account no:")
        bank.cur.execute(f"select amount from user where account = {ac}")
        data = bank.cur.fetchone()  #getting the amount in variable
        data = list(data)   #convering into list type
        print("AVAIABLE BALANCE=",data[0])
        amount = int(input("enter the amount for withdrawal:"))    #amount to be deposit
        amount = data[0] - amount # previous balance - entered amount
        bank.cur.execute(f"update user set amount = {amount} where account = {ac}")    #update the new balance.
        bank.con.commit()

        ''' SHOW AVAILABLE BALANCE'''
        bank.cur.execute(f"select amount from user where account = {ac}")
        data = bank.cur.fetchone()  #getting the amount in variable
        data = list(data)   #convering into list type
        print("AVAIABLE BALANCE=",data[0])
        print("PLZ TAKE YOUR CASH!")

    elif ch == '4':     #to fetch account details!
        ac = input("enter the account no:")
        bank.cur.execute(f"select * from user where account = {ac}")
        data = bank.cur.fetchone()  #getting the amount in variable
        print("NAME\t\t\tAGE\t\t\tADDRESS\t\t\tACCOUNT\t\t\tBALANCE\n")
        print(f"'{data[0]}'\t\t\t{data[1]}\t\t\t'{data[2]}'\t\t\t'{data[3]}'\t\t\t{data[4]}")
        print("\n\n\n")


    elif ch == '0':
        print("Thank you for using XBANK App!")
        bank.con.close()
        break

    else:
        print("enter the correct choice")
'''             PLL ENDS HERE               '''












