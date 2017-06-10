# Sentiment-Analysis-of-Filipino-Tweets

Implementation of proposed [deep learning approach discussed in this paper](https://github.com/iamRusty/Sentiment-Analysis-of-Filipino-Tweets/blob/master/Sentiment%20Analysis%20of%20Filipino%20Tweets.pdf), to sentiment analysis of Filipino tweets.

## Dependencies
Keras 2.0

    $ pip install keras

## How to run
using augmented(tweets with repetition) data:

    $ python tf_builddata.py
    
using clean data:

    $ python tf_builddata_clean.py

using machine learning approach:

    $ cd nbsvm
    $ ./oh_my_go.sh

## Results
![Results](https://puu.sh/wfVFV/45ac583af5.PNG)

## Example of tweets wrongly classified
![Examples](https://puu.sh/wfVHC/14626c0892.PNG)

## Attributions
[NB-SVM Implementation](https://github.com/iamRusty/Sentiment-Analysis-of-Filipino-Tweets/tree/master/nbsvm) used in this paper is based off the work by Grégoire Mesnil [Naive Bayes SVM](https://github.com/mesnilgr/nbsvm). 

[Naive Bayes SVM](https://github.com/mesnilgr/nbsvm) is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).

## Files yet to be posted
1. Raw and Unprocessed JSON data of tweets (around 8GB)
2. Scripts for processing JSON of tweets to text of tweets
3. Scripts for getting stream of Tweets 
