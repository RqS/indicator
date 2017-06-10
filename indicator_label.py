import sys
import codecs
import json
import process_functions as pf
import spacy
import movement_extractor

#input_file = '/Users/runqishao/Downloads/eccie_1000_content_result.jl'
#text_part = 'content_relaxed'
#output_file = '/Users/runqishao/Downloads/label_result.jl'
input_file = sys.argv[1]
output_file = sys.argv[2]
text_part = sys.argv[3]

nlp = spacy.load('en')
matcher = movement_extractor.load_movement_matcher(nlp)
nlp = pf.prep_nlp(nlp)

output = codecs.open(output_file, 'w', 'utf-8')

#text_type=['content_strict', 'content_relaxed', 'title']

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
            movement = movement_extractor.extract(nlp(t_simple_tokens), matcher)
            this_label = pf.process_extracted(movement)
            this_result = {
                "label": this_label,
                "text": sentence,
                "extracted": str(movement),
            }
#            content_result.append(this_result)
            json.dump(this_result, output)
            output.write('\n')

output.close()

#text = pf.process_text(input_file, text_part)

#doc = dict()
#doc_extracted = dict()
#label = dict()
# for i in range(len(text)):
#     print "process text no.%d" %i
#     doc[i] = pf.split_line(text[i].encode("utf-8"))
#     doc_extracted[i] = []
#     label[i] = []
#     for sentence in doc[i]:
#         t = pf.extract_crftokens(sentence.decode("utf-8"), lowercase=False)
#         t_simple_tokens = pf.extract_tokens_from_crf(t)
#         movement = movement_extractor.extract(nlp(t_simple_tokens), matcher)
#         doc_extracted[i].append(movement)
#         this_label = pf.process_extracted(movement)
#         label[i].append(this_label)
