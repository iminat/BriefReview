# Task 11
# Develop a program that reads a four-digit integer from the user and displays the sum of its digits.
# For example, if the user enters 3141 then your program should display 3 + 1 + 4 + 1 = 9.

num = input()
sum = 0
for i in num:
    sum += int(i)
print(sum)