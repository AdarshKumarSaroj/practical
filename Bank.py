class BankAccount:
    def __init__(self, account_name, initial_balance=0):
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs.{amount} deposited successfully!")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully!")

    def check_balance(self):
        print(f"Account Balance: Rs.{self.balance}")

print("Welcome to the Bank!")
account_name = input("Enter your account name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_name, initial_balance)

print("\nMenu:")
print("1. Deposit Money")
print("2. Withdraw Money")
print("3. Check Balance")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    amount = float(input("Enter amount to deposit: "))
    account.deposit(amount)
elif choice == "2":
    amount = float(input("Enter amount to withdraw: "))
    account.withdraw(amount)
elif choice == "3":
    account.check_balance()
elif choice == "4":
    print("Thank you for banking with us!")
else:
    print("Invalid choice! Please try again.")
