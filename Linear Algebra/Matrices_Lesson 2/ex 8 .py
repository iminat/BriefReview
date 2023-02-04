# Create a function that generates a zero matrix.
# You can not solve the problem just by calling the defined above function matrix_diag.

def matrix(n =1,m = 0, a = 0):
    if n == 1 and not m:
        m = 1
    elif n != 1 and not m:
        m = n
    return [[a for _ in range(n)] for _ in range(m)]

print(matrix(3))