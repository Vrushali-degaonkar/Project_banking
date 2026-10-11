class Bank:
    database = {"Jake":[123,0]}
    curr_user = None
    is_logged_in = False
    curr_balance = 0

    def __init__(self):
        print('Press 1 for register')
        print('Press 2 for balance enquiry')
        print('Press 3 for deposite')
        print('Press 4 for withdrawl')
        print('Press 5 for bank statement')
        print('Press 6 for login')
        choice = int(input("enter the choice: "))
        if choice == 1:
            self.register()
        if choice == 2:
            self.check_balance()
        if choice == 3:
            amt = int(input("enter the amount for deposite:"))
            self.deposite(amt=amt)
        if choice == 4:
            amt = int(input("enter the amount for withdraw:"))
            self.withdrawl(amt=amt)
        if choice == 5:
            self.bank_statement()
        if choice == 6:
            self.login()


    def login(self):
        username = input("please enter your username here: ")
        password = int(input("please enter your password here: "))

        if username in self.database and password == self.database[username][0]:
            print('---------------------------------------')
            print('Login Successful!')
            print('---------------------------------------')
            self.curr_user = username
            self.is_logged_in = True
            print('---------------------------------------')
            print(f'Current user =====> {self.curr_user}')
            print('---------------------------------------')
        else:
            print('---------------------------------------')
            print('Username or password is invalid! Please try again!')
            print('---------------------------------------')
            self.login()
            print('---------------------------------------')

        self.__init__()

    def register(self):
        username = input("Enter new username")
        if username in self.database:
            print('---------------------')
            print('Username already exists!')
            print('-------------------------')
        else:
            password = int(input('enter new password:   '))
            self.database[username] = [password, 0]
            print('---------------------')
            print("Registration successfully....!")
        self.__init__()


    def check_balance(self):
        if self.is_logged_in == True:

            print('---------------------------------------')
            #print(f'Your current balance is=======> {self.curr_balance}')
            print(f'User =====> {self.curr_user}')
            print(f'Your current balance is ====> {self.database[self.curr_user][1]}')
            print('---------------------------------------')
            self.__init__()
        else:
            print('---------------------------------------')
            print('Please login first')
            print('---------------------------------------')
            self.__init__()



    def deposite(self,amt):
        if self.is_logged_in == True:
            #self.curr_balance+=amt
            self.database[self.curr_user][1] -= amt
            balance = self.database[self.curr_user][1] 
            print('---------------------------------------')
            print(f'{amt} deposited successfully!')
            print(f'Your current balance is=======> {balance}')
            print('---------------------------------------')
            self.__init__()
        else:
            print('---------------------------------------')
            print('Please login first')
            print('---------------------------------------')
            self.__init__()

            
    def withdrawl(self,amt):
        
        if self.is_logged_in == True:
            #self.curr_balance-=amt
            self.database[self.curr_user][1] += amt
            balance = self.database[self.curr_user][1] 
            print('---------------------------------------')
            print(f'{amt} withdrawn successfully!')
            #print(f'Your current balance is=======> {self.curr_balance}')
            print(f'Your current balance is=======> {balance}')
            print('---------------------------------------')
            self.__init__()
        else:
            print('---------------------------------------')
            print('Please login first')
            print('---------------------------------------')
            self.__init__()

    
    def bank_statement(self):
        if self.is_logged_in == True:

            print('---------------------------------------')
            print(f'Your statement is with balance=======> {self.database[self.curr_user][1]}')
            print('---------------------------------------')
            self.__init__()
        else:
            print('---------------------------------------')
            print('Please login first')
            print('---------------------------------------')
            self.__init__()


ob1 = Bank()

