import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import pickle
import tensorflow as tf

lemmatizer = WordNetLemmatizer()


def preprocess(phrase):
    words = nltk.word_tokenize(phrase)
    words_f = []

    for word in words:
        w = lemmatizer.lemmatize(word.lower())
        words_f.append(w)

    return words_f


def bag_of_words(phrase, words):
    obt_words = preprocess(phrase)

    bag_of_words = [0] * len(words)

    for o in obt_words:
        for w in words:
            # print(o)
            # print(w)
            if o == w:
                # print("A")
                bag_of_words[words.index(w)] = 1

    b_n = np.array(bag_of_words)
    return b_n


def predict_wrapper(phrase):
    model = tf.keras.models.load_model('chatbot_model.h5')
    words = []
    with (open("PickleArchive/words.pkl", "rb")) as openfile:
        while True:
            try:
                words.append(pickle.load(openfile))
            except EOFError:
                break
    tags = []
    with (open("PickleArchive/tags.pkl", "rb")) as openfile:
        while True:
            try:
                tags.append(pickle.load(openfile))
            except EOFError:
                break
    # print(words)
    # print(tags)
    # print(phrase)
    to_pred = bag_of_words(phrase, words[0])
    # print(to_pred)
    pred = model.predict(np.array([to_pred]))[0]
    threshold = 0.25
    results = [[i, r] for i, r in enumerate(pred) if r > threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": tags[0][r[0]], "prob": str(r[1])})
    return return_list
