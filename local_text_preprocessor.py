import os
from keras.preprocessing import sequence

# Read label values from filename
def readLabels(filename):
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

# Write label values to filename
def writeLabels(filename, NEG_LABELS, POS_LABELS):
    with open(filename, 'w', encoding='utf-8') as fd:
        n = 0
        while n < NEG_LABELS:
            print("0", file=fd)
            n = n + 1

        n = 0
        while n < POS_LABELS:
            print("1", file=fd)
            n = n + 1 

# Reads filename and return list of lines in filename
def readFileLines(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as fd:
        content = fd.readlines()
    for x in content:
        data.append(x)
    return data

# Build a dataset that can be read by the model
def buildDataset(tokenizer, filename, pad_len):
    content = readFileLines(filename)
    content_len = len(content)

    data = []
    n = 0
    # Sequence of words to sequence of numbers(integers)
    while n < content_len:
        temp = tokenizer.texts_to_sequences([content[n]])
        data.append(temp[0])
        n = n + 1

    # Pad sequences (the model can't process sequence of difference lengths)
    data = sequence.pad_sequences(data, maxlen=pad_len)

    return data