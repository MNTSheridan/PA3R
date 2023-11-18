class Account:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self._accountNumber = accountNumber 
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance
    
    #getters
    def getAccountNumber(self):
        return self._accountNumber
    def getAccountHolderName(self):
        return self._accountHolderName
    def getRateOfInterest(self):
        return self._rateOfInterest
    def getCurrentBalance(self):
        return self._currentBalance
    #setters
    def setAccountNumber(self, accountNumber):
        self._accountNumber = accountNumber
    def setAccountHolderName(self, accountHolderName):
        self._accountHolderName = accountHolderName
    def setRateOfInterest(self, rateOfInterest):
        self._rateOfInterest = rateOfInterest
    def setCurrentBalance(self, currentBalance):
        self._currentBalance = currentBalance

    def deposit(self, amount):
        try:
            amount = int(amount)
            if amount > 0:
                print(f"${amount} has been added to your account.")
                self.setCurrentBalance(self.getCurrentBalance() + amount)
            elif amount < 0:
                errorMessage = '''
                Negative value inputted, try again.\n
                How much would you like to deposit?\n
                '''
                depositAmount = int(input(errorMessage))
                self.deposit(depositAmount)    
            else:
                errorMessage = '''
                Invalid value inputted, try again.\n
                How much would you like to deposit?\n
                '''
                depositAmount = int(input(errorMessage))
                self.deposit(depositAmount)       

        except ValueError:
            errorMessage = '''
            Invalid value inputted, try again.\n
            How much would you like to deposit?\n
            '''
            depositAmount = int(input(errorMessage))
            self.deposit(depositAmount)

    def withdraw(self, amount):
        try:
            amount = int(amount)
            if amount > 0 and amount < self._currentBalance:
                print(f"${amount} has been withdrawn from your account.")
                self.setCurrentBalance(self.getCurrentBalance() - amount)
            elif amount < 0:
                errorMessage = '''
                Negative value inputted, try again.\n
                How much would you like to withdraw?\n
                '''
                withdrawAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount)  
            elif amount > self._currentBalance:
                errorMessage = '''
                Value inputted is larger than account balance, try again.\n
                How much would you like to withdraw?\n
                '''
                depositAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount)  
            else:
                errorMessage = '''
                Invalid value inputted, try again.\n
                How much would you like to withdraw?\n
                '''
                withdrawAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount)       

        except ValueError:
            errorMessage = '''
            Invalid value inputted, try again.\n
            How much would you like to withdraw?\n
            '''
            withdrawAmount = int(input(errorMessage))
            self.withdraw(withdrawAmount)        

class Bank:


    def __init__(self, bankName):
        self.bankName = bankName
        self.accounts =  accounts = [ChequingAccount(101, "John Smith", 2, 10, -200), 
                        SavingsAccount(102, "John Smith", 2, 200, 200), 
                        ChequingAccount(103, "Joe Smith", 2, 10, -200)
                                                        ]
    
    def openAccount(self):
        choiceMessage = '''
        Which account would you like to have?
        1. Chequing account.
        2. Savings account.
        '''
        try:
            accountType = int(input(choiceMessage))
        except ValueError:
            errorMessage = '''
            Invalid input, to pick choose a number.
            '''    
            self.openAccount()
        newAccount = ChequingAccount(101, "Default Assignment", 2, 0, -200) if accountType == 1 else SavingsAccount(101, "Default Assignment", 2, 0, 200) if accountType == 2 else None
        
        name = input("What is your name?\n")
        newAccount.setAccountHolderName(name)

        #account has been set up
        self.accounts.append(newAccount)
        Application().showAccountMenu(newAccount)


    def searchAccount(self):
        try:
            accountID = int(input("What is the account id?\n"))
        except ValueError:
            accountID = int(input("Invalid input, please type in an integer value. What is the account id?"))

        for account in self.accounts:
            if accountID == account.getAccountNumber():
                if isinstance(accountID, ChequingAccount):
                    accountInfoMessage = f'''
                    ChequingAccount Found:
                    Name: {account.getAccountHolderName()}
                    '''
                    print(accountInfoMessage)
                elif isinstance(accountID, SavingsAccount):
                    accountInfoMessage = f'''
                    Savings Account Found:
                    Name: {account.getAccountHolderName()}
                    '''
                    print(accountInfoMessage)
                
                Application().showAccountMenu(account)
                break
        else:
            print("Account is not found.")
        

class Application:

    def showMainMenu(self, bank):
        while True:
            menuMessage = f'''
            Banking System of {bank.bankName} Application Menu:\n
            1. Select Account.\n
            2. Open Account.\n
            3. Exit.\n
            '''
            try:
                choice = int(input(menuMessage))
            except ValueError:
                print("Invalid selection, try again.")
                choice = int(input(menuMessage))
            if choice == 1:
                bank.searchAccount()
                break
            elif choice == 2:
                bank.openAccount()
                break
            elif choice == 3:
                print("Now closing application.")
                break
            else:
                pass
        


    def showAccountMenu(self, account):
        while True:
            menuMessage = f'''
            Banking Account of {account.getAccountHolderName()} Application Account Menu:\n
            Interest rate: {account.getRateOfInterest()}%\n

            
            1. Check Balance:\n
            2. Deposit.\n
            3. Withdraw.\n
            4. Exit Account.
            '''
            try:
                choice = int(input(menuMessage))
            except ValueError:
                print("Invalid selection, try again.")
                choice = int(input(menuMessage))
            if choice == 1:
                print(f"Your balance: ${account.getCurrentBalance()}")
            elif choice == 2:
                amount = input("How much do you want to deposit?\n")
                account.deposit(amount)
            elif choice == 3:
                amount = input("How much do you want to withdraw?\n")
                account.withdraw(amount)
            elif choice == 4:
                print("You have chosen to exit the account, thank you for using our banking system.")
                break
            else:
                pass
    
    def run(self):
        bankName = input("What is your bank?\n")
        bank = Bank(bankName)
        self.showMainMenu(bank)




class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._minimumBalance = minimumBalance

    def getMinimumBalance(self):
        return self._minimumBalance
    def setMinimumBalance(self, min):
        self._minimumBalance = min

    def withdraw(self, amount):
        try:
            amount = int(amount)
            if amount > 0 and amount < self._currentBalance and self._currentBalance - amount > self._minimumBalance:
                print(f"${amount} has been withdrawn from your account.")
                self.setCurrentBalance(self.getCurrentBalance() - amount)
            elif amount < 0:
                errorMessage = '''
                Negative value inputted, try again.\n
                How much would you like to withdraw?\n
                '''
                withdrawAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount)  
            elif amount > self._currentBalance:
                errorMessage = f'''
                Value inputted is larger than account balance, try again.\n
                How much would you like to withdraw?\n
                Overdraft limit: {self.getMinimumBalance()}\n
                Current balance: {self.getCurrentBalance()}\n
                Withdraw amount: {amount}
                '''
                withdrawAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount)  
            elif self._currentBalance - amount < self._minimumBalance:
                errorMessage = f'''
                Can not withdraw more than the minimum balance, try again.\n
                Overdraft limit: {self.getMinimumBalance()}\n
                Current balance: {self.getCurrentBalance()}\n
                Withdraw amount: {amount}
                How much would you like to withdraw?\n
                '''
                withdrawAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount) 
            else:
                errorMessage = '''
                Invalid value inputted, try again.\n
                How much would you like to withdraw?\n
                '''
                withdrawAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount)       

        except ValueError:
            errorMessage = '''
            Invalid value inputted, try again.\n
            How much would you like to withdraw?\n
            '''
            withdrawAmount = int(input(errorMessage))
            self.withdraw(withdrawAmount)     

class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._overdraftLimit = overdraftLimit
    
    def getOverdraftLimit(self):
        return self._overdraftLimit
    def setOverdraftLimit(self, limit):
        self._overdraftLimit = limit
    
    def withdraw(self, amount):
        try:
            amount = int(amount)
            if amount > 0 and self._currentBalance - amount > self._overdraftLimit:
                print(f"${amount} has been withdrawn from your account.")
                self.setCurrentBalance(self.getCurrentBalance() - amount)
            elif amount < 0:
                errorMessage = '''
                Negative value inputted, try again.\n
                How much would you like to withdraw?\n
                '''
                withdrawAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount)  
            elif self._currentBalance - amount < self._overdraftLimit:
                errorMessage = f'''
                Cannot withdraw more than the overdraft limit, try again.\n
                Overdraft limit: {self.getOverdraftLimit()}\n
                Current balance: {self.getCurrentBalance()}\n
                Withdraw amount: {amount}
                How much would you like to withdraw?\n
                '''
                withdrawAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount)  
            else:
                errorMessage = '''
                Invalid value inputted, try again.\n
                How much would you like to withdraw?\n
                '''
                withdrawAmount = int(input(errorMessage))
                self.withdraw(withdrawAmount)       

        except ValueError:
            errorMessage = '''
            Invalid value inputted, try again.\n
            How much would you like to withdraw?\n
            '''
            withdrawAmount = int(input(errorMessage))
            self.withdraw(withdrawAmount)    
        
app = Application()
app.run()