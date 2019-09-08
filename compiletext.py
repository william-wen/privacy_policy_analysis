import os
from scrape import *
from url_to_txt import *

with open('500companyurl.txt', 'r') as f:
    fl = f.read().splitlines()

f_privacy = open('privacy_pages.txt', 'w+')
f_privacy.seek(0, 0)

ToS = 'Terms of Services'

no_pri_url = 0
total_url = 0
for url in fl:
    total_url += 1
    print("total_url ", total_url, '\n')
    scraped = scrapeUrl(url)
    if scraped == "":
        no_pri_url += 1
        print(no_pri_url)
    else:
        f_privacy.writelines(scraped+'\n')

print("failed to scrape: ", no_pri_url)

if os.path.exists(ToS):
    shutil.rmtree(ToS)

if not os.path.exists(ToS):
    os.mkdir(ToS)

os.chdir(ToS)

for url in fl:
    scraped = scrapeUrl(url)
    if scraped == "":
        no_pri_url += 1
    else:
        url_result = url_to_txt_file(scraped)
        if url_result == "":
            unable_to_parse += 1

print("failed to scrape: ", unable_to_scrape)
print("failed to parse: ", unable_to_parse)

print('Url to Txt Complete')

f.close()
