import random
import os



with open("lahat_pos.txt", 'r', encoding='utf-8') as neg_clean:
    content1 = neg_clean.readlines()

with open("xpos_test.txt", 'r', encoding='utf-8') as xneg_test:
    content2 = xneg_test.readlines()

n = 0
with open("xpos_train.txt", 'w', encoding='utf-8') as ostr:
    while n < len(content1):
        if content1[n] not in content2:
            print(content1[n].rstrip('\n'), file=ostr)    
        n = n + 1

