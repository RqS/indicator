# coding: utf-8
import json
import string
import codecs



#text_part is what you want to extract from text, like: content_strict, content_relaxed or title
def process_text(input_file, text_part):
    with codecs.open(input_file, 'r', 'utf-8') as f:
        content_strict = []
        content_relaxed = []
        title = []

        for index, line in enumerate(f):
            doc = json.loads(line)
            content = doc['content_extraction']
            content_strict.append(content['content_strict']['text'])
            content_relaxed.append(content['content_relaxed']['text'])
            title.append(content['title']['text'])
        if text_part == 'content_strict':
            return content_strict
        elif text_part == 'content_relaxed':
            return content_relaxed
        elif text_part == 'title':
            return title
        else:
            return "No match"

