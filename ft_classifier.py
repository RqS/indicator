import sys
import random
import fasttext
import process_functions as pf

data = sys.argv[1]
training_data = sys.argv[2]
#training_data = '/Users/runqishao/Desktop/dig_indicator/training_data.txt'
#data = '/Users/runqishao/Desktop/dig_indicator/dataset.txt'

data_f = open(data, 'r')
train_f = open(training_data, 'w')

test_text, test_label = pf.generate_train_and_test(data_f, train_f)

data_f.close()
train_f.close()

for epoch in range(21)[4:]:
	classifier = fasttext.supervised(train_f, 'movement_classify_model',
				dim=200, word_ngrams=2, lr=0.2, epoch=epoch)

