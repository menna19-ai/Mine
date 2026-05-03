accounts=[]
total_accounts=0
transaction=[]
def create_new_account():
    global total_accounts #outside the function
    name=input("Enter your name:")
    try:
        balance=float(input("Enter your balance:")) 
        pin=int(input("Enter your pin:")) 
    except ValueError :
        print("Enter numbers only!")
        return
    accounts.append({"Name":name,"Balance":balance,"Pin":pin})
    total_accounts+=1
    transaction.append(("Total account",total_accounts))
    
def check_balance(pin):
    found=False
    for account in accounts:
        if pin==account["Pin"]:
           print("Your balance is",account["Balance"])
           found=True
           break
    if not found:
        print("Enter the right pin")
        

def deposit(pin, amount):
    for account in accounts:
        if pin == account["Pin"]:
            account["Balance"] += amount
            print("Deposit successful. New balance:", account["Balance"])
            return
    print("Account not found")
        
def withdraw_money(pin, amount):
    for account in accounts:
        if pin == account["Pin"]:
            if account["Balance"] < amount:
                print("You do not have enough money!")
            else:
                account["Balance"] -= amount
                print("Withdrawal successful. New balance:", account["Balance"])
            return
    print("Account not found")
def transfer_money(pin1,pin2,amount):
    sender = None
    receiver = None
    for account in accounts:
        if account["Pin"] == pin1:
            sender = account
        if account["Pin"] == pin2:
            receiver = account
    if sender is None or receiver is None:
        print("One or both accounts not found!")
        return
    if sender["Balance"] < amount:
        print("You do not have enough money!")
        return
    sender["Balance"] -= amount
    receiver["Balance"] += amount
    print("Transefered sucessfully!")
def show_bank_statistics():
    total_accounts = len(accounts)
    if total_accounts == 0:
        print("No accounts available")
        return
    total_balance=0
    for account in accounts:
        total_balance+=account["Balance"]
    average_balance = total_balance / total_accounts
    print("Total accounts:", total_accounts)
    print("Total balance:", total_balance)
    print("Average balance:", average_balance)
def main():
    while True:
        print("""
1 Create account
2 Check balance
3 Deposit
4 Withdraw
5 Transfer
6 Statistics
0 Exit
""")
        choice = input("Choose: ")
        if choice == "1":
            create_new_account()
        elif choice == "2":
            pin = int(input("Pin: "))
            check_balance(pin)
        elif choice == "3":
            pin = int(input("Pin: "))
            amount = float(input("Amount: "))
            deposit(pin, amount)
        elif choice == "4":
            pin = int(input("Pin: "))
            amount = float(input("Amount: "))
            withdraw_money(pin, amount)
        elif choice == "5":
            pin1 = int(input("Sender pin: "))
            pin2 = int(input("Receiver pin: "))
            amount = float(input("Amount: "))
            transfer_money(pin1, pin2, amount)
        elif choice == "6":
            show_bank_statistics()
        elif choice == "0":
            break
        else:
            print("Invalid choice")
main()
        
        
    