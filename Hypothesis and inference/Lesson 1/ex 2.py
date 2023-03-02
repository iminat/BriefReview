#Using Python functions compute such X that a random variable x
#obeyed the standard normal distribution is x<X with the probability 0.25

from scipy.stats import norm

# Find X such that P(x < X) = 0.25, where x is a random variable with standard normal distribution
X = norm.ppf(0.25 + norm.cdf(0))

print(f"The value of X such that P(x < X) = 0.25 is: {X:.4f}")
