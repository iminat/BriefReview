# Task 8
# Write a program that begins by reading a radius, , from the user.
# The program will continue by computing and displaying the area of a circle with radius  and the volume of a sphere with radius.
# Use the pi constant in the math or numpy modules in your calculations.
# Use Internet to look up the necessary formula if you don't have them memorized.

from math import *
radius = int(input())
area = pi*(radius)**2
volume = 4/3*pi*(radius)**3
print(round(area,2), round(volume,2))