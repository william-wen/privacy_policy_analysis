# Import libraries
import requests
import urllib.request
import time
import os
import re
import shutil
from bs4 import BeautifulSoup
from lxml import html
from urllib.parse import urlsplit
from inscriptis import get_text
from socket import timeout

ToS = 'Terms of Services'

if os.path.exists(ToS):
    shutil.rmtree(ToS)

if not os.path.exists(ToS):
    os.mkdir(ToS)

os.chdir(ToS)

# Set the URL you want to webscrape from
company_urls = open('./privacy_pages.txt', 'r', encoding='utf-8')
urls = company_urls.read().split('\n')

for url in urls:
    print(url)
    current_page = "{0.netloc}".format(urlsplit(url)).split('.')[1]

    if os.path.exists(current_page):
        shutil.rmtree(current_page)

    new_file = open(current_page + '.txt', 'w+')

    try:
        html = urllib.request.urlopen(url, timeout=3).read().decode('utf-8')
    except (urllib.error.HTTPError, urllib.error.URLError, timeout) as error:
        print(error)

    text = get_text(html)

    with open (current_page + '.txt', 'w', encoding="utf-8") as f:
        f.write(text)