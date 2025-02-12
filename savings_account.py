from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, account_number, routing_number, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, account_number, routing_number, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"Interest has been added! New Balance: {self.current_balance:.2f}")