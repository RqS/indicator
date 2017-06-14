import sys
import codecs
import json
import process_functions as pf
import spacy
import movement_extractor
#import incall_extractor
#import fasttext
#import random

#input_file = '/Users/runqishao/Downloads/eccie_1000_content_result.jl'
#text_part = 'content_relaxed'
#output_file = '/Users/runqishao/Downloads/label_result.jl'
input_file = sys.argv[1]
#output_file = sys.argv[2]
#text_part = sys.argv[2]
positive_text = sys.argv[2]
negative_text = sys.argv[3]
#train_text = sys.argv[4]
#test_text = sys.argv[5]
#text_for_vector = sys.argv[6]

nlp = spacy.load('en')
movement_matcher = movement_extractor.load_movement_matcher(nlp)
#incall_matcher = incall_extractor.load_movement_matcher(nlp)
nlp = pf.prep_nlp(nlp)

#output = codecs.open(output_file, 'w', 'utf-8')
#train_output = open(output_for_train, 'w')
positive_f = open(positive_text, 'w')
negative_f = open(negative_text, 'w')
#train_f = open(train_text, 'w')
#test_f = open(test_text, 'w')
#vector_text = open(text_for_vector, 'w')

#text_type=['content_strict', 'content_relaxed', 'title']
#total=0
#p_num = 0
#n_num = 0
with open(input_file, 'r') as f:
    for index, line in enumerate(f):
        if index % 10000 == 0:
            print "process line no.%d" %index
        content_doc = pf.split_line(line)
        for sentence in content_doc:
            t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=False)
            t_simple_tokens = pf.extract_tokens_from_crf(t)
            movement = movement_extractor.extract(nlp(t_simple_tokens), movement_matcher)
            #incall = incall_extractor.extract(nlp(t_simple_tokens), incall_matcher)
            this_label = pf.process_extracted(movement)
            #this_label[movement] = pf.process_extracted(movement)
            #this_label[incall] = pf.process_extracted(incall)
            if this_label == "TRUE":
                #p_num = p_num + 1
                positive_f.write("__label__%s %s\n" % (this_label, sentence))
                #r = random.random()
                #if r <= 0.5:
                #    train_f.write("__label__%s %s\n" % (this_label, sentence))
                #else:
                #    test_f.write("__label__%s %s\n" % (this_label, sentence))
            else:
                #n_num = n_num + 1
                negative_f.write("__label__%s %s\n" % (this_label, sentence))
            #pf.write_text(positive_f, negative_f, this_label, sentence)
            # this_result = {
            #     "label": this_label,
            #     "text": sentence,
            #     "extracted": str(movement),
            # }
#            total=total+1
#            content_result.append(this_result)
#            json.dump(this_result, output)
#            output.write('\n')

#output.close()
#train_output.close()
positive_f.close()
negative_f.close()

# sample_idx = sorted(random.sample(range(n_num), p_num))
# p = 0

# with open(negative_text, 'r') as f:
#     for index, line in enumerate(f):
#         if p < p_num and index ==  sample_idx[p]:
#             r = random.random()
#             if r <= 0.5:
#                 train_f.write("%s\n" % line)
#             else:
#                 test_f.write("%s\n" % line)
#             p = p + 1

# train_f.close()
# test_f.close()
#vector_text.close()

# vector_model = fasttext.skipgram('text/movement_text_vector.txt', 
#     'text/movement_vector_model', lr=0.1, dim=300, epoch=20)

# classifier = fasttext.supervised('text/movement_train.txt', 'text/movement_classifier_model', 
#     pretrained_vectors = 'text/movement_vector_model.vec', dim=300, lr=0.2, epoch=20)


# classifier = fasttext.supervised(output_for_train, 'model', label_prefix='__LABEL__')
# print classifier.labels

# texts = []
# with open(text_for_test, 'r') as f:
#     for line in f:
#         texts.append(line.strip().decode("utf-8"))

# labels=[]
# with open(label_for_test, 'r') as f:
#     for line in f:
#         labels.append(line.strip())

# predict_labels = classifier.predict(texts)
# tp=0
# p_p = 0
# c_p = 0
# for i in range(len(predict_labels)):
#     if predict_labels[i][0] == "TRUE":
#         p_p = p_p + 1
#     if labels[i] == "TRUE":
#         c_p = c_p + 1
#     if predict_labels[i][0] == labels[i] and labels[i] == "TRUE":
#         tp = tp + 1

# print "training sample number: %d" %(total-len(predict_labels))
# print "testing number: %d" %len(predict_labels)
# print "precision: %f" %(tp/float(p_p))
# print "recall: %f" %(tp/float(c_p))
