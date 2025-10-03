from flask import Flask, g, render_template
from werkzeug.exeptions import BadRequest
from blog.views.users import users_app

app = Flask(__name__)

@app.route("/hello/")
@app.route("/hello/")
def hello(name=None):
  return render_template("hello.html", name=name)

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

@app.route("/power/")
def power_value():
  x = request.args.get("x") or ""
  y = request.args.get("y") or ""
  if not (x.isdigit() and y.isdigit()):
    app.logger.info("its invalid", x, y)
    raise BadRequest("need valid")
  x = int(x)
  y = int(y)
  result = x ** y
  app.logger.debug("yeah it works", x, y, result)
  return str(result)

@app.route("/devide-by-zero/")
def do_zero_division():
  return 1/0

@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(error):
  print(error)
  app.logger.exeption("stop zero division traceback error")
  return "never do so", 400

app.register_blueprint(users_app, url_prefix="/users")
