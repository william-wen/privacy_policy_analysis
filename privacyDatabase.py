#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 04:19:51 2019

@author: willwen
"""

import pandas as pd
import numpy as np

import re
import nltk

from string import punctuation

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
# Classification
from sklearn import svm 
# Regression
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import tree
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def process_policy(policy, lower_case = True, stem = True, stop_words = True):
    # Get rid of newlines
    policy = policy.replace('\n', ' ').rstrip()
    # Get rid of puntuation
    policy = strip_punctuation(policy)
    # One space in between each string
    policy = re.sub(" +", ' ', policy)
    # Make Lower Case
    if lower_case:
        policy = policy.lower()
    # Tokenize
    policy = word_tokenize(policy)
    # Remove Small Words
    if stop_words:
        sw = stopwords.words('english')
        policy = [word for word in policy if word not in sw]
    # Add Stemming
    if stem:
        stemmer = PorterStemmer()
        stemmed_policy = " ".join([stemmer.stem(word) for word in policy])
    return stemmed_policy

policies = pd.read_excel('hello.xlsx')
combine = [policies]

# Preprocess All Data
policies['Policy'] = policies['Policy'].apply(process_policy)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(policies['Policy'], policies['Score'], test_size = 0.1, random_state = 1)
m = y_test.size
# TF-IDF and Vectorization
tfidf = TfidfVectorizer()
X_train = tfidf.fit_transform(X_train)
X_test = tfidf.transform(X_test)

# Training SVM classifier
# svm = svm.SVC(C=1000, gamma='auto')
# svm.fit(X_train, y_train)

# Training Polynomial Regression Classifier
# poly = PolynomialFeatures(degree = 2)
# X_train = poly.fit_transform(X_train)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = np.sum((y_pred - y_test)**2)
rmse = np.sqrt(mse/m)
# print(rmse)

# Test against Test Set 
# X_test = tfidf.transform(X_test)
# y_pred = svm.predict(X_test)
# print(y_pred)
# print(confusion_matrix(y_test, y_pred))

