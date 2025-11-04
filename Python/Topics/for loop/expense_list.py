'''Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.'''

expense_list = [2340, 2500, 2100, 3100, 2980]
expense = input("Enter expense amount: ")
expense = int(expense)
for i in range(len(expense_list)):
    if(expense==expense_list[i]):
        print("Expense occurred in month:",i+1)
        break
    else:
        print("Expense not found in month:", i + 1)