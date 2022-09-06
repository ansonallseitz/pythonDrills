#14. Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# *


base_Size = 7

for r in range(1, base_Size+1):
    for c in range(7- r):
        print('*', end='')
    print()