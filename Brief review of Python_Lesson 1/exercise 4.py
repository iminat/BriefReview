# Task 4
# Pretend that you have just opened a new savings account that earns 4 percent interest per year.
# The interest that you earn is paid at the end of the year, and is added to the balance of the savings account.
# Write a program that begins by reading the amount of money deposited into the account from the user.
# Then your program should compute and display the amount in the savings account after 1, 2, and 3 years.
# Display each amount so that it is rounded to 2 decimal places.

deposit = float(input())
first_year = (deposit*0.04)+deposit
second_year = (first_year*0.04)+first_year
third_year = (second_year*0.04)+second_year
print("The amount of savings in the first year:", round(first_year,2),"in the second:", round(second_year,2), "in the third:", round(third_year,2))