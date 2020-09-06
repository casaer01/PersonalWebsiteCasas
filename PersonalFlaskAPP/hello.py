from flask import Flask
import os
import requests
import sqlite3
import records
from flask import (Flask, escape, make_response, redirect, render_template,
                   request, session, url_for, send_file)

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    # if request.method == "GET":
    return render_template("frontpage.html")

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/contact")
def contactme():
    return render_template("contactme.html")
    
@app.route('/downloads')
def download_file():
	#path = "html2pdf.pdf"
	#path = "info.xlsx"
	path = "templates/ErosCasas_Resume.pdf"
	#path = "sample.txt"
	return send_file(path, as_attachment=True)

if __name__ == '__main__':
   app.run(debug=True)