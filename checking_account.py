from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, account_number, routing_number, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name, account_number, routing_number, current_balance, minimum_balance)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, recipient):
        if amount > self.transfer_limit:
            print(f"\nTransfer failure. Exceeds transfer limit of {self.transfer_limit}\n")
        elif self.current_balance - amount < self.minimum_balance:
            print("\nCannot transfer! Insufficient funds.\n")
        else:
            self.current_balance -= amount
            recipient.current_balance += amount
            print(f"Transfer Success. New Balance: {self.current_balance}")