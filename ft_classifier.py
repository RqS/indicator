import sys
import random
import fasttext
import process_functions as pf
import json
import codecs
import numpy

data = sys.argv[1]
training_data = sys.argv[2]
result_data = sys.argv[3]


data_f = open(data, 'r')   #dataset containing training and test datasets
train_f = open(training_data, 'w')  # save as trainging datasets
result_f = codecs.open(result_data, 'w', 'utf-8')  #save as test prediction result

test_text, test_label = pf.generate_train_and_test(data_f, train_f)

data_f.close()
train_f.close()

#for word_ngrams in [1]:
num=0
for epoch in range(4, 21, 1):
	for dim in range(60, 220, 20):
		for lr in numpy.arange(0.01, 0.26, 0.01):
			num = num + 1
			print ("Tune parameter no.%d" %num)
			classifier = fasttext.supervised(training_data, "movement_model",
						lr=lr, dim=dim, epoch=epoch)
			predict_labels = classifier.predict(test_text)

			t_t = 0
                        t_f = 0
                        f_t = 0
                        f_f = 0
                        
			for i in range(len(predict_labels)):
				if test_label[i] == 'TRUE' and predict_labels[i][0].encode('utf-8') == 'TRUE':
                                        t_t += 1
                                elif test_label[i] == 'TRUE' and predict_labels[i][0].encode('utf-8') == 'FALSE':
                                        t_f += 1
                                elif test_label[i] == 'FALSE' and predict_labels[i][0].encode('utf-8') == 'TRUE':
                                        f_t += 1
                                elif test_label[i] == 'FALSE' and predict_labels[i][0].encode('utf-8') == 'FALSE':
                                        f_f += 1 

			this_result = {
				"prams": {
					"lr": lr,
					"dim": dim,
					"epoch": epoch,
                                        
				},
				"stats": {
					"t_t": t_t,
					"t_f": t_f,
					"f_t": f_t,
					"f_f": f_f,
					"precision": t_t / float(t_t + f_t),
					"recall": t_t / float(t_t + t_f)
				}
			}

			json.dump(this_result, result_f)
			result_f.write("\n")

result_f.close()

