import pickle
from imdb import IMDb
import bs4
import requests
import re
from flask import Flask, flash, jsonify, redirect, render_template, request, session

from googletrans import Translator

translator = Translator()
# myinput = str(input())
# print(myinput)
translation = translator.translate(input(), dest='hi')
print(translator.translate(str(translation.text), dest='en').text)
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
ia = IMDb()
# from sklearn.externals import joblib
# joblib.dump(clf1, "../output" )
# filename = 'finalized_model.sav'
# joblib.dump(clf1, open(filename, 'wb'))
# from sklearn.feature_extraction.text import CountVectorizer
# cv = CountVectorizer(max_features=1000)
model1 = pickle.load(open("gbmodel.sav", 'rb'))
# result1 = model1.predict(my_test)
model2 = pickle.load(open("mbmodel.sav", 'rb'))
# result2 = model2.predict(my_test)
model3 = pickle.load(open("bbmodel.sav", 'rb'))
# result3 = model3.predict(my_test)
mycv = pickle.load(open("allfeatures.sav", 'rb'))

# mv_sentiment = mycv.transform(text).toarray()
# result4 = model1.predict(mv_sentiment)
# result5 = model2.predict(mv_sentiment)
# result6 = model3.predict(mv_sentiment)
