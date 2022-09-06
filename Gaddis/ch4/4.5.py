#5. Average Rainfall
#Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
#The program should first ask for the number of years. The outer loop will iterate once for each year. 
#The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
#After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.


print("Hey Buddy!")
print("This is the average rainfall calcualting program.")
print(" first enter the number of years, then the rainfall each month.")
print("and the program will tell you the average rainfall")


yearNumber = int(input("How many years?: "))
monthList = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
totalRainfall= 0
monthRainfall = 0

for y in range(yearNumber):
    for mon in range(len(monthList)):
        print(' enter the monthly rainfall for',monthList[mon])
        monthRainfall = int(input(': '))
        totalRainfall =  totalRainfall + monthRainfall 

averageYearRainfall = totalRainfall / (12 * yearNumber)
print("Average rainfall for the peroid", y, " = ", averageYearRainfall)
print("Total Rainfall for the Peroid: ", y, "=", totalRainfall)
