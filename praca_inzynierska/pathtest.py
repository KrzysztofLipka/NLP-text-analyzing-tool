import os
import sys

path = os.path.dirname(sys.argv[0])
print(path)
dir = os.path.dirname(__file__)
filename = os.path.join(dir,path + '/ml_models/cookbook_vector')
from word_click_models import search_in_model
clicked_word = "egg"
familiar = search_in_model(clicked_word,filename)
print(familiar)