from flask import Flask, render_template
from utils import get_candidates, get_candidates_by_uid

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = get_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:uid>")
def page_candidates(uid):
    candidate = get_candidates_by_uid(uid)
    return render_template("card.html", candidate=candidate)


app.run()
