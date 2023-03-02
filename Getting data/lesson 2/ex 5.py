#Write the program the loads webpage https://kupav.github.io/data-sc-intro/dickens.html
#and find there a link to a wikipedia article about Charles Dickens.
import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
response = requests.get("https://kupav.github.io/data-sc-intro/dickens.html")

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the Wikipedia article about Charles Dickens
link = soup.find("a", href="https://en.wikipedia.org/wiki/Charles_Dickens")

# Print the link if it exists
if link:
    print(link['href'])
else:
    print("Link not found")
