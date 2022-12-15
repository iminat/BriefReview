# Before doing the exercise find some image in the Internet and download it to your local directory.
# Now create a program that shows this image.
# Hide axes tics. Add a title to your plot and show there an image height, width and a number of colors.

import requests

# This is an URL of a repository
base_url = "https://eus-www.sway-cdn.com/s/2GQzKvICIXF26anZ/images/iKW0l2Kw3xTx3Q?quality=900&allowAnimation=true"

# We need this file
file_name = "boole.jpeg"

# Here we download the file
web_data = requests.get(base_url + file_name)
assert web_data.status_code == 200

# And save it locally
with open(file_name, "wb") as f:
    f.write(web_data.content)

import matplotlib.pyplot as plt
img = plt.imread("boole.jpeg")

print(type(img))
print(img.shape)

fig, ax = plt.subplots()
ax.imshow(img)


from matplotlib import ticker  # import ticker to customize ticks
ax.xaxis.set_major_formatter(ticker.NullFormatter())  # it hides x tick labels
ax.yaxis.set_major_formatter(ticker.NullFormatter())  # it hides x tick labels
ax.xaxis.set_major_locator(ticker.NullLocator())  # it hides x ticks
ax.yaxis.set_major_locator(ticker.NullLocator())  # it hides y ticks

plt.title('George Boole')
plt.show()