from flask import Flask, g

app = Flask(__name__)

@app.route("/")
def index():
  return "Lol what?"

@app.route("/greet/<name>")
def greet_name(name: str):
  return f"Hey, {name}"

@app.route("/user/")
def read_user():
  name = request.args.get("name")
  surname = request.args.get("surname")
  return f"User {name or '[no name]'} {surname or '[no surname]'}"

@app.route("/status/", methods=["GET", "POST"])
def custom_status_code():
  if request.method =="GET":
    return "that was get"

  print("raw bytes data:", request.data)

  if request.form and "code" in request.form:
    return "code from form", request.form["code"]

  if request.json and "code" in request.json:
    return "code from json", request.json["code"]

  return "", 204

@app.before_request
def process_before_request():
  """
  sets start_time to g object
  """
  g.start_time = time()

@app.after_request
def process_after_request(response):
  """
  adds process time in headers
  """
  if hasattr(g, "start_time"):
    response.headers["process-time"] = time() - g.start_time
  
  return response
