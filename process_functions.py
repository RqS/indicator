# coding: utf-8
import json
import string
import codecs
from tokenizer_extractor import TokenizerExtractor

#text_part is what you want to extract from text, like: content_strict, content_relaxed or title
def process_text(input_file, text_part):
    with codecs.open(input_file, 'r', 'utf-8') as f:
        content_result = []
        text_type=['content_strict', 'content_relaxed', 'title']
        if text_part not in text_type:
            return "No match"
        else:
            for index, line in enumerate(f):
                doc = json.loads(line)
                content = doc['content_extraction']
                content_result.append(content[text_part]['text'])
            return content_result

def extract_crftokens(text, options=None, lowercase):
        t = TokenizerExtractor(recognize_linebreaks=True, create_structured_tokens=True)
        return t.extract(text, lowercase)

def extract_tokens_from_crf(crf_tokens):
        return [tk['value'] for tk in crf_tokens]

#given a string, split this string into many line according to new line symbol
def split_line(str):
    line_list = []
    str = str.strip()
    list = str.split('\n')
    return list
