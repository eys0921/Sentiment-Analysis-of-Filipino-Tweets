from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SimpleRNN
from keras.preprocessing.text import Tokenizer
from keras import backend as k
from keras.utils import to_categorical
import numpy as np

vocab_file = 'data//vocab.txt'
xtrain_file = 'data//train//xtrain.txt'
ytrain_file = 'data//train//ytrain.txt'
xtest_file = 'data//test//xtest.txt'
xtest_file_neg = 'data//test//xneg_test.txt'
xtest_file_pos = 'data//test//xpos_test.txt'

max_features = 10000
maxlen = 50  # cut texts after this number of words (among top max_features most common words)
batch_size = 64

# Load Data
def read_data(fname):
    data = []
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.readlines()
    for x in content:
        data.append(x)
    return data

# Build Vocabulary of words
vocab_data = read_data(vocab_file)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(vocab_data)
#print(tokenizer.word_index)
#print(max((tokenizer.word_index).values()))

# Build Dataset according to the vocabulary
xtrain_data = read_data(xtrain_file)
xtest_data_neg = read_data(xtest_file_neg)
xtest_data_pos = read_data(xtest_file_pos)
xtest_data = read_data(xtest_file)


n = 0
x_test = []
while (n < 381):
    halo = tokenizer.texts_to_sequences([xtest_data[n]])
    x_test.append(halo[0])
    n = n + 1

n = 0
x_train = []
while (n < 19139):
    halo = tokenizer.texts_to_sequences([xtrain_data[n]])
    x_train.append(halo[0])
    n = n + 1

n = 0
x_test_neg = []
while (n < 195):
    halo = tokenizer.texts_to_sequences([xtest_data_neg[n]])
    x_test_neg.append(halo[0])
    n = n + 1

n = 0
x_test_pos = []
while (n < 186):
    halo = tokenizer.texts_to_sequences([xtest_data_pos[n]])
    x_test_pos.append(halo[0])
    n = n + 1

n = 0
y_test_neg = []
while n < 195:
    y_test_neg.append(0)
    n = n + 1

n = 0
y_test_pos = []
while n < 186:
    y_test_pos.append(1)
    n = n + 1

n = 0
y_test = []
while n < 195:
    y_test.append(0)
    n = n + 1 

while n < 195 + 186:
    y_test.append(1)
    n = n + 1        

n = 0
y_train = []
while n < 7945:
    y_train.append(0)
    n = n + 1

while n < 7945 + 11194:
    y_train.append(1)
    n = n + 1


# Pad Sequences ?? THE HECK IS THIS ??
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test_neg = sequence.pad_sequences(x_test_neg, maxlen=maxlen)
x_test_pos = sequence.pad_sequences(x_test_pos, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

# Print data
print(len(x_train))
print(len(y_train))

#while 1 == 1:
#    continue

print('Build model...')
model = Sequential()
model.add(Embedding(max_features, maxlen))
model.add(LSTM(64, dropout=0.8))
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
n = 1
while n <= 5: 
    model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=1,
          validation_data=(x_test, y_test))
    score, acc1 = model.evaluate(x_test_neg, y_test_neg,
                            batch_size=batch_size)
    print('Neg Test score:', score)
    print('Test accuracy:', acc1)

    score, acc2 = model.evaluate(x_test_pos, y_test_pos,
                            batch_size=batch_size)
    print('Pos Test score:', score)
    print('Test accuracy:', acc2)

    print("mean: ", (acc1 + acc2 )/2)

    n = n + 1
#model.save('pretrained')
#print(x_test)
#print(y_test)
score, acc1 = model.evaluate(x_test_neg, y_test_neg,
                            batch_size=batch_size)
print('Neg Test score:', score)
print('Test accuracy:', acc1)

score, acc2 = model.evaluate(x_test_pos, y_test_pos,
                            batch_size=batch_size)
print('Pos Test score:', score)
print('Test accuracy:', acc2)

print("mean: ", (acc1 + acc2 )/2)

test1 = "Sana magonline si"
test2 = "Ang ganda mo"

man_test1 = []
halo1 = tokenizer.texts_to_sequences([test1])
man_test1.append(halo1[0])
man_test1 = sequence.pad_sequences(man_test1, maxlen=maxlen)

print(man_test1)
print([0])

n = 0
c = 0
"""
while (n < 128):
    halo = tokenizer.texts_to_sequences([xtest_data_neg[n]])
    temp_list = []
    temp_list.append(halo[0])
    temp_list.append(halo[0])
    temp_list = sequence.pad_sequences(temp_list, maxlen=maxlen)
    score1, acc1 = model.evaluate(temp_list, [1,1],
                            batch_size=2)
    if (acc1 == 1):
        print(xtest_data_neg[n])
    n = n + 1
"""
"""
while (n < 94):
    halo = tokenizer.texts_to_sequences([xtest_data_pos[n]])
    temp_list = []
    temp_list.append(halo[0])
    temp_list.append(halo[0])
    temp_list = sequence.pad_sequences(temp_list, maxlen=maxlen)
    score1, acc1 = model.evaluate(temp_list, [1,1],
                            batch_size=2)
    if (acc1 == 0):
        print(xtest_data_pos[n])
    n = n + 1

"""
"""
while True:
    print("Maglagay ng pangungusap")
    sentence = input()
    num_array = tokenizer.texts_to_sequences([sentence])
    num_array = sequence.pad_sequences(num_array, maxlen=maxlen)
    predixion = model.predict(num_array[0], batch_size = 1, verbose = 0)
    #print(num_array[0])
    print(predixion)
    continue
    if (predixion == 0):
        print("Negative")
    else:
        print("Postive")
"""

while True:
    print("Maglagay ng pangungusap")
    sentence = input()
    sentence = sentence.lower()
    temp_list = []
    temp_list.append(tokenizer.texts_to_sequences([sentence])[0])
    temp_list.append(tokenizer.texts_to_sequences([sentence])[0])
    temp_list = sequence.pad_sequences(temp_list, maxlen=maxlen)
    score1, acc1 = model.evaluate(temp_list, [1,1],
                            batch_size=2)

    if (acc1 == 0):
        print("Negative")
    else:
        print("Positive")

# Fixes error message after testing phase
k.clear_session()
