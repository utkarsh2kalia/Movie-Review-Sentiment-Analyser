import pickle
from imdb import IMDb
import bs4
import requests
import re
from flask import Flask, flash, jsonify, redirect, render_template, request, session
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
# test2 = mycv.transform(text).toarray()
# result4 = model1.predict(test2)
# result5 = model2.predict(test2)
# result6 = model3.predict(test2)


@app.route("/")
def index():
    return render_template("search_movie.html")


@app.route("/movies", methods=["GET", "POST"])
def movies():
    movie_name = request.form.get("movie_name")
    print(movie_name)
    search_results = ia.search_movie(movie_name)
    listt = {}
    for i in range(0, len(search_results)):
        year = ""
        if 'year' in search_results[i].keys():
            year = search_results[i]['year']

        listt[i] = [search_results[i]['title'],
                    search_results[i].movieID, year]

    # movie = ia.search_movie('Titanic')[0].movieID
    print(listt)
    return render_template("search_results.html", listt=listt)


@app.route("/sentiment", methods=["GET"])
def sentiment():

    # movie_name = request.form.get("movie_name")
    # # display the names
    # # get the id of the movie searched
    # movie = ia.search_movie(movie_name)[0].movieID
    movie = str(request.args.get('movieID'))
    movie_name = str(request.args.get('movie_name'))
    print(movie)
    # get all the info of the movie
    movie_info = ia.get_movie(movie, info=['reviews'])
    review_length = len(movie_info['reviews'])
    mylist = {}
    for i in range(0, review_length):
        review_data = movie_info['reviews'][i]
        text = [review_data['content'].replace("\'", "")]
        # print(text)
        # rating = review_data['rating']
        mv_sentiment = mycv.transform(text).toarray()
        result4 = model1.predict(mv_sentiment)
        result5 = model2.predict(mv_sentiment)
        result6 = model3.predict(mv_sentiment)

        mylist["review"+str(i+1)] = {"sentiment": ["Negative" if result4[0]
                                                   == 0 else "Positive", "Negative" if result5[0]
                                                   == 0 else "Positive", "Negative" if result6[0]
                                                   == 0 else "Positive"], "content": text, "movie_name": movie_name}
    # print(movie_info['reviews'][0])
    # print(mylist)
    return render_template("sentiment.html", mylist=mylist)
    # return mylist


# ia = IMDb()
# # get the id from movie name
print(ia.get_movie_infoset())
# movie = ia.search_movie('Titanic')[0]['year']
# print(movie)


# # movie = ia.get_movie('0133093', info=['reviews'])
# # get movie details
# mymovie = ia.get_movie(movie, info=['reviews'])
# # store teh first review
# print(mymovie['year'])
# text = [mymovie['reviews'][4]['content']]
# # open the saved countvectorizer
# filename1 = "features.sav"
# mycv = pickle.load(open(filename1, 'rb'))
# text = [
#     "You can watch this movie in 1997, you can watch it again in 2004 or 2009 or you can watch it in 2015 or 2020, and this movie will get you EVERY TIME. Titanic has made itself FOREVER a timeless classic! I just saw it today (2015) and I was crying my eyeballs out JUST like the first time I saw it back in 1998. This is a movie that is SO touching, SO precise in the making of the boat, the acting and the storyline is BRILLIANT! And the preciseness of the ship makes it even more outstanding! Kate Winslet and Leonardo Dicaprio definitely created a timeless classic that can be watched time and time again and will never get old. This movie will always continue to be a beautiful, painful & tragic movie. 10/10 stars for this masterpiece!"]
# my_test = mycv.transform(text).toarray()


# model1 = pickle.load(open("gbmodel.sav", 'rb'))
# result1 = model1.predict(my_test)
# model2 = pickle.load(open("mbmodel.sav", 'rb'))
# result2 = model2.predict(my_test)
# model3 = pickle.load(open("bbmodel.sav", 'rb'))
# result3 = model3.predict(my_test)
# mycv = pickle.load(open("allfeatures.sav", 'rb'))
# test2 = mycv.transform(text).toarray()
# result4 = model1.predict(test2)
# result5 = model2.predict(test2)
# result6 = model3.predict(test2)

# print(result1, result2, result3, result4, result5, result6)
# # print(test2)

# # filename = 'finalized_model1.sav'

# # loaded_model = pickle.load(open(filename, 'rb'))
# # result = loaded_model.predict(test2)
# # print(result)
# # loaded_model = joblib.load(open(filename, 'rb'))
# # result = loaded_model.predict(my_test)
# # print(result)

# # print(ia.get_movie_infoset())
# # url = "https://www.imdb.com/title/tt0088727/reviews?ref_=tt_urv"

# # movie = ia.get_movie('0133093', info=['reviews'])
# # print(movie.get('critic reviews'))
# # movie = ia.get_movie('0094226', info=['reviews'])
# # print(movie.current_info)
# # plot = movie['reviews'][0]["content"]
# # print(plot)
# # for genre in the_matrix['review']:
# #     print(genre)


# # r = requests.get(url, allow_redirects=True)
# # open('imdb.html', 'wb').write(r.content)
# # soup = bs4.BeautifulSoup(r.content, 'html.parser')
# # content = soup.find_all("div", class_="text show-more__control")
# # reviews = []


# # def cleanhtml(raw_html):
# #     cleanr = re.compile('<.*?>')
# #     cleantext = re.sub(cleanr, '', raw_html)
# #     return cleantext


# # for elm in content:
# #     reviews.append(cleanhtml(str(elm)))
# # print(reviews[0])
