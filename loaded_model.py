# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 03:11:32 2019

@author: yuche
"""
import pandas as pd

import joblib
import re
from privacyDatabase import process_policy
from inscriptis import get_text
from sklearn.feature_extraction.text import TfidfVectorizer

def predict_score(txt:str) -> int:
    txt = re.sub('[^a-zA-Z\d\s:]', '', txt)
    filename = 'finalized_model.sav'
    vectorizer_name = 'vectorizer.sav'

    model = joblib.load(filename)
    data = [[txt]]
    df = pd.DataFrame(data, columns=['Policy'])
    df['Policy'] = df['Policy'].apply(process_policy)

    tfidf = joblib.load(vectorizer_name)
    df = tfidf.transform(df['Policy'])
    predictions = model.predict(df)
    return predictions[0]

# f = open('Terms of Services/ted.txt', 'r', encoding='utf-8')
# text = re.sub('[^a-zA-Z\d\s:]', '', f.read())
# print(predict_score(text))
    
    
    