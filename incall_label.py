import sys
import codecs
import json
import process_functions_with_neg as pf
import spacy
import incall_extractor

input_file = sys.argv[1]
positive_text = sys.argv[2]
negative_text = sys.argv[3]

nlp = spacy.load('en')
incall_matcher = incall_extractor.load_incall_matcher(nlp)
nlp = pf.prep_nlp(nlp)

positive_f = open(positive_text, 'w')
negative_f = open(negative_text, 'w')

with open(input_file, 'r') as f:
    for index, sentence in enumerate(f):
        if index % 10000 == 0:
            print "process line no.%d" %index
        t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=False)
        t_simple_tokens = pf.extract_tokens_from_crf(t)
        incall = incall_extractor.extract(nlp(t_simple_tokens), incall_matcher)
        this_label = pf.process_extracted(incall)
        if this_label == "TRUE":
            positive_f.write("__label__%s %s" % (this_label, sentence))
        else:
            negative_f.write("__label__%s %s" % (this_label, sentence))

positive_f.close()
negative_f.close()


