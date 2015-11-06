# -*- coding:utf8 -*-
"""
    
"""
from bs4 import BeautifulSoup

__author__ = 'hanjiewu'

import nltk
# from urllib import urlopen

# url = 'http://qq.com'
# raw = urlopen(url).read()
# print type(raw)

document = 'Corpus reader for the York-Toronto-Helsinki Parsed Corpus of Old\
English Prose (YCOE), a 1.5 million word syntactically-annotated\
corpus of Old English prose texts. The corpus is distributed by the\
Oxford Text Archive: http://www.ota.ahds.ac.uk/  It is not included\
with NLTK.'
tokens = nltk.word_tokenize(document)
print len(tokens)

print tokens
html_content = ''.join(open('../data/qq_index.html').readlines())
# raw = nltk.clean_html(html_content.decode('utf8'))
raw = BeautifulSoup(html_content).getText()
print raw