import os

def getLabels(filename):
    with open(filename, 'r', encoding='utf-8') as fd:
        content = fd.readlines()
        content_len = len(content)

        label_list = []
        n = 0
        while n < content_len:
            if content[n] == "0\n": 
                label_list.append(0)
            else:
                label_list.append(1)

            n = n + 1

    return label_list

