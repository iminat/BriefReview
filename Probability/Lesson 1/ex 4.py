#In this exercise you will estimate how smoking is related with some (imaginary) disease
#Imagine that 0.1% of the population have this disease.
#Also it is known that there are 13% of smoker in the population.
#Finally 30% of the diseased people smoke.
#Given this data draw a conclusion do smoking provoke the disease?
#To answer it find the percentage of the smokers that have this disease
#and then compare it with the marginal percentage of the diseased people.

disease_percentage = 0.1  # 0.1% of the population have the disease
smoker_percentage = 0.13  # 13% of the population are smokers
smoker_disease_percentage = 0.30  # 30% of the diseased people are smokers

# Calculate the percentage of smokers that have the disease
smoker_disease_ratio = smoker_disease_percentage / smoker_percentage
diseased_smokers = smoker_disease_ratio * disease_percentage

print(f"Percentage of smokers that have the disease: {diseased_smokers:.2%}")
print(f"Percentage of diseased people: {disease_percentage:.2%}")