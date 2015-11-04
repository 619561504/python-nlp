# -*- coding:utf8 -*-
"""
    
"""
import codecs
import re
import jieba
import jieba.posseg
import nltk

__author__ = 'hanjiewu'

bank_pattern = re.compile(u'【([^】]*)】')

f = codecs.open('../data/fa1_head', mode='r', encoding='utf8')

sample = []
for f_line in f:
    f_line = f_line.strip().split('\t')[3]
    m = bank_pattern.search(f_line)
    if m:
        bank = m.group(1)

        for word, flag in jieba.posseg.cut(f_line):
            if flag not in ['m', 'w', 'x']:
                sample.append((bank, word))
cfdist = nltk.ConditionalFreqDist(sample)
f.close()

for c in cfdist.conditions():
    print c
print cfdist.tabulate(conditions=[u'中国邮政'], cumulative=True)