class Bank:
    """Simple Bank Class"""
    def __init__(self, name, address, city, state, zipcode):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def bankInfo(self):
        print(f"{self.name} \n{self.address}, {self.city}, {self.state} {self.zipcode} ")   


class BankAccount:
    """Simple BankAccount Class which takes in important customer information"""
    def __init__(self,customername, accountnumber, saving_account, checking_account):
        self.customername = customername
        self.accountnumber = accountnumber
        self.saving_account= saving_account
        self.checking_account = checking_account
        self.checkingLineOfCredit = 500
    
    # Function allows customer to deposit integer dollar amount
    def deposit(self,amount):
        choice = input("1 Checking\n2 Savings\nSelection: ")
        if(choice == 1):
            print(f"Depositing {amount} into checking...\nThank you for you continued support!")
            self.checking_account += amount
        if(choice == 2):
            print(f"Depositing {amount} into savings...\nThank you for you continued support!")
            self.saving_account += amount

    # Function allows customer to withdraw integer dollar amount
    #  as long as funds are on available
    def withdraw(self,amount):
        choice = ''
        while(choice != '1' and choice != '2'):
            choice = input("1 Checking\n2 Savings\nSelection:  ")
        else:
            if(choice == '1'):
                # Customer can withdraw from checking as long as funds don't exceed checking line of credit
                if amount > self.checking_account + self.checkingLineOfCredit:
                    print(f"You only have {self.checking_account} at this time!")
                else:
                    self.checking_account -= amount
            elif(choice == '2'):
                if amount > self.saving_account:
                    print(f"You only have {self.saving_account} at this time!")
                else:
                    self.saving_account -= amount

    def accInfo(self):
        print(f"Customer Name: {self.customername} Account Number: {self.accountnumber}\nChecking Account Balance: {self.checking_account}\nSaving Account Balance: {self.saving_account} ")

class Loan(BankAccount):
    def __init__(self,customername, accountnumber, saving_account, checking_account):
        super().__init__(customername, accountnumber, saving_account, checking_account)
    
    def application(self):
       print("1.Car\n2.Boat\n3.Personal\n4.Home")

acc1 = BankAccount("Amani Kayin Muller",7068990,10000,431.50)

acc1.withdraw(11000)
