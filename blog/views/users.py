from flask import Blueprint, render_template
from werkzeug.exeptions import NotFound
from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db

users_app = Blueprint("users_app", __name__)
USERS = {
  1: "Lelik",
  2: "Bolik",
  3: "Archibald von Vising",
}

@users_app.route("/", endpoint="list")
def users_list():
  return render_template("users/list.html", users=USERS)

@users_app.route("/<int:user_id>/", endpoint="details")
def user_details(user_id: int):
  try:
    user_name = USERS[user_id]
  except KeyError:
    raise NotFound(f"User #{user_id} and love doesn't exist")
  return render_template("users/details.html", user_id=user_id, user_name=user_name)

class User(db.Model):
  id = Column(Integer, primary_key=True)
  username = Column(String(80), unique=True, nullable=False)
  is_staff = Column(Boolean, nullable=False, default=False)

  def __repr__(self):
    return f"<User #{self.id} {self.username!r}>"
