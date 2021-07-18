from flask import Flask, jsonify

# import requests
import csv

app = Flask(__name__)

all_articles = []
with open("articles.csv") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_articles = data[1:]
liked_articles = []
not_liked_articles = []


@app.route("/get_article")
def get_article():
    return jsonify({"data": all_articles[0], "status": "success"})


@app.route("/like_article", methods=["POST"])
def like_article():
    liked_articles.append(all_articles[0])
    all_articles.pop(0)
    return jsonify({"data": liked_articles, "status": "success"})


@app.route("/not_like_article", methods=["POST"])
def not_like_article():
    not_liked_articles.append(all_articles[0])
    all_articles.pop(0)
    return jsonify({"data": not_liked_articles, "status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
