from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

Glenn = InterestRewardsAcct(1000, 'Glenn')

Glenn.getBalance()

Glenn.deposit(100)

Glenn.transfer(100, Dave)

Blaize = SavingsAcct(1000, "Blaize")

Blaize.getBalance()

Blaize.deposit(100)

Blaize.transfer(10000, Sara)
Blaize.transfer(1000, Sara)
