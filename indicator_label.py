import sys
import codecs
import json
import process_functions as pf

input_file = argv[1]
output_file = argv[2]
text_part = argv[3]

text = pf.process_text(input_file, text_part)

doc=dict()
for i in range(len(text)):
	doc[i] = pf.split_line(text[i])