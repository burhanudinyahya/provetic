#!/usr/bin/python

from flask import Flask, Response
from posts import Posts



app = Flask(__name__)



@app.route("/", methods=["GET"])
def home():
    urls = """
        <h3>Daftar Endpoint</h3>
        <ol>
            <li><a href="/topwords">/topwords</a></li>
            <li><a href="/popular/users">/popular/users</a></li>
            <li><a href="/popular/mentions">/popular/mentions</a></li>
            <li><a href="/hourly">/hourly</a></li>
            <li><a href="/bulk_insert">/bulk_insert</a></li>
        </ol>"""

    return urls



@app.route("/topwords", methods=["GET"])
def topwords():
    posts = Posts()
    topwords = posts.topwords()
    return Response(topwords, mimetype='application/json')



@app.route("/popular/users", methods=["GET"])
def popular_users():
    posts = Posts()
    popusers = posts.popular_users()
    return Response(popusers, mimetype='application/json')



@app.route("/popular/mentions", methods=["GET"])
def popular_mentions():
    posts = Posts()
    popmens = posts.popular_mentions()
    return Response(popmens, mimetype='application/json')



@app.route("/hourly", methods=["GET"])
def hourly():
    posts = Posts()
    hours = posts.hourly()
    return Response(hours, mimetype='application/json')



@app.route("/bulk_insert", methods=["GET"])
def bulk_insert():
    posts = Posts()
    bulk = posts.bulk_insert()
    return  Response(bulk, mimetype='application/json')



if __name__ == "__main__":
    app.run()