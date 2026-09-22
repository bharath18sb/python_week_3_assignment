class BankAccount:
    def __init__(self, holder_name, account_number, initial_balance=0.0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited ₹{amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount
        print(f"Withdrew ₹{amount:.2f}")

    def display_balance(self):
        print(f"Holder: {self.holder_name}")
        print(f"Account: {self.account_number}")
        print(f"Balance: ₹{self.__balance:.2f}")
        print("-" * 20)

if __name__ == "__main__":
    acc = BankAccount("Rahul", "1001", 5000)
    acc.display_balance()
    acc.deposit(1500)
    acc.withdraw(1000)
    acc.display_balance()
    try:
        acc.withdraw(6000)
    except ValueError as e:
        print(f"Error: {e}")
