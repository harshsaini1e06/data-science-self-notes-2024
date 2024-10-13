available_balance = 5000
message = """
enter 1 for check balance,
enter 2 for deposit amount,
enter 3 for withdrawl amount
"""
print (message)
task = int(input('enter your task : '))

if task == 1: # check balance
    print ("your availabe balance is : ",available_balance)

elif task == 2: # deposition of amount
    deposit_amount = int(input('enter the amount of deposition : '))
    if deposit_amount>0:
        available_balance += deposit_amount
        print ("you have successfully deposited your amount in account : ",deposit_amount)
        print ("now your total amount is : ",available_balance)
else: # withdrawal of amount
    withdrawl_amount = int(input("enter the amount you want to withdraw : "))
    if withdrawl_amount <= available_balance:
        available_balance -= withdrawl_amount
        print ("you hav successfully withdrawl the amount : ",withdrawl_amount)
        print ("the remaining total amount : ",available_balance)
