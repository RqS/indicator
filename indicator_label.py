import sys
import codecs
import json
import process_functions as pf
import spacy
import movement_extractor

input_file = '/Users/runqishao/Downloads/eccie_1000_content_result.jl'
text_part = 'content_relaxed'
#input_file = argv[1]
#output_file = argv[2]
#text_part = argv[3]
nlp = spacy.load('en')
matcher = movement_extractor.load_movement_matcher(nlp)

text = pf.process_text(input_file, text_part)

doc = dict()
doc_extracted = dict()
nlp = pf.prep_nlp(nlp)
for i in range(len(text)):
    doc[i] = pf.split_line(text[i].encode("utf-8"))
    doc_extracted[i] = []
    for sentence in doc[i]:
        t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=False)
        t_simple_tokens = pf.extract_tokens_from_crf(t)
        movement = movement_extractor.extract(nlp(t_simple_tokens), matcher)
        doc_extracted[i].append(movement)
