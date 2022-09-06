#3. Budget Analysis
#Write a program that asks the user to enter the amount that he or she has budgeted for a month. 
#A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total.
#When the loop finishes, the program should display the amount that the user is over or under budget.
userEntryExpense = float
print("Hey buddy")
print("you need to save some money$$")
monthTotal = int(input('Please enter how much you want to spend: '))
print("Now enter your expenses, when you are done, enter 0")

while userEntryExpense != 0: 
    userEntryExpense =float(input("please enter what you spent: "))
    monthTotal= monthTotal - userEntryExpense
    print("You have this much left in your budget: ", monthTotal)

print('all done buddy, you have this much to spend this month: ', monthTotal)
