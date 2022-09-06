#6. Celsius to Fahrenheit Table
#Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents. 
#The formula for converting a temperature from Celsius to Fahrenheit is: 
#                                   F=(9/5)C +32
#where F is the Fahrenheit temperature, and C is the Celsius temperature. Your program must use a loop to display the table.

print("This is the Farenheit display Program")
print("It will display a cute little table")
print("Temp in C\t\tTemp in F")
print("---------------------------------")

for temp in range(0, 20):
    fTemp = round(((9/5)*temp) + 32)
    print(f'{temp}\t\t\t{fTemp}')
    
    