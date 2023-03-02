
#Write the program that loads main page of this site https://ria.ru/?ysclid=ler8xultst917623234
# and saves its full textual content to a file.

import requests

# Send a GET request to the webpage
response = requests.get("https://ria.ru/")

# Save the textual content of the webpage to a file
with open("ria_ru.txt", "w", encoding=response.encoding) as file:
    file.write(response.text)
