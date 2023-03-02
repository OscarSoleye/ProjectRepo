from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

@app.route("/hello")
def hello_world():
    return "<p>Everytime i Go out, you know i bring them hoes out!</p>"
    #This will be outputted in the broweser at http://127.0.0.1:5000

