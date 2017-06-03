from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SimpleRNN
from keras.preprocessing.text import Tokenizer
from keras import backend as k
from keras.utils import to_categorical
import numpy as np
import local_text_preprocessor as ltp

# Dataset filenames
vocab_file = 'data//vocab.txt'
xtrain_file = 'data//train//xtrain.txt'
ytrain_file = 'data//train//ytrain.txt'
xtest_file = 'data//test//xtest.txt'
xtest_file_neg = 'data//test//xtest_neg.txt'
xtest_file_pos = 'data//test//xtest_pos.txt'
ytest_file = 'data//test//ytest.txt'
ytest_file_neg = 'data//test//ytest_neg.txt'
ytest_file_pos = 'data//test//ytest_pos.txt'

# Model Hyperparameters
max_features = 10000
maxlen = 50  # cut texts after this number of words (among top max_features most common words)
batch_size = 64

# Initialize Tokenizer constructor
tokenizer = Tokenizer()

# Build Vocabulary of words
vocab_data = ltp.readFileLines(vocab_file)
tokenizer.fit_on_texts(vocab_data)

# Build Dataset according to the vocabulary
xtrain = ltp.buildDataset(tokenizer, xtrain_file, maxlen)
xtest = ltp.buildDataset(tokenizer, xtest_file, maxlen)
xtest_neg = ltp.buildDataset(tokenizer, xtest_file_neg, maxlen)
xtest_pos = ltp.buildDataset(tokenizer, xtest_file_pos, maxlen)

# Get labels
ytrain = ltp.readLabels(ytrain_file)
ytest = ltp.readLabels(ytest_file)
ytest_neg = ltp.readLabels(ytest_file_neg)
ytest_pos = ltp.readLabels(ytest_file_pos)

# Build model
print('Build model...')
model = Sequential()
model.add(Embedding(max_features, maxlen))
model.add(LSTM(64, dropout=0.8))
model.add(Dense(1, activation='sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Train model
print('Train...')
n = 1
while n <= 5: 
    model.fit(xtrain, ytrain,
          batch_size=batch_size,
          epochs=1,
          validation_data=(xtest, ytest))
    score, acc1 = model.evaluate(xtest_neg, ytest_neg,
                            batch_size=batch_size)
    print('\nNeg Test score:', score)
    print('Test accuracy:', acc1)

    score, acc2 = model.evaluate(xtest_pos, ytest_pos,
                            batch_size=batch_size)
    print('\nPos Test score:', score)
    print('Test accuracy:', acc2)

    print("mean: ", (acc1 + acc2 )/2)

    n = n + 1

# Save model
#model.save('pretrained')

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
