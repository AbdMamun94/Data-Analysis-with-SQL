import sys
from dbhelper import DBhelper
class Flipkart:

    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):

        users_info_input= input(""" 
        1.Enter 1 to register
        2.Enter 2 to login
        3.Anything else to leave
        """)

        if users_info_input == "1":
            self.register()
        elif users_info_input == "2":
            self.login()
        else:
            sys.exit(1000)

    def register(Self):
        name = input("Enter the name:")
        email = input("Enter the email:")
        password = input("Enter the password:")

        response = Self.db.register(name,email,password)

        if response :
            print("Registration Successful")
        else:
            print("Register failed")
        Self.menu()

    def login(self):
        email = input("Enter email:")
        password = input("Enter password:")

        self.db.search(email,password)

obj = Flipkart()