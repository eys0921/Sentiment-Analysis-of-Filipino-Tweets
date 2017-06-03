import local_text_preprocessor as ltp

ltp.writeLabels("ytrain.txt", 7945, 11194)
ltp.writeLabels("ytest.txt", 195, 186)
ltp.writeLabels("ytest_neg.txt", 195, 0)
ltp.writeLabels("ytest_pos.txt", 0, 186)
