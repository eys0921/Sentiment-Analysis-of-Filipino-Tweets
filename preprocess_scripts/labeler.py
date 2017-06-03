import os

POS_LABELS = 1698
NEG_LABELS = 1702
 
with open("ytrain.txt", 'w', encoding='utf-8') as fd:
    n = 0
    while n < NEG_LABELS:
        print("0", file=fd)
        n = n + 1

    n = 0
    while n < POS_LABELS
        print("1", file=fd)
        n = n + 1 
