#Create a program that writes to a CSV-file a table with two columns.
# The first one is the month name and the second one is the number of its days.

import csv

# Define the list of month names and number of days
month_days = [("January", 31), ("February", 28), ("March", 31), ("April", 30), ("May", 31), ("June", 30),
              ("July", 31), ("August", 31), ("September", 30), ("October", 31), ("November", 30), ("December", 31)]

# Open the CSV file for writing
with open("month_days.csv", "w", newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Month", "Days"])
    # Loop over the months and write the rows to the CSV file
    for month, days in month_days:
        writer.writerow([month, days])
