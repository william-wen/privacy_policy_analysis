# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 03:11:32 2019

@author: yuche
"""
import pandas as pd

from sklearn.externals import joblib
from privacyDatabase import process_policy
from inscriptis import get_text
from sklearn.feature_extraction.text import TfidfVectorizer

def predict_score(txt:str) -> int:
    filename = 'finalized_model.sav'
    model = joblib.load(filename)
    data = [[txt, 0]]
    df = pd.DataFrame(data, columns=['Policy', 'Score'])
    df['Policy'] = df['Policy'].apply(process_policy)

    vectorizer_filename = 'vectorizer.sav'
    tfidf = joblib.load(vectorizer_filename)
    df = tfidf.transform(df)
    predictions = model.predict(df)
    return predictions[0]

# f = open('Terms of Services/about.txt', 'r', encoding='utf-8')
# html = f.read()
# print(predict_score(html))
    
    
    