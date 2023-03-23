import json
import pickle
import numpy as np
import random
import nltk
from nltk.stem import WordNetLemmatizer
import random

lemmatizer=WordNetLemmatizer()

data=json.load(open('archive/Intent.json'))
features=pickle.load(open('features.pkl','rb'))
model=pickle.load(open('chatbot_model.pkl','rb'))
result_map=pickle.load(open('result_map.pkl','rb'))


def create_input(sentence):
    words=nltk.word_tokenize(sentence)
    input_=[ ]
    for i in range(len(features)):
        if features[i] in words:
            input_.append(1)
        else:
            input_.append(0)
        
    return np.array(input_)


def predict(sent):
    input_list=create_input(sent)
    input_list=np.array([input_list])
   
    label=model.predict(input_list)
    maxprob=np.argmax(label[0])
    intent=result_map[maxprob]
    for i in data['intents']:
        if i['intent']==intent:
            return random.choice(i['responses'])
    


    