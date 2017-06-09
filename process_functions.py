# coding: utf-8
import json
import string
import codecs
from tokenizer_extractor import TokenizerExtractor

_LEAST_LEN = 3
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

def extract_crftokens(text, options=None, lowercase=False):
        t = TokenizerExtractor(recognize_linebreaks=True, create_structured_tokens=True)
        return t.extract(text, lowercase)

def extract_tokens_from_crf(crf_tokens):
        return [tk['value'] for tk in crf_tokens]

#given a string, split this string into many line according to new line symbol
def split_line(s):
    if len(s) >= 10:
        str_result = s.strip().translate(string.maketrans("", ""), string.punctuation)
        lst = [x.strip() for x in str_result.split('\n') if x != ' ']
    return lst

def prep_nlp(nlp):
    old_tokenizer = nlp.tokenizer
    nlp.tokenizer = lambda tokens: old_tokenizer.tokens_from_list(tokens)
    return nlp

#def process_extracted()

