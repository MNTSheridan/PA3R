class Account:
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self._accountNumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance

class Bank:
    def __init__(self, bankName):
        self._bankName = bankName

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
                print("Try again")
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
                print("Try again")
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
    pass

class ChequingAccount(Account):
    pass
