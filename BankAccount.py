class BankAccount:
    bank_title = "Generic Ahh Bank"

    def __init__(self, customer_name, account_number, routing_number, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  # Protected
        self.__routing_number = routing_number  # Private

    def deposit(self, amount):
        self.current_balance += amount
        print("Deposit Successful!\nNew Balance:", self.current_balance)

    def withdraw(self, amount):
        if self.current_balance-amount < self.minimum_balance:
            print("\nCannot make a withdrawal at this time! Cannot drop below the minimum balance\n")
        else:
            self.current_balance -= amount
            print("Withdrawal Successful!\nNew Balance:", self.current_balance)

    def print_customer_information(self):
        print("Bank Title:", BankAccount.bank_title)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.current_balance)
        print(f"Minimum Balance: {self.minimum_balance}\n")
'''
person1 = BankAccount("John", 100000, 100000)
person2 = BankAccount("Wendy", 200000, 100000)

person1.print_customer_information()
person1.deposit(100)
person2.print_customer_information()
person2.withdraw(100)
person2.withdraw(100)
person1.print_customer_information()
person1.withdraw(100000)
person1.deposit(1100)
person1.withdraw(1200)
person1.withdraw(100)
person2.print_customer_information()
person2.deposit(1300)
person2.withdraw(1500)


print("\nFinal Accounts")
person1.print_customer_information()
person2.print_customer_information()
'''