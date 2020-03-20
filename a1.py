import os
import sys
import pandas as pd
import numpy as np
import numpy.random as npr

# ADDED IMPORTS: 
from os import walk
from os.path import join
import re
import math 

# "HELPER" FUNCTIONS:
def get_files(folder1, folder2):
    f = []
    for (root, dirnames, _) in walk('.'): #if grain/crude are in same directory as code, otherwise change expression in 'walk'
        for dirname in dirnames:
            if dirname == folder1 or dirname == folder2:
                subfolder = os.path.join(root, dirname)
                for (_, _, filenames) in walk(subfolder):
                    for filename in filenames:
                        f.append(os.path.join(subfolder, filename))
    return f

#function to get all unique words used in an article, ignoring spelling with big letters 
def get_words(path):
    with open(path, 'r') as article:
        content = article.read().lower()
        words = re.findall(r'\w+', content) #as 'content.split()' would exclude words in brackets like "(word)"
        filtered = [x for x in words if re.match('[a-z]+', x)] # alternative: x.isalpha
        return filtered

#function to count words
def get_word_counts(words):
    word_counts = {}
    unique_words = set(words)
    for word in unique_words:
        word_counts[word] = words.count(word)
    return word_counts

#### PART 1:
def part1_load(folder1, folder2, n=1):
    all_files = get_files(folder1, folder2)
    all_words=[]
    all_subfolders=[]
    all_files1=[]
    for article in all_files:
        words = get_words(article)
        word_counts=get_word_counts(words)
        all_words.append(word_counts)
        A = list(reversed(article.split(os.sep))) #Helper variable to extract file/foldernames
        all_subfolders.append(A[1]) #foldernames
        all_files1.append(A[0].split('.')[0]) #articlenames

    arrays = [np.asarray(all_files1), np.asarray(all_subfolders)]
    idx = pd.MultiIndex.from_arrays(arrays, names=('article', 'folder')) # multiindex category 'folder' could be converted to a regular column: df = df.reset_index(level='folder')
    df = pd.DataFrame(all_words, index=idx)
    df = df.fillna(0) 
    df_sum = df.sum() #global wordcount 

    # delete columns of words that occur less than n times in df
    for key, value in df_sum.items():
        if value < n:
            del df[key]
    return df

#### PART 2:
def part2_vis(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    df_sum = df.sum() #global wordcount
    df_folders = df.sum(level='folder') # wordcount per folder
    df_top_n = df_sum.nlargest(n=10) #n most used words

    word_index = []
    crude = []
    grain = []
    for key, _ in df_top_n.items():
        word_index.append(key)
        crude.append(df_folders[key][0])
        grain.append(df_folders[key][1])

    df_plot = pd.DataFrame({'crude': crude, 'grain': grain}, index=word_index)
    return df_plot.plot.bar(rot=0)


#### PART 3:
def part3_tfidf(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    df_tfidf = df.copy()
    N = df_tfidf.shape[0] # total amount of documents, alternative: len(df.index)
    K = df_tfidf.shape[1] # total amount of articles
    d = (df > 0).sum(axis=0) # amount of articles that contain the word

    k=0
    while k < K: #iterates through every column in df
        a = 0
        while a < N: # iterates through every row in df
            if df_tfidf.iat[a, k] != 0:
                df_tfidf.iat[a, k] = df_tfidf.iat[a, k] * math.log(N/d[k]) #change value in row a, column k to tfidf value
            a=a+1
        k=k+1
    return df_tfidf