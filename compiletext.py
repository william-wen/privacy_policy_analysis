import os
from scrape import *
from url_to_txt import *

with open('500companyurl.txt', 'r') as f:
    fl = f.read().splitlines()

f_privacy = open('privacy_pages.txt', 'w+')
f_privacy.seek(0, 0)

PrP = 'Privacy_Policies'

unable = 0

if os.path.exists(PrP):
    shutil.rmtree(PrP)

if not os.path.exists(PrP):
    os.mkdir(PrP)
    
os.chdir(PrP)

for url in fl:
    scraped = scrapeUrl(url)
    if scraped == "":
        unable += 1
    else:
        url_to_txt_file(scraped)

print("failed to scrape: ", unable)

print('Url to Txt Complete')
