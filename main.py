from savings_account import SavingsAccount
from checking_account import CheckingAccount

savings1 = SavingsAccount("John", "123456", "987654", 100000, 10000, 0.05)
savings2 = SavingsAccount("Wendy", "789012", "654321", 200000, 10000, 0.03)

checking1 = CheckingAccount("Mark", "234567", "876543", 50000, 5000, 10000)
checking2 = CheckingAccount("Lisa", "345678", "765432", 75000, 5000, 5000)

savings1.print_customer_information()
savings1.apply_interest()
savings1.print_customer_information()

checking2.print_customer_information()
checking2.transfer(6000, checking1)
checking2.transfer(3000, checking1)
checking2.print_customer_information()

checking1.deposit(2000)
checking1.transfer(8000, checking2)
checking1.print_customer_information()

print("\nFinal Accounts")
savings1.print_customer_information()
savings2.print_customer_information()
checking1.print_customer_information()
checking2.print_customer_information()
