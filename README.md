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
![Results](https://puu.sh/wfWdE/7b173f214e.PNG)

## Example of tweets wrongly classified
![Examples](https://puu.sh/wfWdN/85d06eb7f2.PNG)

### How should I cite this repo?

Please cite this study in your publications if it helps your research. Here is an example BibTeX entry:

```
@misc{MinaFilipinoSentiment,
  title={Sentiment Analysis of Filipino Tweets Using Recurrent Neural Network},
  author={Mina, Rusty John Lloyd and Atienza, Rowel},
  year={2017},
  publisher={GitHub},
  howpublished={\url{https://github.com/iamRusty/Sentiment-Analysis-of-Filipino-Tweets}},
}
```

## Files yet to be posted
1. Raw and Unprocessed JSON data of tweets (around 8GB)
2. Scripts for processing JSON of tweets to text of tweets
3. Scripts for getting stream of Tweets 


## Attributions
[NB-SVM Implementation](https://github.com/iamRusty/Sentiment-Analysis-of-Filipino-Tweets/tree/master/nbsvm) used in this paper is based off the work by Grégoire Mesnil [Naive Bayes SVM](https://github.com/mesnilgr/nbsvm). 

[Naive Bayes SVM](https://github.com/mesnilgr/nbsvm) is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).
