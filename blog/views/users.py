from flask import Blueprint, render_template

users_app = Blueprint("users_app", __name__)
USERS = {
  1: "Lelik",
  2: "Bolik",
  3: "Archibald von Vising",
}

@users_app.route("/")
def users_list():
  return render_template("users/list.html", users=USERS)
