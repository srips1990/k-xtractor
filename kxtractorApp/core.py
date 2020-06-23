#!/usr/bin/env python
# coding: utf-8

import nltk
import pandas as pd
import re
import string
import random
import os
from wordcloud import STOPWORDS
from nltk.stem import WordNetLemmatizer
from datauri import DataURI
from wordcloud import WordCloud
from . import appSettings


stopwords = nltk.corpus.stopwords.words('english')
ps = WordNetLemmatizer()

def compute(inp_text, inp_number):
    data = inp_text
    clean_word = clean_text(data)  # Cleaning the input data to remove unwanted characters and words
    listToStr = ' '.join([str(elem) for elem in clean_word])

    # a=int(input())
    a = int(inp_number)

    # Generate a word cloud image for most frequent words
    file1_name = wordcloud_gen_image(listToStr, a)

    frequency = {} # to get frequency of words
    for word in clean_word:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    newList =[]
    # Iterate over all the items in dictionary and filter items which has values equal to 1
    for (key, value) in frequency.items():      # Check if key is even then add pair to new dictionary
        if value <= 2:
            newList.append(key)

    # print(newList)
    listToStr1 = ' '.join([str(elem) for elem in newList])

    stop=['job', 'description', 'making', 'individual', 'collaborating', 'growing', 'part', 'organization', 'partner', 'purpose', 'world',
          'join', 'tangible', 'tasked', 'ideal', 'evaluate', 'responsible', 'global', 'applied', 'identifies', 'like', 'candidate', 'using', 'range',
          'background', 'solving', 'package', 'validity', 'real', 'true', 'false', 'complete', 'execute', 'well', 'multiple', 'subject', 'provide',
          'willing', 'related', 'action', 'matter', 'spanning']

    stop_words = stop + list(STOPWORDS)

    # Generate a word cloud image for least frequent words
    file2_name = wordcloud_gen_image(listToStr1, a, stop_words)

    file1_datauri = convert_file_to_dataURI(file1_name)
    file2_datauri = convert_file_to_dataURI(file2_name)

    return file1_datauri, file2_datauri
    # return file1_name, file2_name


# Convert image to DataURI and delete file
def convert_file_to_dataURI(file_name):
    file_path = os.path.join(appSettings.TEMP_FILES_DIR_PATH, file_name)
    data_uri = DataURI.from_file(file_path)
    os.unlink(file_path)
    return data_uri

# Generate a word cloud image
def wordcloud_gen_image(str_inp, num_of_words, stop_words=[]):
    if not stop_words:
        wordcloud = WordCloud(stopwords=stop_words, max_words=num_of_words, max_font_size=40).generate(str_inp)
    else:
        wordcloud = WordCloud(max_words=num_of_words, max_font_size=40).generate(str_inp)
    rand = random.randint(10000, 99999)
    file_name = "img" + str(rand) + ".png"
    wordcloud.to_file(os.path.join(appSettings.TEMP_FILES_DIR_PATH, file_name))
    return file_name


def clean_text(text):
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    tokens = re.split('\W+', text)
    text = [ps.lemmatize(word) for word in tokens if word not in stopwords]
    return text
