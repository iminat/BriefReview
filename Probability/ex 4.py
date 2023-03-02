#Using cross-entropy compare two probability distributions
#Q1 = [0.16, 0.19, 0.17, 0.15, 0.19, 0.14]
#Q2 = [0.13, 0.11, 0.14, 0.19, 0.21, 0.22]
#designed to model rolling the die. Which one approximate the die better?
import numpy as np

def cross_entropy(Q, P):
    H = -np.sum(P * np.log(Q))
    return H

Q1 = np.array([0.16, 0.19, 0.17, 0.15, 0.19, 0.14])
Q2 = np.array([0.13, 0.11, 0.14, 0.19, 0.21, 0.22])

# The true distribution is represented by the uniform distribution
P = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

H1 = cross_entropy(Q1, P)
H2 = cross_entropy(Q2, P)

if H1 < H2:
    print("Q1 is a better approximation of the true distribution")
elif H1 > H2:
    print("Q2 is a better approximation of the true distribution")
else:
    print("Both Q1 and Q2 have the same approximation")