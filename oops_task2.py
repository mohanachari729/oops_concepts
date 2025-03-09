# ##single inheritance
# class ATM():
#     def __init__ (self,bank_name,location,expire,balance=0):
#         self.bank_name = bank_name
#         self.location = location
#         self.expire = expire
#         self.balance = balance

# class card(ATM):
#     def display_menu(self):
#         print("--"*20)
#         print("\nATM Menu:")
#         print("1. Credit")
#         print("2. Debit")
#         print("3. Balance_enqiery")
#         print("4. Exit")
#         print("--"*20)
#     def get_choice(self):
#         return input("Choose the option(1-4):")
#     def credit(self):
#         amount = int(input("enter the amount:"))
#         global balance
#         self.balance += amount
#         print(f"${amount} is credited sucessfully in your {self.bank_name}")
#     def debit(self):
#         global balance
#         amount = int(input("enter the amount:"))
#         self.balance -= amount
#         if amount > self.balance:
#             print("insufficient balance in your account")
#         else:
#             self.balance -= amount
#             print(f"${amount} is debited sucessfully in your {self.bank_name} in {self.location}")
#     def balance_enqire(self):
#         print(f"${self.balance} is avalible in your account")


# bank = card("SBI","veerepalli",2026)
# print()
# print("welcome to SBI bank,have a nice day")
# print()
# bank.display_menu()
# while True:
#     value = bank.get_choice()   
#     if value <= "0" or value >="5":
#         print("invalid option, Please enter correct option")
#     elif value == "1":
#         bank.credit()
#     elif value == "2":
#         bank.debit()
#     elif value == "3":
#         bank.balance_enqire()
#     else:
#         print("thank you have a nice day")
#         break
#     print()




# ##hierachical inheristance
class ATM:
    def __init__(self, bankname, location, balance=0):
        self.bankname = bankname
        self.location = location
        self.balance = balance
    def show_balance(self):
        print(f"Your current balance is ${self.balance}")

    def exit(self):
        print(f"Thank you for visiting {self.bankname} ATM located at {self.location}. have a nice day")

class credit(ATM):
    def credit(self):
        credit_amt = float(input("Enter the depositing amount: "))
        if credit_amt > 0:
            self.balance += credit_amt
            print(f"${credit_amt} is Deposited into your {self.bankname} account")
        else:
            print("Enter the positive amount ")

class debit(ATM):
    def debit(self):
        debit_amt = float(input("Enter the amount to withdraw from your account: "))
        if debit_amt > 0 :
            self.balance -= debit_amt
            print(f"${debit_amt} is debited from your {self.bankname} account in {self.location}")
        else:
            print("you account is empty")

    

class ATM(credit ,debit ):
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





