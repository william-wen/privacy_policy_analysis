from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import scrape
import re
import url_to_txt
import urllib
from urllib.parse import urlsplit
from inscriptis import get_text
from socket import timeout
import http
import textstat
import fleschIndex
from loaded_model import predict_score


regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def somethingwentwrong():
    messagebox.showinfo("Oops", "Sorry, something went wrong!")


def display_scores(name: str, text: str) -> None:
    fleschEaseScore = textstat.flesch_reading_ease(text)
    fESAll = fleschIndex.fleschscore()
    fESAll.sort()
    print(fESAll)
    percentile = 100
    for i in range(len(fESAll)):
        if fleschEaseScore < fESAll[i]:
            percentile = int(100*(i/len(fESAll)))
            break

    fESContent = "Flesch Reading Ease Score: {},\n which is in the {}th percentile.".format(fleschEaseScore, percentile)
    fESLbl = Label(root, text=fESContent, font=12, pady=10)
    fESLbl.pack()


    flKinScore = textstat.flesch_kincaid_grade(text)
    fKSAll = fleschIndex.fleschkincaid()
    fKSAll.sort(reverse=True)
    print(fKSAll)
    percentile = 100
    for i in range(len(fKSAll)):
        if flKinScore > fKSAll[i]:
            percentile = int(100 * (i / len(fKSAll)))
            break

    fKSContent = "Flesch-Kincaid Grade: {},\n which is in the {}th percentile.".format(flKinScore, percentile)
    fKSLbl = Label(root, text=fKSContent, font=12, pady=10)
    fKSLbl.pack()

    avgSentenceLen = int(len(text.split())/textstat.sentence_count(text))
    aSLAll = fleschIndex.avg_sentence_len()
    aSLAll.sort(reverse=True)
    print(aSLAll)
    percentile = 100
    for i in range(len(aSLAll)):
        if avgSentenceLen > aSLAll[i]:
            percentile = int(100 * (i / len(aSLAll)))
            break
    aSLContent = "Average Sentence Length is: {},\n which is in the {}th percentile.".format(avgSentenceLen, percentile)
    aSLLbl = Label(root, text=aSLContent, font=12, pady=10)
    aSLLbl.pack()

    predictedScore = predict_score(text)
    predictedScoreContent = "Regression Model Predicted Score is: {}.".format("{0:.2f}".format(predictedScore))
    pSLbl = Label(root, text=predictedScoreContent, font=12, pady=10)
    pSLbl.pack()

def get_me():
    url = simpledialog.askstring("input website", "please enter a website")
    if re.match(regex, url) is None:
        messagebox.showinfo("Wrong", "Invalid URL, try again!")
    else:
        s = scrape.scrapeUrl(url)
        if s == "":
            somethingwentwrong()
            return ""
        else:
            if 'www.' in url:
                company_name = "{0.netloc}".format(urlsplit(s)).split('.')[1]
            else:
                company_name = "{0.netloc}".format(urlsplit(s)).split('.')[0]
            try:
                html = urllib.request.urlopen(s, timeout=5).read().decode('utf-8')
                text = get_text(html)
                display_scores(company_name, text)
            except (urllib.error.HTTPError, urllib.error.URLError, timeout, http.client.HTTPException) as error:
                print(url + ": ", error)
                somethingwentwrong()
                return ""


root = Tk()

one = Label(root, text="Check Your Company's Privacy Policy Index", font=15, pady=10)
one.pack()
button = Button(root, text="enter a url", command=get_me)
button.pack()

root.geometry("500x500")
root.mainloop()
