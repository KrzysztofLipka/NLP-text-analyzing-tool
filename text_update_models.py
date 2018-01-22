import spacy
import nltk
#nlp = spacy.load('en')
import en_core_web_sm
nlp = en_core_web_sm.load()
import json
from nltk import FreqDist,sent_tokenize, word_tokenize, pos_tag
import pickle
import os
import os.path
import  pandas as pd
import marshal
import re
import sys


from Django_website.settings import APP_STATIC

os.chdir(APP_STATIC)
food_set = "food_set.pkl"
pkl_name = "food_plot_classificator.pkl"
vectorizer = "count_vectorizer.pkl"
ingr_name = "ingridient_list.pkl"
with open(food_set,'rb') as file:
    foods = marshal.load(file)

with open(pkl_name,'rb') as file:
    food_plot_classificator = pickle.load(file)

with open(vectorizer,'rb') as file:
    count_vectorizer = pickle.load(file)

with open(ingr_name,'rb') as file:
    food_list = pickle.load(file)


def from_draftjs_to_text(state):
    editor_state = json.loads(state)
    list_of_lines = []
    text = ''
    editor_text = editor_state['blocks']  # all text in editor
    # petla przetwarzajaca wyslany stan edytora
    # na liste akapitow
    for line in range(len(editor_text)):
        list_of_lines.append([editor_text[line]['text']])
        text += ' ' + editor_text[line]['text']
    return text


def classify_text_type(text):
    text = pd.Series(text)
    text_test = count_vectorizer.transform(text)
    text_type = food_plot_classificator.predict(text_test)
    return text_type


def most_common_words(text, number, stopwords):
    if stopwords is True:
        stop_words = set(stopwords.words("english"))
        res = [w for w in text if w not in stop_words]
    elif stopwords is False:
        res = [w for w in text]
    f = FreqDist(res)
    return f.most_common(number)


def text_to_text_count(text):
    text = re.sub("[^a-zA-Z0-9]", " ", text)
    text = word_tokenize(text)
    word_count = most_common_words(text, number=10,
                                   stopwords=False)
    tab = []
    for i in range(len(word_count)):
        tab.append((word_count[i][0],word_count[i][1]))
    return tab


def search_ner(text):
    c = nlp(text)
    person_list = [(i.orth_, i.label_) for i in c.ents if i.label_ == "PERSON"]
    org_list = [(i.orth_, i.label_) for i in c.ents if i.label_ == "ORG"]
    dates_list = [(i.orth_, i.label_) for i in c.ents if i.label_ == "DATE"]
    return person_list + org_list + dates_list


def text_to_ingridients(sample_text):
    try:
        ingridients = []
        for i in sent_tokenize(sample_text):
            i = re.sub("[^a-zA-Z0-9/]", " ", i)
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            pattern = r"""
            Adjective:{<JJ><NN.?>}
            Number:{<CD><NN.?>}
            Noun:{<NN.?>}
            """

            chunkParser = nltk.RegexpParser(pattern)
            chunked = chunkParser.parse(tagged)
            for i in chunked.subtrees():
                if i.label() =="Adjective" or i.label()=="Number":
                    if i[1][0] in food_list or i[1][0][:-1] in food_list:
                        ingridients.append((i[1][0], i[0][0]))

                if i.label() == "Noun":
                    if i[0][0] in food_list or i[0][0][:-1] in food_list:
                        ingridients.append((i[0][0],' ' ))
        return ingridients

    except Exception as e:
        print(str(e))
        return['']


