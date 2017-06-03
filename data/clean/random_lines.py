import random
import os

with open("xneg_train_new.txt", 'w', encoding='utf-8') as ostr:
    n = 0
    while n < 1702:
        line = random.choice(open('xneg_train_clean.txt', encoding='utf-8').readlines())
        with open("xneg_train_new.txt", 'r', encoding='utf-8') as ostr2:
            content = ostr2.readlines()
        if line in content:
            continue
        print(line.rstrip('\n'), file=ostr)
        n = n + 1