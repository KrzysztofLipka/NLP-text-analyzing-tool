import os
import pandas as pd

from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import marshal

"""ten modul ma za zadanie stworzenie
listy wektorow slow
ze zbioru danych ingredients v1.csv
"""
os.chdir('C:\\Users\\Dell\\Desktop\\data')

ingr = pd.read_csv('Reviews.csv')



# usuwanie z tekstu znacznikow Html, znakow i
# normalizacja (tylko male litery)

def recipe_to_wordlist(review, remove_stopwords=False):
    review_text = BeautifulSoup(review).get_text()
    review_text = re.sub("[^a-zA-Z]"," ", review_text)
    words = review_text.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    return(words)


# sentences - lista przepsow
# ingr_set - zbior skladnikow
text_corpus = []

for lab,row in ingr.iterrows():
    l = recipe_to_wordlist(str(row["Text"]))
    text_corpus.append(l)




print(len(text_corpus))



#---------------------------------------------------------------


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
    level=logging.INFO)


num_features = 300
min_word_count = 20
num_workers = 4
context = 3
downsampling = 1e-3


from gensim.models import word2vec
print ("Training model...")
model = word2vec.Word2Vec(text_corpus, workers=num_workers, \
            size=num_features, min_count=min_word_count, \
            window=context, sample=downsampling)


model.init_sims(replace=True)

# wczytywanie modelu -  Word2Vec.load()
os.chdir('C:\\Users\\Dell\\Desktop\\data')
model_name = "amazon_model"
model.save(model_name)





