import time
from flask import Flask, render_template
import requests

date = time.strftime('%Y')
YOUR_NAME="Filip Wadolowski"
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", name="hello world!",
                           CURRENT_YEAR=date,
                           YOUR_NAME=YOUR_NAME)


@app.route('/guess/<some_name>')
def geuss(some_name):
    gender_req = requests.get(url=f"https://api.genderize.io?name={some_name}")
    gender = gender_req.json()["gender"]
    age_req = requests.get(url=f"https://api.agify.io?name={some_name}")
    age = age_req.json()["age"]
    return render_template("index.html", name=some_name.title(),
                           gender=gender, age=age, YOUR_NAME=YOUR_NAME)


if __name__ == "__main__":
    app.run(debug=True)
