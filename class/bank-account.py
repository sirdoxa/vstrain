from random import randrange

class BankAccount:
    all_account_numbers = set()

    def __init__(self, name):
        self.account_number = 0
        while True:
            if (an := randrange(10000, 100000)) not in BankAccount.all_account_numbers:
                BankAccount.all_account_numbers.add(an)
                self.account_number = an
                break
        self.name = name
        self.balance = 0

    def display(self):
        print(40 * "-")
        print(f"Hi, {self.name}\nYour current balance: {self.balance}")
        print(40 * "-")

    def deposit(self):
        amount = float(input('Please enter your amount to deposit: '))
        if amount < 0:
            print("Invalid amount!")
        else:
            self.balance += amount
        self.display()

    def withdraw(self):
        amount = float(input("Please enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
        self.display()

def main():
    acc1 = BankAccount("Mahdi")
    print(f"Your account number is: {acc1.account_number}")

    while True:
        choice = int(input("1) your balance\n2) deposit\n3) withdraw\n>>> Your choice: "))
        if choice == 1:
            acc1.display()
        elif choice == 2:
            acc1.deposit()
        elif choice == 3:
            acc1.withdraw()
        else:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()

