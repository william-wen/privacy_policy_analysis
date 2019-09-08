import os
from scrape import *
from url_to_txt import *

with open('500companyurl.txt', 'r') as f:
    fl = f.read().splitlines()

f_privacy = open('privacy_pages.txt', 'w+')
f_privacy.seek(0, 0)

PrP = 'Privacy_Policies'

unable_to_scrape = 0
unable_to_parse = 0


if os.path.exists(PrP):
    shutil.rmtree(PrP)

if not os.path.exists(PrP):
    os.mkdir(PrP)
    
os.chdir(PrP)

for url in fl:
    scraped = scrapeUrl(url)
    if scraped == "":
        unable_to_scrape += 1
    else:
        url_result = url_to_txt_file(scraped)
        if url_result == "":
            unable_to_parse += 1

print("failed to scrape: ", unable_to_scrape)
print("failed to parse: ", unable_to_parse)

print('Url to Txt Complete')
