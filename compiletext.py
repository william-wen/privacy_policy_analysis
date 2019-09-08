import os
from scrape import *
from url_to_txt import *

with open('100company.txt', 'r') as f:
    fl = f.read().splitlines()

f_privacy = open('privacy_pages.txt', 'w+')
f_privacy.seek(0, 0)

ToS = 'Terms of Services'

unable = 0
for url in fl:
    scraped = scrapeUrl(url)
    if scraped == "":
        unable += 1
    else:
        f_privacy.writelines(scraped+'\n')
        
print("failed to scrape: ", unable)

if os.path.exists(ToS):
    shutil.rmtree(ToS)

if not os.path.exists(ToS):
    os.mkdir(ToS)
    
os.chdir(ToS)

for url in fl:
    scraped = scrapeUrl(url)
    if scraped == "":
        unable += 1
    else:
        url_to_txt_file(scraped)

print('Url to Txt Complete')
    
f.close()
