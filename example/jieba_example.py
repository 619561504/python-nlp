# -*- coding:utf8 -*-
"""
    
"""
import jieba.posseg

__author__ = 'hanjiewu'
sms_text = '尊敬的李允信客户，您在深圳分行的贷款本期已足额还款100元，现贷款余额 {2} 元，详询平安银行 {3} - {4} 。【中国平安】'

flag_name_map = {}
for f_line in open('../jieba/pos_name.txt').readlines():
    fields = f_line.strip().split('\t')
    flag_name_map[fields[0]] = fields[1]

for word, flag in jieba.posseg.cut(sms_text):
    flag_name = flag_name_map[flag] if flag in flag_name_map else flag
    print word, flag_name
