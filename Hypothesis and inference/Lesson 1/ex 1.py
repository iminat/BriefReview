#Using Python functions defined above compute probability that a random variable
#obeyed the standard normal distribution fits the range [-1, 1].

from scipy.stats import norm

# Calculate the probability that a random variable in the standard normal distribution is within [-1, 1]
prob = norm.cdf(1) - norm.cdf(-1)

print(f"The probability that a random variable in the standard normal distribution is within [-1, 1] is: {prob:.4f}")
