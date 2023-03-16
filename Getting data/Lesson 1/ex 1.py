#Create the program that writes to a file the multiplication table for pairs of integers from 2 to 9.
# The content of the file should be like
#2 x 2 = 4
#2 x 3 = 6
#...
#9 x 8 = 72
#9 x 9 = 81

with open("multiplication_table.txt", "w") as file:
    # Loop over the pairs of integers from 2 to 9
    for i in range(2, 10):
        for j in range(2, 10):
            # Compute the product
            result = i * j
            # Write to the file
            file.write(f"{i} x {j} = {result}\n")
