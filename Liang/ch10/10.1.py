       #(Assign grades) Write a program that reads a list of scores and then assigns grades based on the following scheme:


import random 

RandomGradeList = []

for i in range(0, 20):
    n = random.randint(55, 100)
    RandomGradeList.append(n)


RandomGradeList.sort()


print(RandomGradeList)


best = RandomGradeList[-1]

for z in RandomGradeList:
    if z >= (best-10): 
        print("Score: ", z, "Is an A") 
    elif z >= (best-20):
        print("Score: ", z, "Is a B")
    elif z >= (best-30):
        print("Score: ", z, "Is a C")
    elif z >= (best-40):
        print("Score: ", z, "Is a D")
    else:
        print("Score: ", z, "Is an F")







