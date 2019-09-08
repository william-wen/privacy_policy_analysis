# Import libraries
import requests
import requests.exceptions
import time
import re
from bs4 import BeautifulSoup
import socket

def scrapeUrl(url: str) -> str:
    # Set the URL you want to webscrape from
    # Connect to the URL
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.Timeout:
        return ""
    except requests.exceptions.TooManyRedirects:
        return ""
    except requests.exceptions.ConnectionError:
        return ""
    except requests.exceptions.ContentDecodingError:
        return ""

    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    # print(soup.get_text())
    pri_url = []
    for link in soup.find_all('a'):
        try:
            if 'rivacy' in link.get('href'):
                pri_url.append(link.get('href'))
        except TypeError:
            continue
    newurl = ""
    if len(pri_url) > 0:
        pri_url.sort(key=len)
        suburl = url.split(".")[-1]
        for i in range(len(pri_url)):
            if 'http' in pri_url[i]:
                newurl = pri_url[i]
            else:
                if pri_url[0] == '/':
                    newurl = url[:-2] + pri_url[i][1:]
                else:
                    newurl = url[:-1] + pri_url[i]
            if suburl in newurl:
                break
    return newurl


# # To download the whole data set, let's do a for loop through all a tags
# for i in range(36, len(soup.findAll('a')) + 1):  # 'a' tags are for links
#     one_a_tag = soup.findAll('a')[i]
#     link = one_a_tag['href']
#     download_url = 'http://web.mta.info/developers/' + link
#     urllib.request.urlretrieve(download_url, './' + link[link.find('/turnstile_') + 1:])
#     time.sleep(1)  # pause the code for a sec

# if __name__ == '__main__':
#     print(scrapeUrl('https://www.amazon.ca/'))
