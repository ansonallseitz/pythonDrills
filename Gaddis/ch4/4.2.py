#2. Calories Burned
#Running on a particular treadmill you burn 4.2 calories per minute. 
#Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.


print('Minutes\t\tCalories')
print('----------------------')
    
for i in range(10, 31, 5):
    calories = i * 4.2
    print(f'{i}\t\t{calories}')

    
