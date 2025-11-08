from flask import Flask, request, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = "data.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    return render_template("index.html")

# deliberately vulnerable search endpoint (SQL injection)
@app.route("/search", methods=["GET", "POST"])
def search():
    q = request.values.get("q", "")
    db = get_db()
    # DANGEROUS: direct string concatenation used intentionally for lab
    query = f"SELECT id, title, body FROM posts WHERE title LIKE '%{q}%' OR body LIKE '%{q}%'"
    try:
        cur = db.execute(query)
        rows = cur.fetchall()
    except Exception as e:
        rows = []
    return {"query": query, "results": [{"id": r[0], "title": r[1], "body": r[2]} for r in rows]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
