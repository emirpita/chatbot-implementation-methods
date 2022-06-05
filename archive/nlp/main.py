from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
import re

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()


def swap_pronouns(phrase):
    if 'I' in phrase:
        return re.sub('I', 'you', phrase)
    if 'my' in phrase:
        return re.sub('my', 'your', phrase)
    else:
        return phrase


def filter_command(phrase):
    tokens = []
    tok = word_tokenize(phrase)
    for t in tok:
        tokens.append(t.lower())
    tags = nltk.pos_tag(tokens)

    work = []
    work_f = []
    subject = []
    number = []
    adj = []
    query = []
    name = 0
    for tup in tags:
        if "VB" in tup[1]:
            work.append(tup[0])
        if "CD" in tup[1]:
            number.append(tup[0])
        if "JJ" in tup[1]:
            adj.append(tup[0])
        if "NN" in tup[1]:
            subject.append(tup[0])
        if "W" in tup[1] and "that" not in tup[0]:
            query.append(tup[0])
    for w in work:
        work_f.append(lemmatizer.lemmatize(w.lower()))
    if query:
        if "you" in tokens or "your" in tokens:
            task = 0
        elif 'headlines' not in tokens:
            task = 1
    elif 'book' in work_f or 'book' in tokens[0]:
        task = 2
    else:

        if '?' in tokens and 'you' not in tokens and 'your' not in tokens:
            task = 1
        else:
            task = 0

    return task, work_f, subject, number, adj, query