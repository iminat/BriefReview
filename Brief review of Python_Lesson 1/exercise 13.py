# Task 13
# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60 percent.
# Write a program that begins by reading the number of loaves of day old bread being purchased from the user.
# Then your program should display the regular price for the bread, the discount because it is a day old, and the total price.
# Each of these amounts should be displayed on its own line with an appropriate label.
# All of the values should be displayed using two decimal places, and the decimal points in all of the numbers should be aligned when reasonable values are entered by the user.

loaf_of_bread = 3.49
day_old_bread = loaf_of_bread*0.6
number_of_loaves = int(input())
print("Price for the loaves:", round(loaf_of_bread*number_of_loaves,2))
print("Price for the day old loaves:", round(day_old_bread*number_of_loaves,2))
print("total:", round(loaf_of_bread*number_of_loaves-(day_old_bread*number_of_loaves),2))