import os
import requests
import sqlite3
import records
from flask import (Flask, escape, make_response, redirect, render_template,
                   request, session, url_for)

app = Flask(__name__)

app.secret_key = b'sT\xee\x96\x17X\xbb\xdc\x00\x0c\xf5\xa0\xe7\xd4\xb5\xdd'

# cur.execute("INSERT INTO weaponsData VALUES()")
# for using sqlite3 in console use '.mode column' and then use '.headers on'

def get_data_from_db(query: str) -> list:
    conn = sqlite3.connect("WeaponsINFO.db")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("homepage.html")

    if request.form.get("primary"):
        primary = request.form.get('primary')
        query = f"select * from weaponsData where Name='{primary}';"
        result = get_data_from_db(query)
        return render_template("result.html", rows=result)

    if request.form.get('blueprint'):
        blueprint = request.form.get('blueprint')
        query = f"select * from weaponsBlueprint join weaponsData on weaponsData.Name=weaponsBlueprint.Name where weaponsBlueprint.Name='{blueprint}'"
        result = get_data_from_db(query)
        return render_template("resultBP.html", rows=result)

    if request.form.get('parts'):
        parts = request.form.get('parts')
        query = f"select * from weaponsResource join weaponsBlueprint on weaponsBlueprint.Name=weaponsResource.Name where weaponsResource.Name='{parts}'"
        result = get_data_from_db(query)
        return render_template("resultParts.html", rows=result)


@app.route('/primary', methods=['GET', 'POST'])
def primary():
    all_primary = get_data_from_db("SELECT Name FROM weaponsBlueprint;")
    return render_template("primary.html", options=all_primary)

@app.route('/blueprint', methods=["GET"])
def blueprint():
    all_bp = get_data_from_db("SELECT Name FROM weaponsBlueprint;")
    return render_template("blueprint.html", options=all_bp)

@app.route('/parts', methods=["GET"])
def parts():
    all_parts = get_data_from_db("SELECT Name FROM weaponsResource;")
    return render_template("parts.html", options=all_parts)
    
if __name__ == '__main__':
    app.run()
