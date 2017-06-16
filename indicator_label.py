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
positive_text = sys.argv[2]
negative_text = sys.argv[3]


nlp = spacy.load('en')
movement_matcher = movement_extractor.load_movement_matcher(nlp)
#incall_matcher = incall_extractor.load_movement_matcher(nlp)
nlp = pf.prep_nlp(nlp)

positive_f = open(positive_text, 'w')
negative_f = open(negative_text, 'w')

with open(input_file, 'r') as f:
    for index, sentence in enumerate(f):
        if index % 10000 == 0:
            print "process line no.%d" %index
        t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=False)
        t_simple_tokens = pf.extract_tokens_from_crf(t)
        movement = movement_extractor.extract(nlp(t_simple_tokens), movement_matcher)
        #incall = incall_extractor.extract(nlp(t_simple_tokens), incall_matcher)
        this_label = pf.process_extracted(movement)
        if this_label == "TRUE":
            positive_f.write("__label__%s %s" % (this_label, sentence))
        else:
            negative_f.write("__label__%s %s" % (this_label, sentence))

positive_f.close()
negative_f.close()


