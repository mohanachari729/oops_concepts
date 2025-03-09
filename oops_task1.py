# #creating a laptop object
# class laptop():
#     brand_name = 'acer nitro'
#     colour = 'black'
#     model = 'V15'
#     def browsing(self):
#         print(f"i browsing in {self.brand_name}")
#         print("--"*20)
#     def hardware(self):
#         print(f"the hardware model is {self.model} and the laptop is {self.colour} colour")
#         print("--"*20)
#     def calling(self):
#         print(f"i calling in {self.brand_name}")
#         print("--"*20)
#     def gaming(self):
#         print(f"i gamimg in laptop {self.brand_name} and it's performance depends GPU amd model{self.model}")
#         print("--"*20)
# obj = laptop()
# obj.browsing()
# obj.calling()
# obj.hardware()
# obj.gaming()

##ATM program in oops concept 
class ATM:
    def __init__(self, bankname, location, balance=0):
        self.bankname = bankname
        self.location = location
        self.balance = balance

    def credit(self):
        credit_amt = float(input("Enter the depositing amount: "))
        if credit_amt > 0:
            self.balance += credit_amt
            print(f"${credit_amt} is Deposited into your {self.bankname} account")
        else:
            print("Enter the positive amount ")

    def debit(self):
        debit_amt = float(input("Enter the amount to withdraw from your account: "))
        if debit_amt > 0 :
            self.balance -= debit_amt
            print(f"${debit_amt} is debited from your {self.bankname} account in {self.location}")
        else:
            print("you account is empty")

    def show_balance(self):
        print(f"Your current balance is ${self.balance}")

    def exit(self):
        print(f"Thank you for visiting {self.bankname} ATM located at {self.location}. have a nice day")

    def menu(self):
        return input('''
          Welcome ATM !!
    ------------------------------
             1. Credit
             2. Debit
             3. Balance
             4. Exit
        Please choose an option: ''')
    print("--"*20)

def main():
    atm = ATM("SBI", "VEEREPALLI")
    while True:
        choice = atm.menu()
        if choice == '1':
            atm.credit()
        elif choice == '2':
            atm.debit()
        elif choice == '3':
            atm.show_balance()
        elif choice == '4':
            atm.exit()
            break
        else:
            print("Invalid option, please try again")
main()


