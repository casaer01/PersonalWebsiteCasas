from flask import Flask
import os
import requests
import sqlite3
import records
from flask import (Flask, escape, make_response, redirect, render_template,
                   request, session, url_for)

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    if request.method == "GET":
        return render_template("Intro.html")
   # return render_template("base.html")

if __name__ == '__main__':
   app.run(debug=True)