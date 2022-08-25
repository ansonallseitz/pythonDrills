#A bug collector collects bugs every day for five days. 
#Write a program that keeps a running total of the number of bugs collected during the five days. 
#The loop should ask for the number of bugs collected 
#for each day, and when the loop is finished, the program should display the total number of bugs collected.


total = 0
for x in range (5): 
    BugNumber = int(input("Enter the number of bugs you collected today: "))
    total = total + BugNumber

print("You caught this many bugs:  ", total)
    