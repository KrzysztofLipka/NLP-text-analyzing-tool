from flask import Flask, render_template, jsonify, request
#import app.word_click_models as word_click_models

import os
import sys
app = Flask(__name__)

from Django_website.word_click_models import click_event_processing, word_to_synonims, text_to_speech_part,search_in_model
from Django_website.text_update_models import from_draftjs_to_text, classify_text_type, search_ner,text_to_text_count,text_to_ingridients

@app.route('/updateEditorState')
def char_searching():
    input_text = request.args.get('editor_state', 0)
    text = from_draftjs_to_text(input_text)
    classify_text_type(text)
    most_common = text_to_text_count(text)
    type_of_text  = classify_text_type(text)
    if type_of_text == 'film':
        elements = search_ner(text)
    elif type_of_text == 'food':
        elements = text_to_ingridients(text)
        print(elements)
    else:
        elements = ['.']
    print(most_common)
    print(elements)
    return jsonify(most_common=most_common, elements=elements,
                   type_of_text=type_of_text[0])


@app.route('/click_event=')
def click_event():
    kursor_id = request.args.get('ID', 1, type=str)
    text = request.args.get('content', 1, type=str)
    res = click_event_processing(kursor_id, text)
    clicked_word = res[0]
    clicked_sent = res[1]

    synonims = word_to_synonims(clicked_word)
    synonims = synonims[:9]
    familiar = search_in_model(clicked_word,"amazon_model")

    # similar_to_word = search_in_model(word)
    speech_parts = text_to_speech_part(clicked_sent)

    return jsonify(synonims=synonims, speech_parts=speech_parts,
                   familiar=familiar)



@app.route("/")
def index():
    path = os.path.dirname(sys.argv[0])
    print(path)
    return render_template("index.html")


if __name__ == "__main__":
    app.run()