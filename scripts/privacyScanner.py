#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:10:13 2019

@author: willwen
"""
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from collections import Counter


f = open("Facebook.txt", "r")
text = f.read()
split_text = text.split()
Counter = Counter(split_text)
most_occur = Counter.most_common(100)

bans = ['the', 'and', 'to', 'To','of', 'or', 'that', 'as', 'in', 'is', 'on', 'a', 'by', 'are']
for i in most_occur:
    if i[0] in bans:
        most_occur.remove(i)
        
print(most_occur)

