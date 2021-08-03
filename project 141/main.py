from os import read
from flask import Flask, jsonify, request
import csv
import pandas as pd
all_articles = []

f = pd.read_csv('C:\\Users\\Dhairya\\Desktop\\python\\c 141\\project 141\\shared_articles.csv')
reader = csv.reader(f)
data = list(reader)
all_articles = data[1:]

liked_articles = []
not_liked_articles = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-read", methods=["POST"])
def did_not_read():
    article = all_articles[0]
    all_articles = all_articles[1:]
    did_not_watch.append(article)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()