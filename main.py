from flask import Flask, render_template
from markupsafe import escape

main = Flask(__name__)

JOBS = [
    {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Abuja',
    'salary' : 'N1500'
    },
    {
    'id' : 2,
    'title' : 'Data Scientist',
    'location' : 'Lagos',
    'salary' : 'N2500'
    },
    {
    'id' : 3,
    'title' : 'Game Analyst',
    'location' : 'PH',
    'salary' : 'N2100'
    },
{
    'id' : 4,
    'title' : 'Security Analyst',
    'location' : 'MNH',
    }
]
@main.route("/")
def index():
    return render_template("index.html", jobs=JOBS, coursename="Wale")

