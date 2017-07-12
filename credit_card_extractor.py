from spacy.matcher import Matcher
from spacy.attrs import LOWER, IS_ASCII, IS_DIGIT, DEP, FLAG40, FLAG41, ORTH

def add_to_vocab(nlp, lst):
    for lexeme in lst:
        nlp.vocab[lexeme.lower().decode('utf8')]

def set_flag(nlp, token_l, flag):
    # for t in token_l:
        # elst = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in t)))
    for lexeme in token_l:
        nlp.vocab[lexeme.decode('utf8')].set_flag(flag, True)

def load_credit_card_matcher(nlp):
    matcher = Matcher(nlp.vocab)

    payment =  [
        'visa',
        'mastercard',
        'masterc',
        'mc',
        'mcard',
        'cash',
        'csh',
        'discover',
        'amex',
        'interac',
        'jcb'
    ]

    visa_type =  [
        'us',
        'american',
        'canadian',
        'student',
        'online',
        'transit',
        'need',
        'make',
        'f1',
        'temp',
        'temporary',
        'permanent',
        'visitor',
        'visit',
        'visiting'
    ]

    is_payment = FLAG40
    is_visa_type = FLAG41
    set_flag(nlp, payment, is_payment)
    set_flag(nlp, visa_type, is_visa_type)

    matcher.add_entity(1)
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: "/"}, {is_payment: True}])
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: ","}, {is_payment: True}])
    matcher.add_pattern(1, [{is_payment: True}, {LOWER: "and"}, {is_payment: True}])
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: "/"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: ","}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{is_payment: True}, {ORTH: "&"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{is_payment: True}, {LOWER: "and"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}, {ORTH: "/"}, {LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}])
    matcher.add_pattern(1, [{LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}, {ORTH: ","}, {LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}])
    matcher.add_pattern(1, [{LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}, {LOWER: "and"}, {LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}])
    matcher.add_pattern(1, [{LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}, {ORTH: "/"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}, {ORTH: ","}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}, {ORTH: "&"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}, {LOWER: "and"}, {LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LOWER: "american"}, {LOWER: "express"}])
    matcher.add_pattern(1, [{LOWER: "diners"}, {LOWER: "club"}, {LOWER: "internacional"}])
    matcher.add_pattern(1, [{LOWER: "union"}, {LOWER: "pay"}])
    matcher.add_pattern(1, [{LOWER: "credit"}, {LOWER: "card"}])
    matcher.add_pattern(1, [{LOWER: "creditcard"}])

    matcher.add_entity(2)
    matcher.add_pattern(2, [{LOWER: "accept"}, {LOWER: "card"}])
    matcher.add_pattern(2, [{LOWER: "accept"}, {is_payment: True}])
    matcher.add_pattern(2, [{LOWER: "accept"}, {LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}])
    matcher.add_pattern(2, [{LOWER: "accept"}, {ORTH: ":"}, {is_payment: True}])
    matcher.add_pattern(2, [{LOWER: "payment"}, {ORTH: ":"}, {is_payment: True}])
    matcher.add_pattern(2, [{LOWER: "accept"}, {ORTH: ":"}, {LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}])
    matcher.add_pattern(2, [{LOWER: "payment"}, {ORTH: ":"}, {LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}])    

    matcher.add_entity(3)
    matcher.add_pattern(3, [{LOWER: "at"}, {is_payment: True}])
    matcher.add_pattern(3, [{LOWER: "at"}, {LOWER: "m"}, {ORTH: "/"}, {LOWER: "card"}])
    matcher.add_pattern(3, [{LOWER: "visa"}, {LOWER: "versa"}])  
    
    matcher.add_entity(4)
    matcher.add_pattern(4, [{DEP: "neg"}, {LOWER: "credit"}, {LOWER: "card"}])
    matcher.add_pattern(4, [{LOWER: "credit"}, {LOWER: "card"}, {DEP: "neg"}])
    matcher.add_pattern(4, [{DEP: "neg"}, {LOWER: "creditcard"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LOWER: "credit"}, {LOWER: "card"}])
    matcher.add_pattern(4, [{LOWER: "no"}, {LOWER: "creditcard"}])
    matcher.add_pattern(4, [{LOWER: "not"}, {IS_ASCII: True}, {LOWER: "credit"}, {LOWER: "card"}])
    matcher.add_pattern(4, [{LOWER: "not"}, {IS_ASCII: True}, {LOWER: "creditcard"}])
    matcher.add_pattern(4, [{is_visa_type: True}, {LOWER: "visa"}])
    matcher.add_pattern(4, [{LOWER: "visa"}, {LOWER: "student"}])
    matcher.add_pattern(4, [{LOWER: "rent"}, {LOWER: "and"}, {LOWER: "visa"}])
    matcher.add_pattern(4, [{LOWER: "rent"}, {LOWER: "and"}, {LOWER: "credit"}])
    matcher.add_pattern(4, [{LOWER: "visa"}, {LOWER: "and"}, {LOWER: "rent"}])
    matcher.add_pattern(4, [{LOWER: "card"}, {LOWER: "and"}, {LOWER: "rent"}])
    matcher.add_pattern(4, [{LOWER: "apply", DEP: "ROOT"}, {LOWER: "for", DEP: "prep"}, {LOWER: "visa"}])
    matcher.add_pattern(4, [{LOWER: "apply", DEP: "ROOT"}, {LOWER: "visa"}])
    matcher.add_pattern(4, [{LOWER: "arrival", DEP: "ROOT"}, {LOWER: "visa"}])

    return matcher

def post_process(matches, nlp_doc):
    credit_card = dict()
    label_list = ["positive", "strong positive", "negative", "strong negative"]
    for ent_id, label, start, end in matches:
        if label_list[ent_id-1] not in credit_card:
            credit_card[label_list[ent_id-1]] = []
            credit_card[label_list[ent_id-1]].append(nlp_doc[start:end])
        else:
            credit_card[label_list[ent_id-1]].append(nlp_doc[start:end])
    return credit_card

def extract(nlp_doc, matcher):
    credit_card_matches = matcher(nlp_doc)
    credit_card = post_process(credit_card_matches, nlp_doc)

    return credit_card