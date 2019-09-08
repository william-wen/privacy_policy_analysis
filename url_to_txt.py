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

def url_to_txt_file(url:str):
    if ('www.' in url):
        current_page = "{0.netloc}".format(urlsplit(url)).split('.')[1]
    else:
        current_page = "{0.netloc}".format(urlsplit(url)).split('.')[0]
        
    if os.path.exists(current_page):
        shutil.rmtree(current_page)

    try:
        html = urllib.request.urlopen(url, timeout=5).read().decode('utf-8')
        text = get_text(html)
        if text != "":
            with open (current_page + '.txt', 'w+', encoding="utf-8") as f:
                f.write(text)
        else:
            print(current_page + ' is empty')

    except (urllib.error.HTTPError, urllib.error.URLError, timeout) as error:
        print(url + ": ", error)

