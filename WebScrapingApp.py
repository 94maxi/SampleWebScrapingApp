#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import requests
import urllib.request
import csv
import pandas as pd
from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import Counter
from django.conf.urls import url, include
from django.contrib import admin
import random
import re


df = pd.read_csv('Positive_Reviews_GM.csv', sep = ',', engine='python')
df.head()


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)




df_list = []


for i in range(len(df.urls)):
        try:
            req = urllib.request.Request(df.urls[i], headers={'User-Agent': 'Mozilla/5.0'})
            fp = urllib.request.urlopen(req).read()
            l = text_from_html(fp)
            df_list.append(l)
            
        except:
            print (f"Something is wrong with {df.urls[i]} this URL is broken for some reason.")
            continue
df_pd = pd.DataFrame({'review':df_list})




df_pd.to_csv('test.csv')

