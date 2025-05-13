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
        
        amount = float(input('please enter your amount to deposit: '))
        if amount > self.balance:
            print('insufficent balance!')
        else:
            self.balance-= amount
        
        self.display()

def main():
    acc1 = BankAccount("reza dolati")
    print(acc1.account_number)

    while True:
        choice = int(input("Enter 1 to see your balance,\n2 to deposit\n3 to withdraw\n\tYour choice: "))
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

mahdi = BankAccount('mahdi')

mahdi()