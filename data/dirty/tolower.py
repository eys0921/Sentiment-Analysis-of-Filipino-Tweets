from itertools import chain
from glob import glob

file = open('lahat.txt', 'r', encoding='utf-8')

lines = [line.lower() for line in file]
with open('lahat.txt', 'w', encoding='utf-8') as out:
     out.writelines(sorted(lines))