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
    pass

class SavingsAccount(Account):
    pass

class ChequingAccount(Account):
    pass
