#!/usr/bin/env python3
import flask
import sqlite3

app = flask.Flask(__name__)

def db_search(code):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM country WHERE code='{code}'")
        found = cur.fetchone()
    return None if found is None else found[0]

@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route('/api/search', methods=['POST'])
def api_search():
    code =  request.values.get('code')
    name = db_search(code)
    if name is None:
        flask.abort(404, "No such country")
    return {'name': name}

if __name__ == '__main__':
    app.run(debug=True)
