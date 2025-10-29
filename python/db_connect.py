import sqlite3
from flask import Flask, g

app = Flask(__name__)
DATABASE = "database.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        # дозволяє звертатись до результатів за іменами полів (зручно)
        g.db.row_factory = sqlite3.Row
    return g.db

# Дана функція викливається Flask після кожного запиту
@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()
