#File "random_words.txt" that you can find at
"https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/"
#contains the output of a random word generator.
#Its outcomes include six different words that are generated at random, one word per line.
#Write a program that downloads this file,
#reveals and print the words, and computes the related information entropy.
import requests
import math

url = "https://raw.githubusercontent.com/kupav/data-sc-intro/main/data/random_words.txt"

# Download the file
response = requests.get(url)
text = response.text

# Split the file into individual words
words = text.strip().split('\n')

# Count the frequency of each word
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Calculate the probability of each word
total_words = len(words)
word_probs = {word: count / total_words for word, count in word_counts.items()}

# Calculate the entropy
entropy = -sum(prob * math.log2(prob) for prob in word_probs.values())

# Print the words and entropy
print("Words:")
print(words)
print("\nEntropy:")
print(entropy)