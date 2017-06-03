from itertools import chain
from glob import glob

file = open('vocab.txt', 'r', encoding='utf-8')

lines = [line.lower() for line in file]
with open('vocab.txt', 'w', encoding='utf-8') as out:
     out.writelines(sorted(lines))