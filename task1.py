class ATM:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        print(f"Account balance: ${self.balance:.2f}")

    def withdraw_cash(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
            print(f"Withdrawal successful! New balance: ${self.balance:.2f}")

    def deposit_cash(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount:.2f}")
        print(f"Deposit successful! New balance: ${self.balance:.2f}")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Invalid old PIN!")

    def view_transaction_history(self):
        print("Transaction history:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")
    atm = ATM(account_number, pin)

    while True:
        print("\nATM Menu:")
        print("1. Check balance")
        print("2. Withdraw cash")
        print("3. Deposit cash")
        print("4. Change PIN")
        print("5. View transaction history")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw_cash(amount)
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: "))
            atm.deposit_cash(amount)
        elif choice == "4":
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter your new PIN: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == "5":
            atm.view_transaction_history()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()