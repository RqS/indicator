from spacy.matcher import Matcher
from spacy.attrs import LOWER, IS_ASCII, DEP, FLAG23, FLAG24, FLAG25

def add_to_vocab(nlp, lst):
    for lexeme in lst:
        nlp.vocab[lexeme.lower().decode('utf8')]

def load_outcall_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    location = ['location', 'place', 'studio', 'apartment', 'home', 'house', 'hotel']

    add_to_vocab(nlp, location)

    location_ids = {nlp.vocab.strings[s.lower()] for s in location}
    hyphen_id = nlp.vocab.strings['-']
    ampersand_id = nlp.vocab.strings['&']

    is_hyphen = FLAG23
    is_ampersand = FLAG24
    is_location = FLAG25
    
    for lexeme in nlp.vocab:
        if lexeme.lower == hyphen_id:
            lexeme.set_flag(is_hyphen, True)
        if lexeme.lower == ampersand_id:
            lexeme.set_flag(is_ampersand, True)
        if lexeme.lower in location_ids:
            lexeme.set_flag(is_location, True)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{LOWER: "outcall"}])
    matcher.add_pattern(1, [{LOWER: "out"}, {LOWER: "call"}])
    matcher.add_pattern(1, [{LOWER: "out"}, {is_hyphen: True}, {LOWER: "call"}])
    matcher.add_pattern(1, [{LOWER: "your"}, {is_location: True}])
    matcher.add_pattern(1, [{LOWER: "out"}, {LOWER: "and"}, {LOWER: "in"}, {LOWER: "call"}])
    matcher.add_pattern(1, [{LOWER: "out"}, {is_ampersand: True}, {LOWER: "in"}, {LOWER: "call"}])
    matcher.add_pattern(1, [{LOWER: "visit"}, {LOWER: "you"}])
    matcher.add_pattern(1, [{LOWER: "mind"}, {LOWER: "travel"}])
    matcher.add_pattern(1, [{LOWER: "anywhere"}, {LOWER: "and"}, {LOWER: "everywhere"}])
    matcher.add_pattern(1, [{LOWER: "prefer"}, {LOWER: "residence"}])
    matcher.add_pattern(1, [{LOWER: "prefer"}, {LOWER: "hotel"}])
    matcher.add_pattern(1, [{LOWER: "come"}, {LOWER: "to"}, {LOWER: "you"}])
    matcher.add_pattern(1, [{LOWER: "will"}, {LOWER: "travel"}])
    
    matcher.add_entity(2)
    matcher.add_pattern(2, [{LOWER: "outcall"}, {LOWER: "only"}])
    matcher.add_pattern(2, [{LOWER: "out"}, {LOWER: "call"}, {LOWER: "only"}])
    matcher.add_pattern(2, [{LOWER: "out"}, {is_hyphen: True}, {LOWER: "call"}, {LOWER: "only"}])
    matcher.add_pattern(2, [{LOWER: "your", DEP: "amod"}, {is_location: True}])
    matcher.add_pattern(2, [{LOWER: "your", DEP: "amod"}, {IS_ASCII: True}, {is_location: True}])
    matcher.add_pattern(2, [{LOWER: "your", DEP: "poss"}, {is_location: True}])
    matcher.add_pattern(2, [{LOWER: "your", DEP: "poss"}, {IS_ASCII: True}, {is_location: True}])

    matcher.add_entity(3)
    matcher.add_pattern(3, [{is_location: True}])
    matcher.add_pattern(3, [{LOWER: "place"}])
    matcher.add_pattern(3, [{LOWER: "be"}, {LOWER: "place"}])
    matcher.add_pattern(3, [{LOWER: "is"}, {LOWER: "place"}])

    matcher.add_entity(4)
    matcher.add_pattern(4, [{LOWER: "house"}, {LOWER: "wives"}])
    matcher.add_pattern(4, [{LOWER: "if", DEP: "mark"}, {LOWER: "have"}, {IS_ASCII: True, DEP: "dobj"}])
    matcher.add_pattern(4, [{LOWER: "if", DEP: "mark"}, {IS_ASCII: True}, {LOWER: "have"}, {IS_ASCII: True}, {IS_ASCII: True, DEP: "dobj"}])
    matcher.add_pattern(4, [{LOWER: "if", DEP: "mark"}, {LOWER: "have"}, {IS_ASCII: True}, {IS_ASCII: True, DEP: "dobj"}])
    matcher.add_pattern(4, [{LOWER: "my", DEP: "poss"}, {is_location: True}])
    matcher.add_pattern(4, [{LOWER: "my", DEP: "poss"}, {IS_ASCII: True}, {is_location: True}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LOWER: "outcall"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LOWER: "out"}, {LOWER: "call"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LOWER: "out"}, {is_hyphen: True}, {LOWER: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LOWER: "outcall"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LOWER: "out"}, {LOWER: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {LOWER: "out"}, {is_hyphen: True}, {LOWER: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {IS_ASCII: True}, {LOWER: "outcall"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {IS_ASCII: True}, {LOWER: "out"}, {LOWER: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "neg"}, {IS_ASCII: True}, {LOWER: "out"}, {is_hyphen: True}, {LOWER: "call"}])
    matcher.add_pattern(4, [{LOWER: "visit"}, {LOWER: "your"}, {LOWER: "city"}])
    matcher.add_pattern(4, [{IS_ASCII: True}, {LOWER: "miss"}, {LOWER: "out"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LOWER: "out"}, {LOWER: "call"}])
    matcher.add_pattern(4, [{IS_ASCII: True, DEP: "dep"}, {LOWER: "no"}])
    
    return matcher

def post_process(matches, nlp_doc):
    outcall = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id-1] not in outcall:
            outcall[label_list[ent_id-1]] = []
            outcall[label_list[ent_id-1]].append(nlp_doc[start:end])
        else:
            outcall[label_list[ent_id-1]].append(nlp_doc[start:end])
    return outcall

def extract(nlp_doc, matcher):
    outcall_matches = matcher(nlp_doc)
    outcall = post_process(outcall_matches, nlp_doc)

    return outcall