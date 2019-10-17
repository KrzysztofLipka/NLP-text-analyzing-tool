import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
os.chdir('C:\\Users\\Dell\\Desktop\\data')
# load files
films_data = pd.read_csv("IMDB-Movie-Data.csv")
foods_data = pd.read_csv("Reviews.csv")
print(len(films_data))
print(len(foods_data))
# load
foods = foods_data['Text'][:1000]
foods_type = ['food' for i in foods]
foods_df = list(zip(foods,foods_type))
df = pd.DataFrame(foods_df, columns=['text','type'])

films = films_data['Description']
films_type = ['film' for i in films]
films_df = list(zip(films,films_type))
df2 = pd.DataFrame(films_df, columns=['text','type'])

data = pd.concat([df,df2])
mixed_data = data.sample(frac=1)
y = mixed_data.type
x_train, x_test, y_train,y_test = train_test_split(mixed_data['text'], y,
                                                   test_size=0.35,
                                                   random_state=51)

count_vec = CountVectorizer(stop_words='english')
count_train = count_vec.fit_transform(x_train)
count_test = count_vec.transform(x_test)


naive_bayes_classifier = MultinomialNB()

naive_bayes_classifier.fit(count_train, y_train)
pred = naive_bayes_classifier.predict(count_test)
score = metrics.accuracy_score(y_test, pred)
print('score: ' + str(score))

cm = metrics.confusion_matrix(y_test, pred, labels=['food', 'film'])
print(cm)




txt = ['Preheat oven to 425 degrees F. Whisk pumpkin, sweetened condensed milk,'
                     ' eggs, spices and salt in medium bowl until smooth.'
                     ' Pour into crust. Bake 15 minutes. Reduce oven temperature to 350 degrees'
                     ' F and continue baking 35 to 40 minutes or until knife inserted 1 inch from crust comes out clean. '
                     'Cool. Garnish as desired. Store leftovers covered in refrigerator.']
txt2 = ['In a city of humanoid animals, a hustling theater impresario attempt to save his theater with a'
        ' singing competition becomes grander than he anticipates even'
        ' as its finalists find that their lives will never be the same.']
txt3 = ['My cats have been happily eating Felidae Platinum for more than two years. I just got a new bag and the shape of the food is different. They tried the new food when I first put it in their bowls and now the bowls sit full and the kitties will not touch the food.'
        ' I ve noticed similar reviews related to formula changes in the past. '
        'Unfortunately, I now need to find a new food that my cats will eat.']

pkl_name = "food_plot_classificator.pkl"
with open(pkl_name,'wb') as file:
    pickle.dump(naive_bayes_classifier, file)

vectorizer = "count_vectorizer.pkl"
with open(vectorizer,'wb') as file:
    pickle.dump(count_vec, file)


with open(pkl_name,'rb') as file:
    klasyfikator = pickle.load(file)

with open(vectorizer,'rb') as file:
    count_vectorizer = pickle.load(file)



text = pd.Series(txt2)
print(type(text))
text_test = count_vec.transform(text)
print(text_test)
print(klasyfikator.predict(text_test))


def classify(text):

    text_test = count_vectorizer.transform(text)
    return klasyfikator.predict(text_test)

print(classify(txt2))

#list_of_dicts = [lists2dict(sublist) for sublist in list_of_dicts]