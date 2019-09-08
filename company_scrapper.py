# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

# Set the URL you want to webscrape from
# url = 'https://www.zyxware.com/articles/4344/list-of-fortune-500-companies-and-their-websites'
url = "https://moz.com/top500"

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.content, "html.parser")
f = open('100Companies.txt', 'w')
i = 0
for link in soup.find_all('a'):
    text = link.get('href')
    print(link.get('href'))
    # regex matching has first 1/3 of data not working, omit regex for now
    # if (13 < i < 115) and (text is not None):
    #     found = re.search("www.*\.com$", text)
    #     # if found is not None:
    #     f.write(text + "\n")
    #     print(text)
    # i += 1

f.close()
print("Done")
