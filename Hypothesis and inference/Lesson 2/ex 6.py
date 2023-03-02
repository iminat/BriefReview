#Assume that for a certain age group of students scores on an IQ (intelligence) test are distributed normally with μ = 110 and σ = 16.
#One of the students received a score of 82. Compute p-value for this score. Accepting the significance level at α = 0.05
#make a decision do this student requires a special treatment or his/her IQ is within the norm.

import scipy.stats as stats

# Define the parameters of the normal distribution
mu = 110
sigma = 16

# Define the IQ score of the student
x = 82

# Compute the z-score of the IQ score
z = (x - mu) / sigma

# Compute the p-value of the test
p_value = stats.norm.sf(abs(z)) * 2

# Print the p-value
print("The p-value of the test is:", p_value)

# Make a decision based on the significance level alpha = 0.05
alpha = 0.05
if p_value < alpha:
    print("The IQ score of the student is statistically significant.")
    print("The student may require special treatment based on their IQ score.")
else:
    print("The IQ score of the student is not statistically significant.")
    print("The student's IQ is within the normal range.")

