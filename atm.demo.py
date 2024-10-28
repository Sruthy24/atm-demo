'''
author :sruthy s
date:28/10/24
driscription:Write a program that simulates a simple bank ATM system. The user has an initial balance of $1000. 
'''
balance_amount=1000
while True:
    print("1.\tCheck Balance")
    print("2.\tDeposite Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter your Choice"))
    if choice==1:
        print(f"The Current balance${balance_amount}")
    elif choice==2:
        deposit_amount =float(input("Enter the Amount"))
        balance_amount = balance_amount +deposit_amount
        print(f"The deposited amount${deposit_amount}and"f"the current balance_amount")
    elif choice==3:
        withdraw_amount= float(input("Enter the amount to""withdraw:"))
        if withdraw_amount >balance_amount:
         print("Insufficient Balance")
        else:
          balance_amount =balance_amount-withdraw_amount
        print(f" The amount withdraw from the account"f"${withdraw_amount}the balance amount"f"${balance_amount}")
    elif choice ==4:
         break
else:
    print("invalid entry")
