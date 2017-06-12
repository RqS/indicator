import sys
import codecs
import json
import process_functions as pf
import spacy
import incall_extractor
import fasttext

#input_file = '/Users/runqishao/Downloads/eccie_1000_content_result.jl'
#text_part = 'content_relaxed'
#output_file = '/Users/runqishao/Downloads/label_result.jl'
input_file = sys.argv[1]
output_file = sys.argv[2]
text_part = sys.argv[3]
output_for_train = sys.argv[4]
text_for_test = sys.argv[5]
label_for_test = sys.argv[6]

nlp = spacy.load('en')
matcher = incall_extractor.load_incall_matcher(nlp)
nlp = pf.prep_nlp(nlp)

output = codecs.open(output_file, 'w', 'utf-8')
train_output = open(output_for_train, 'w')
test_text = open(text_for_test, 'w')
test_label = open(label_for_test, 'w')

#text_type=['content_strict', 'content_relaxed', 'title']
total=0
with codecs.open(input_file, 'r', 'utf-8') as f:
    for index, line in enumerate(f):
#        content_result = []
        doc = json.loads(line)
        content = doc['content_extraction'][text_part]['text']
        print "process text no.%d" %index
        content_doc = pf.split_line(content.encode("utf-8"))
        for sentence in content_doc:
            t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=False)
            t_simple_tokens = pf.extract_tokens_from_crf(t)
            incall = incall_extractor.extract(nlp(t_simple_tokens), matcher)
            this_label = pf.process_extracted(incall)
            pf.write_text(train_output, test_text, test_label, this_label, sentence)
            this_result = {
                "label": this_label,
                "text": sentence,
                "extracted": str(incall),
            }
            total=total+1
#            content_result.append(this_result)
            json.dump(this_result, output)
            output.write('\n')

output.close()
train_output.close()
test_text.close()
test_label.close()
 
classifier = fasttext.supervised(output_for_train, 'model', label_prefix='__LABEL__')
print classifier.labels

texts = []
with open(text_for_test, 'r') as f:
    for line in f:
        texts.append(line.strip().decode("utf-8"))

labels=[]
with open(label_for_test, 'r') as f:
    for line in f:
        labels.append(line.strip())

predict_labels = classifier.predict(texts)
tp=0
p_p = 0
c_p = 0
for i in range(len(predict_labels)):
    if predict_labels[i][0] == "TRUE":
        p_p = p_p + 1
    if labels[i] == "TRUE":
        c_p = c_p + 1
    if predict_labels[i][0] == labels[i] and labels[i] == "TRUE":
        tp = tp + 1

print "training sample number: %d" %(total-len(predict_labels))
print "testing number: %d" %len(predict_labels)
print "precision: %f" %(tp/float(p_p))
print "recall: %f" %(tp/float(c_p))
