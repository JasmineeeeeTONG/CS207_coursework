import sys
from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2



class BankAccount():
    
    def __init__(self, owner, accountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0 # The initial balance of a BankAccount should be 0
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception('BankAccount_withdraw Error: In %s , you are attempting to withdraw more than the current balance. \n' % self.accountType.name)
        self.balance = self.balance - amount
        print('BankAccount_withdraw Sucessful: \n In %s , current balance: %f \n' % (self.accountType.name, self.balance))
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print('BankAccount_deposit Sucessful: \n In %s , current balance: %f \n' % (self.accountType.name, self.balance))
    
    def __str__(self):
        return ('-----BankAccount-----\n owner: %s \n Accont Type: %s \n---------------------\n' % (self.owner, self.accountType.name))
    
    def __len__(self):
        return self.balance
        
        
        

class BankUser():
    
    def __init__(self, owner):
        self.owner = owner
        self.savings_account = None
        self.checking_account = None
        
    def addAccount(self, accountType):
        if accountType == AccountType.SAVINGS: # Add a savings account
            if self.savings_account != None:
                raise Exception('BankUser_addAccount Limit Error: You can have only 1 SAVINGS account. \n')
            else:
                self.savings_account = BankAccount(self.owner, AccountType.SAVINGS)
                print('BankUser_addAccount Successful: \n AccountType: SAVINGS \n')
        
        elif accountType == AccountType.CHECKING: # Add a checking account
            if self.checking_account != None:
                raise Exception('BankUser_addAccount Limit Error: You can have only 1 CHECKING account. \n')
            else:
                self.checking_account = BankAccount(self.owner, AccountType.CHECKING)
                print('BankUser_addAccount Successful: \n AccountType: CHECKING \n')
         
        else: # Add some other non-specified type of account. Exception raised.
            raise Exception('BankUser_addAccount Type Error: You can add either a SAVINGS or CHECKING account. \n')
    
    
    def getBalance(self, accountType):
        if accountType == AccountType.SAVINGS: # Get balance of the savings account
            if self.savings_account != None:
                print('BankUser_getBalance: \n In %s , current balance: %f \n' % (accountType.name, self.savings_account.balance))
                return self.savings_account.balance
            else:
                raise Exception('BankUser_getBalance Error: You do not have a SAVINGS account yet. \n')
        
        elif accountType == AccountType.CHECKING: # Get balance of the checking account
            if self.checking_account != None:
                print('BankUser_getBalance: \n In %s , current balance: %f \n' % (accountType.name, self.checking_account.balance))
                return self.checking_account.balance
            else:
                raise Exception('BankUser_getBalance Error: You do not have a CHECKING account yet. \n')
        
        else: # Get balance of some other non-specified type of account. Exception raised.
            raise Exception('BankUser_getBalance Type Error: You can get balance from either your SAVINGS or CHECKING account. \n')
     
    
    def deposit(self, accountType, amount):
        if accountType == AccountType.SAVINGS: # Deposit to the savings account
            if self.savings_account != None:
                self.savings_account.deposit(amount)
            else:
                raise Exception('BankUser_deposit Error: You do not have a SAVINGS account yet. \n')
        elif accountType == AccountType.CHECKING: # Deposit to the checking account
            if self.checking_account != None:
                self.checking_account.deposit(amount)
            else:
                raise Exception('BankUser_deposit Error: You do not have a CHECKING account yet. \n')
        else: # Deposit to some other non-specified type of account. Exception raised.
            raise Exception('BankUser_deposit Type Error: You can deposit to either your SAVINGS or CHECKING account. \n')
    
    
    def withdraw(self, accountType, amount):
        if accountType == AccountType.SAVINGS: # Withdraw from the savings account
            if self.savings_account != None:
                self.savings_account.withdraw(amount)
            else:
                raise Exception('BankUser_withdraw Error: You do not have a SAVINGS account yet. \n')
        elif accountType == AccountType.CHECKING: # Withdraw from the checking account
            if self.checking_account != None:
                self.checking_account.withdraw(amount)
            else:
                raise Exception('BankUser_withdraw Error: You do not have a CHECKING account yet. \n')
        else: # Withdraw from some other non-specified type of account. Exception raised.
            raise Exception('BankUser_withdraw Type Error: You can withdraw from either your SAVINGS or CHECKING account. \n')
    
    def __str__(self):
        description = '-----BankUser-----\n owner: %s \n' % self.owner
        if self.savings_account != None:
            description += ' SAVINGS current balance: %f \n' % self.savings_account.balance
        if self.checking_account != None:
            description += ' CHECKING current balance: %f \n' % self.checking_account.balance
        description += '-------------------\n'
        return description
        



def ATMSession(bankUser):
    def Interface():
        option = input('Enter Option: \n1)Exit \n2)Create Account \n3)Check Balance \n4)Deposit \n5)Withdraw \n')
        while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
            option = input('Invalid Input... \nEnter option: \n1)Exit \n2)Create Account \n3)Check Balance \n4)Deposit \n5)Withdraw \n')
        
        if option == '1':
            print('=> Exiting ATMSession...')
            sys.exit()
        
        # Option 2, 3, 4, 5
        account_option = input('Enter option: \n1)Checking \n2)Savings \n')
        while account_option != '1' and account_option != '2':
            account_option = input('Invalid Input... \nEnter option: \n1)Checking \n2)Savings \n')
        
        if account_option == '1':
            accountType = (AccountType.CHECKING)
        elif account_option == '2':
            accountType = (AccountType.SAVINGS)
        
        if option == '2': # Create Account
            try:
                bankUser.addAccount(accountType)
            except Exception as err:
                print('[Error Msg] '+str(err))
            
        if option == '3': # Check Balance
            try:
                bankUser.getBalance(accountType)
            except Exception as err:
                print('[Error Msg] '+str(err))
        
        if option == '4': # Deposit
            amount = input('Enter Integer Amount, Cannot Be Negative: \n')
            while int(amount) < 0:
                amount = input('Invalid Input... \nEnter Integer Amount, Cannot Be Negative: \n')
            try:
                bankUser.deposit(accountType, int(amount))
            except Exception as err:
                print('[Error Msg] '+str(err))
            
        if option == '5': # Withdraw
            amount = input('Enter Integer Amount, Cannot Be Negative: \n')
            while int(amount) < 0:
                amount = input('Invalid Input... \nEnter Integer Amount, Cannot Be Negative: \n')
            try:
                bankUser.withdraw(accountType, int(amount))
            except Exception as err:
                print('[Error Msg] '+str(err))
        
        Interface() # Show the main interface again until the user hit 1 for 1)Exit
        
    return Interface