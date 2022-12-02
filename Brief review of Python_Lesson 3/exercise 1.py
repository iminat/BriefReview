# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters traveled.
# Write a function that takes the distance traveled (in kilometers) as its only parameter
# and returns the total fare as its only result. Write a main program that demonstrates the function.

# Hint: Taxi fares change over time.
# Use constants to represent the base fare and the variable portion of the fare
# so that the program can be updated easily when the rates increase.

BASE_FARE = 4.00
FOR_EVERY_140_METERS = 0.25
def taxi_fares(distance):
    #convert km to meters
    total_fare = ((distance * 1000)//140)*FOR_EVERY_140_METERS
    total_fare += BASE_FARE
    return total_fare

distance = int(input())
print(taxi_fares(distance))

