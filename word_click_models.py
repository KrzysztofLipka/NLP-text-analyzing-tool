
import os, os.path

from gensim.models import Word2Vec
from nltk.corpus import wordnet
import spacy

from nltk import sent_tokenize, word_tokenize, pos_tag
import re

from app.settings import APP_STATIC


nlp = spacy.load('en')


'''
Click models for word.
'''

def click_event_processing(cursor_position, text):
    cursor_position = int(cursor_position)
    text = str(text)
    l = text.split()
    if cursor_position >= len(text):
        return['','']
    elif len(text) == 0:  # return empty word an sentence
        return['empty', 'empty']
    else:
        word_counter = 0
        len_to_cursor = 0 # len from line start to click
        while len_to_cursor <= cursor_position:
            len_to_cursor += len(l[word_counter])+1
            word_counter += 1
        sentences = sent_tokenize(text)  # slice text to sentences
        words_in_sentences_list = [word.split() for word in sentences]

        len_counter = 0  # len of sum of words increment in loop
        sent_counter = 0  # adding sents while sent>word

        # Looping while len_counter <= clicked word.
        while len_counter <= word_counter-1:
            len_counter += len(words_in_sentences_list[sent_counter])
            sent_counter+=1
        # Return clicked word and sentence.
        return [l[word_counter-1], sentences[sent_counter-1]]


def word_to_synonims(word):
    synonims_list = []
    if word:
        if word[-1] == '.' or word[-1] == ',':
            word = word[:-1]
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonims_list.append(l.name())
    synonims_list = list(set(synonims_list))

    return synonims_list


def text_to_speech_part(sent):
    sent = re.sub("[^a-zA-Z0-9]", " ", sent)
    tagged_list = []
    words = word_tokenize(sent)
    tagged = pos_tag(words)
    for word in tagged:
        tagged_list.append([word[0], speech_parts[word[1]]])

    return tagged_list

# wyszukiwanie podobnych slow


def search_in_model(word,model):
    try:
        if word[-1] == '.' or word[-1] == ',':
            word = word[:-1]
        #os.chdir(path + '/ml_models/')
        os.chdir(APP_STATIC)
        model = Word2Vec.load(model)
        return [i[0] for i in model.most_similar(word.lower())]
    except Exception:
        return ['.']

speech_parts = {
'CC':	'coordinating conjunction',
'CD':	'cardinal digit',
'DT':	'determiner',
'EX':	'existential there (like: "there is" ... think of it like "there exists")',
'FW':	'foreign word',
'IN':	'preposition/subordinating conjunction',
'JJ':	'adjective	(big)',
'JJR':	'adjective, comparative (bigger)',
'JJS':	'adjective, superlative (biggest)',
'LS':	'list marker	1)',
'MD':	'modal	could, will',
'NN':	'noun, singular (desk)',
'NNS':	'noun plural (desks)',
'NNP':	'proper noun, singular (Harrison)',
'NNPS':	'proper noun, plural (Americans)',
'PDT':	'predeterminer	(all the kids)',
'POS':	'possessive ending	parents',
'PRP':	'personal pronoun	I, he, she',
'PRP$':	'possessive pronoun my, his, hers',
'RB':	'adverb	very, silently,',
'RBR':	'adverb, comparative better',
'RBS':	'adverb, superlative best',
'RP':	'particle	give up',
'TO':	'to go (to) the store.',
'UH':	'interjection	errrrrrrrm',
'VB':	'verb, base form	take',
'VBD':	'verb, past tense	took',
'VBG':	'verb, gerund/present participle taking',
'VBN':	'verb, past participle	taken',
'VBP':	'verb, sing. present, non-3d	take',
'VBZ':	'verb, 3rd person sing. present takes',
'WDT':	'wh-determiner	which',
'WP':	'wh-pronoun	who, what',
'WP$':	'possessive wh-pronoun	whose',
'.':	'.',
',':	',',
'!':	'!',
' ':	' ',
'':	'',
':':	'!',

'WRB':	'wh-abverb	where, when',

}

