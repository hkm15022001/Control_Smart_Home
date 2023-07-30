import json
import random
from nltk_utils import bag_of_words, token
import pickle
from training_LogisticRegression import file_name, all_words, tags
import numpy as np

with open('data.json  ', 'rb') as json_data:
    contents = json.load(json_data)
with open(file_name, 'rb') as file:
    loaded_model = pickle.load(file)


def predict_LR(sentence):
    sentence = token(sentence)
    X = bag_of_words(sentence, all_words)
    X = np.asarray(X)
    X = np.reshape(X, (1, X.shape[0]))
    output = loaded_model.predict_proba(X)
    predict = np.argmax(output, axis=1)
    tag = tags[predict.item()]
    return tag
