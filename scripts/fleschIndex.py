"""
this returns defferent scores of the policies, the higher the better
"""
import pandas as pd
import textstat
from typing import List

policies = pd.read_excel('./files/hello.xlsx')


def fleschscore() -> List:
    """return flesch reading ease score
    """
    flesch_list = []
    for text in policies['Policy']:
            flesch_list.append(textstat.flesch_reading_ease(text))
    return flesch_list


def avg_sentence_len() -> List:
    """return sentence length in each policy
    """
    count = []
    for text in policies['Policy']:
        w_count = len(text.split())
        count.append(int(w_count/textstat.sentence_count(text)))
    return count


def fleschkincaid() -> List:
    """returns Flesch-Kincaid score
    """
    score = []
    for text in policies['Policy']:
        score.append(textstat.flesch_kincaid_grade(text))
    return score
