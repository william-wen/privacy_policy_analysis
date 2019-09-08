# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 03:11:32 2019

@author: yuche
"""
import pandas as pd

from sklearn.externals import joblib
from privacyDatabase import process_policy

def predict_score(txt:str) -> int:
    filename = 'finalized_model.sav'
    model = joblib.load(filename)
    data = [[txt, 0]]
    df = pd.DataFrame(data, column=['Policy', 'Score'])
    df['Policy'] = df['Policy'].apply(process_policy)
    predictions = model.predict(df)
    return predictions

    
    
    