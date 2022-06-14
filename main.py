from flask import Flask, render_template
from utils import get_candidates, get_candidates_by_uid, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = get_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:uid>")
def page_candidates(uid):
    candidate = get_candidates_by_uid(uid)
    return render_template("card.html", candidate=candidate)


@app.route("/candidate_name/<candidate_name>")
def page_candidate_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def page_skills(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)


app.run()
