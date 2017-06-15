import sys
import random
import fasttext
import process_functions as pf
import json
import codecs


data = sys.argv[1]
training_data = sys.argv[2]
result_data = sys.argv[3]
#training_data = '/Users/runqishao/Desktop/dig_indicator/training_data.txt'
#data = '/Users/runqishao/Desktop/dig_indicator/dataset.txt'

data_f = open(data, 'r')
train_f = open(training_data, 'w')
result_f = codecs.open(result_data, 'w', 'utf-8')

test_text, test_label = pf.generate_train_and_test(data_f, train_f)

data_f.close()
train_f.close()

#for word_ngrams in [1]:
num=0
for epoch in range(4, 21, 2):
	for neg in range(4, 17, 2):
		for lr in [x / 100.0 for x in range(5, 51, 5)]:
			num = num + 1
			print ("Tune parameter no.%d" %num)
			model_name = "movement_model/movement_classifier"
			model_name = model_name+"_lr_"+str(lr)+"_neg_"+str(neg)+"_epoch_"+str(epoch)
			classifier = fasttext.supervised(training_data, model_name,
						dim=200, lr=lr, epoch=epoch, neg=neg)
			predict_labels = classifier.predict(test_text)

			tp=0
			fp = 0
			tn = 0
			fn = 0
			for i in range(len(predict_labels)):
			    if predict_labels[i][0] == "TRUE" and test_label[i] == "FALSE":
			        fp = fp + 1
			    elif test_label[i] == "TRUE" and predict_labels[i][0] == "FALSE":
			        fn = fn + 1
			    elif predict_labels[i][0] == "TRUE" and test_label[i] == "TRUE":
			        tp = tp + 1
			    else:
			    	tn = tn + 1

			this_result = {
				"prams": {
					"lr": lr,
					"neg": neg,
					"epoch": epoch
				},
				"stats": {
					"tp": tp,
					"fp": fp,
					"fn": fn,
					"tn": tn,
					"precision": tp/float(fp+tp),
					"recall": tp/float(tp+fn)
				}
			}

			json.dump(this_result, result_f)


