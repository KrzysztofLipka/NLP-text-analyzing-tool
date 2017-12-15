from nltk import sent_tokenize
import nltk
from nltk.tree import Tree
import re
import os
import xlrd
import csv
import pandas as pd
from nltk import tree2conlltags
import pickle

os.chdir('C:\\Users\\Dell\\Desktop\\data')

x1 = pd.ExcelFile('lista_skladnikow.xlsx')
print(x1.sheet_names)
df1 = x1.parse('Arkusz1')
df2 = df1['food']
food_list = []
for i in df2:
    if 'Related' in i:
        i2= i.split('Related')
        #print (i2)
        food_list.append(i2[0].lower())
    else:
        food_list.append(i.lower())

data = pd.DataFrame(food_list,columns=['food'])

pkl_name = "ingridient_list.pkl"
with open(pkl_name,'wb') as file:
    pickle.dump(food_list, file)


with open(pkl_name,'rb') as file:
    food_list = pickle.load(file)



txt = 'Preheat oven to 400 degrees F (205 degrees C). In a large bowl, beat eggs until foamy, and stir in melted butter.' \
      ' Stir in the brown sugar, white sugar and the flour; mix well. Last add the milk, vanilla and nuts. Pour into an unbaked 9-in' \
      ' pie shell. Bake in preheated oven for 10 minutes at 400 degrees, then reduce temperature' \
      ' to 350 degrees and bake for 30 to 40 minutes, or until done. Take two cups of sugar.'

txt2 = 'Take two cups of milk'
txt1 = '1 cup chopped pecans'
txt3 = '1/4 teaspoon vanilla extract'
def chunking(sample_text):
    try:
        #print(train_text)
        for i in sent_tokenize(sample_text):
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #<RB adverb (very, silently).any char except new line? (aby bylo RBR RBS)>*
            #(match 0 or more repetitions)<VERBS>*<NNP> -zreczownik osobowy+
            chunkGram = r"""Chunk: {<CD>*<NN.?><IN><NN.>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            #chunked.draw()
            print (chunked)

    except Exception as e:
        print(str(e))



def ingr_chunking(sample_text):
    try:
        #print(train_text)
        out = []
        #sample_text = re.sub("[^a-zA-Z0-9/]", " ", sample_text)
        for i in sent_tokenize(sample_text):
            i = re.sub("[^a-zA-Z0-9/]", " ", i)
            print(i)

            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #<RB adverb (very, silently).any char except new line? (aby bylo RBR RBS)>*
            #(match 0 or more repetitions)<VERBS>*<NNP> -zreczownik osobowy+
            chunkGram = r"""
            Chunk: {<CD>*<NN.?>*<IN><NN.? >?}
                   {<CD>*<NN.?>*<VBD><NN.>?}
                   {<JJ>*<CD>*<NN>+<NN>?}
            """
            chunkGram2 = r"""
            Chunk1: {<JJ><NN.?>}
            Chunk2:{<CD><NN.?>}
            Chunk3:{<CD><IN><NN.?>}
            Chunk4:{<NN.?>}
            """
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            #chunked.draw()

            #print (chunked)
            #print(type(chunked))
            for tr in chunked:
                tr1 = str(tr)
                s1 = Tree.fromstring(tr1)
                #s2 = s1.productions()
                out.append(s1)
                print(s1)

            #print(tree2conlltags(chunked))
            #print([c for c in chunked])

    except Exception as e:
        print(str(e))

def ingr_chunking2(sample_text):
    try:
        ingridients = []
        for i in sent_tokenize(sample_text):
            i = re.sub("[^a-zA-Z0-9/]", " ", i)
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #<RB adverb (very, silently).any char except new line? (aby bylo RBR RBS)>*
            #(match 0 or more repetitions)<VERBS>*<NNP> -zreczownik osobowy+
            pattern = r"""
            Adjective:{<JJ><NN.?>}
            Number:{<CD><NN.?>}
            Noun:{<NN.?>}
            """
            chunkParser = nltk.RegexpParser(pattern)
            chunked = chunkParser.parse(tagged)
            #print(chunked)
            for i in chunked.subtrees():
                print(i)
                ingr = i[1][0] # name of ingridient
                desc = i[0][0] # count of adjective
                if i.label() =="Adjective" or i.label()=="Number":
                    print (i[1][0][:-1] in food_list)
                    if i[1][0] in food_list or i[1][0][:-1] in food_list:
                        el = i[0][0]+' '+i[1][0]
                        #el = [j[0] for j in i]
                        #print(i[0][0]+' '+i[1][0])

                        print(el)
                        ingridients.append(el)

                if i.label() == "Noun":
                    if i[0][0] in food_list or i[0][0][:-1] in food_list:
                        ingridients.append(i[0][0])
        return ingridients


    except Exception as e:
        print(str(e))
        return['']


print(ingr_chunking2('take two eggs'))
#print(ingr_chunking(txt2))
#print('F' in food_list)

example = 'A large white truck appeared around the corner.' \
          ' I just got a new bag and the shape of the food is different.'

from nltk import sent_tokenize, word_tokenize,pos_tag
sent_segmentation = sent_tokenize(example)
print(sent_segmentation)
tokenized_sentences = [word_tokenize(sent) for sent in sent_segmentation]
print(tokenized_sentences)
pos_tagged = (pos_tag(tokenized_sentences[0]))
print(pos_tagged)
pattern = r"""
            Adjectives:{<DT>?<JJ>*<NN.?>?}
            """
chunkParser = nltk.RegexpParser(pattern)
chunked = chunkParser.parse(pos_tagged)
print(chunked)
#chunked.draw()

for i in chunked.subtrees():
    print(i)


from nltk.corpus import wordnet
print(wordnet.synsets('car'))
print(wordnet.synset('car.n.02').lemmas())

print(wordnet.synset('car.n.02').definition())
print(wordnet.synset('car.n.02').examples())