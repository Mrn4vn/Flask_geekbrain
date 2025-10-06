from flask import Blueprint, render_template

articles_app = Blueprint("articles_app", __name__)

ARTICLES = ["beer", "sleep", "coffee"]

@articles_app.route("/", endpoint="list")
def articles_list():
  return render_template("articles/list.html", articles=ARTICLES)
