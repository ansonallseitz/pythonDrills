#4. Distance Traveled The distance a vehicle travels can be calculated as follows: 
#_________________________________________________________Distance = Speed x time
#For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120 miles. 
#Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. 
#It should then use a loop to display the distance the vehicle has traveled for each hour of that time period. Here is an example of the desired output:
#What is the speed of the vehicle in mph? 40 [Enter]
# How many hours has it traveled? 3 [Enter]
# Hour         Distance Traveled
# 1                    40
# 2                    80
# 3                   120



print("This is the  mph calculating program")
print(" distance = speed x time")
print("tell us how fast you want a train to run, and how many hours, and this program")
print("will spit out a table.")

speed= int(input("what is the speed of the choochoo train in mph?: "))
hourNum = int(input("how many hours does the choo-choo train travel? I prefer you enter a whole number: "))
print('Hour\t\tDistance_Traveled')
print('-------------------------')

distanceTraveled =int
distanceTraveled = 0

for i in range(0, hourNum+1, 1):
    distanceTraveled = speed * i 
    print(f'{i}\t\t\t40{distanceTraveled}')
