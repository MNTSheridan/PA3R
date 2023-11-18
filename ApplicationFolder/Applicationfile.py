class Account:
    def __init__(self):
        self._accountNumber = None
        self._accountHolderName = None
        self._rateOfInterest = None
        self._currentBalance = None
    
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

    def deposit():
        pass

    def withdraw():
        pass

class Bank:
    def __init__(self, bankName):
        self._bankName = bankName
    
    def openAccount():
        pass
    def searchAccount():
        pass

class Application:
    def showMainMenu():
        while True:
            menuMessage = '''
            Banking Application Menu:\n
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
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            else:
                pass

    def showAccountMenu():
        while True:
            menuMessage = '''
            Banking Application Account Menu:\n
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
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                print("You have chosen to exit the account, thank you for using our banking system.")
                break
            else:
                pass
    
    def run():
        pass

    run()


class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._minimumBalance = minimumBalance

class ChequingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._overdraftLimit = overdraftLimit
        
