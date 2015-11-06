# -*- coding:utf8 -*-
"""
    
"""

import nltk
__author__ = 'hanjiewu'

text = nltk.word_tokenize('And now for something completely different')
print nltk.pos_tag(text)
