echo "BI-GRAM";
python ../nbsvm/nbsvm.py --liblinear liblinear-1.96 --ptrain ../data/clean/xpos_train_clean.txt --ntrain ../data/clean/xneg_train_clean.txt --ptest ../data/test/xtest_pos.txt --ntest ../data/test/xtest_neg.txt --ngram 12 --out NBSVM-TEST-BIGRAM
echo "TRI-GRAM";
python ../nbsvm/nbsvm.py --liblinear liblinear-1.96 --ptrain ../data/clean/xpos_train_clean.txt --ntrain ../data/clean/xneg_train_clean.txt --ptest ../data/test/xtest_pos.txt --ntest ../data/test/xtest_neg.txt --ngram 123 --out NBSVM-TEST-TRIGRAM
cd ../nbsvm
