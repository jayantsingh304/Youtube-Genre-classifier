import re
import oauth2
from distutils.command.build import build
import time
import urllib2
import json
import os
import sys

import requests
import json, ast
import nltk
import nltk.data
tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
import sys
from textblob import TextBlob
from textblob.compat import PY2
from nltk.tokenize import word_tokenize
from nltk import word_tokenize,sent_tokenize
from textblob.classifiers import NaiveBayesClassifier


def func(xyz):

    url= "https://www.googleapis.com/youtube/v3/commentThreads"
    params=dict()


    api_key='api key from google developer console for youtube comments'
    videoId=xyz#'8Deidy3ONqg'

    params["part"] = "snippet"      #mandatory
    params["maxResults"] = "80"        #optional
    params["textFormat"] = "plainText"  #or html
    params["videoId"] = xyz

    params["key"] = api_key
    url=url+'?'
    i=0
    for key,value in params.iteritems():
        if i==0:
            url=url+key+'='+value
            i=i+1
        else:
            url=url+'&'+key+'='+value
    print (url)


    proxies = {}
#'https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyDR_p3sWUI9R21TaewInZOBpKWrS19EfK4&textFormat=plainText&part=snippet&videoId=kffacxfA7G4&maxResults=50'
    r = requests.get(url, proxies=proxies)
    commit_data = (r.json())
    dot=". "
    stringcocat=""
    commit_item=commit_data[ u'items']
    for i in commit_data[u'items']:
        commit_tag=json.dumps(i)
        jdata = json.loads(commit_tag)
        hello=jdata[ u'snippet']
        comma=hello[u'topLevelComment']
        commentdata =json.dumps(comma)
        moondata = json.loads(commentdata)
        textDisplay=moondata[u'snippet']
        commentdfdata =json.dumps(textDisplay)
        moondafaata = json.loads(commentdfdata)
        string=json.dumps(moondafaata[u'textDisplay'])
        string = string[1:-1]
        #print (string)
        #re.sub("[^a-zA-Z]+", "", string)

        stringcocat=stringcocat+string.replace(".", "")+dot

    withooutslash=stringcocat.replace("\\ud83d", "").replace("\\ude0d", "").replace("\\udc4c", "").replace("\\ufeff", "").replace("\\u00d1i", "").replace("\\u00e7e", "").replace("\\u2661", "").replace("\\udc4e", "").replace("\\udfff", "").replace("\\udc4e", "").replace("\\n", "")
    #print (withooutslash) #final
    #\ud83d,\ude0d,udc4c,\ufeff


    #blob = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)
    #for s in blob.sentences:
    #    print(s)
    #    print(s.classify())
    prob_dist = cl.prob_classify(withooutslash)
    prob_dist.max()
    original_list = [round(prob_dist.prob("politics"), 4),round(prob_dist.prob("song"), 4),round(prob_dist.prob("comedy"), 4)]
    list_dump = json.dumps(original_list)
    def json_list(list_dump):
        lst = []
      #  for pn in list_dump:
    d = {}
    lst = []
    d['politics']=original_list[0]
    d['song']=original_list[1]
    d['comedy']=original_list[2]
    #lst.append(d)
    loo=json.dumps(d)
    print json.dumps(d)
    return json.loads(loo)

from flask import Flask, request, jsonify

app = Flask(__name__)
from flask.ext.restful import Api
from flask.ext.restful import Resource
api=Api(app)
train = [
         ('song', 'song'),
         ('singer , arjit singh ', 'song'),
          ('song', 'song'),
         ('song', 'song'),
          ("beats ", 'song'),
         ("soulful ", 'song'),
         ("singing", 'song'),
         ("vocal", 'song'),
          ("lyrics", 'song'),
          ("lyric", 'song'),
          ("music", 'song'),
          ("music director", 'song'),
          ("chords", 'song'),
          ("guitar", 'song'),

          ("soothing ", 'song'),
         ("nostalgic ", 'song'),
         ("soothing ", 'song'),
         ("melodious ", 'song'),
            ("melody ", 'song'),
            ("flute ", 'song'),   ("soothing ", 'song'),
            ("harmonica ", 'song'),
            ("harmonium ", 'song'),
            ("piano ", 'song'),
         ("band ", 'song'),
      ("concert ", 'song'),
          ("singing", 'song'),
        ("taylor swift", 'song'),
        ("arjit singh", 'song'),


         ('democracy politics', 'politics'),
         ('manmohan singh.', 'politics'),
         ("Parliament", 'politics'),
         ("Caste", 'politics'),
         ("Nehru", 'politics'),
         ("Politician", 'politics'),
         ("politics", 'politics'),

         ("governance", 'politics'),
         ("Mahatma Gandhi", 'politics'),
         ("Jayaprakash Narayan", 'politics'),
        ("speech", 'politics'),
          ("democratic", 'politics'),
          ("Naredra modi", 'politics'),
          ("APJ Abdul kalam", 'politics'),
          ("Pratibha Patil", 'politics'),
          ("Rajendra Prasad", 'politics'),
          ("Chief Justice", 'politics'),
          ("rti , RTI", 'politics'),
          ("sonia gandhi", 'politics'),
          ("rahul gandhi", 'politics'),
          ("PM", 'politics'),
          ("Minister", 'politics'),
         ("lok sabha", 'politics'),
         ("rajya sabha", 'politics'),
         ("rashtriyapati", 'politics'),
          ("Pt. Jawaharlal Nehru", 'politics'),
         ("B. R. Ambedkar", 'politics'),
          ("Atal Behari Vajpayee", 'politics'),
        # Lal Bahadur Shastri,Sardar Vallabhbhai Patel, Subhash Chandra Bose,Indira Gandhi,Dr. Rajendra Prasad,APJ Abdul Kalam,Dadabhai Naoroji,Jyoti Basu,Shashi Tharoor,E M Sankaran Namboodiripad,N.T.Rama Rao,M. G. Ramachandran,Sonia Gandhi,Rajiv Gandhi,Manmohan Singh,Zakir Hussain,P. V. Narasimha Rao,Morarji Desai,Sunil Dutt,Narendra Modi,Jairam Ramesh,Jayaprakash Narayan,Nitish Kumar'
          (" Lal Bahadur Shastri", 'politics'),
          ("Sardar Vallabhbhai Patel", 'politics'),
          ("Subhash Chandra Bose", 'politics'),
          ("namo", 'politics'),
         ("obama", 'politics'),
         ("Dadabhai Naoroji", 'politics'),
         ("criminal", 'politics'),
         ("Shashi Tharoor", 'politics'),
         ("speaker public", 'politics'),
         ("Shashi Tharoor", 'politics'),
         ("gandhi", 'politics'),
         ("President ", 'politics'),
         ("conference ", 'politics'),
         ("AAP", 'politics'),
         ("aam admi ", 'politics'),
         ("congress", 'politics'),
          ("congress", 'politics'),
         #("manmohan", 'politics')
        ('haha ', 'comedy'),
         (' hahahahah', 'comedy'),
         ('ha ', 'comedy'),
         ('hahaa hahahaha', 'comedy'),
         ('hahaa hahahaha', 'comedy'),
         (' lolllll','comedy'),
          ('lol','comedy'),
         (' smile ,humour', 'comedy'),
         (' funny ', 'comedy'),
         ('entertaining', 'comedy'),
          (' Comedy  ', 'comedy'),
          ('  comedy', 'comedy'),
          ('comedy ', 'comedy'),
          (' funny', 'comedy'),
          (' comedian', 'comedy')



        # ('He is my sworn enemy!', 'neg'),
         #('My boss is horrible.', 'neg')
        ]

cl = NaiveBayesClassifier(train)
cl.show_informative_features()
#all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
#print (all_words)
#test_sentence = "This is the best band I've ever heard!"
#test_sent_features = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}
#t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]
#print (test_sent_features)
class hello(Resource):
    def post(self):

        v_id=request.get_data()

        return func(v_id)

api.add_resource(hello,'/',methods=['POST'])



if __name__ == "__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
