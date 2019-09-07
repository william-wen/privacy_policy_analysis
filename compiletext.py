from scrape import *

f = open('100company.txt', 'r')

fl = f.readlines()

f_privacy = open('privacy_pages.txt', 'w+')
f_privacy.seek(0, 0)

unable = 0
for url in fl:
    scraped = scrapeUrl(url)
    if scraped == "":
        unable += 1
    else:
        f_privacy.writelines(scraped+'\n')

print("failed to scrape: ", unable)

f.close()
