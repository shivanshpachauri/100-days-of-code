import requests
from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return ("hello world")

@app.route('/guess/<username>')
def main(username):
    age_response=requests.get(f"https://api.agify.io/?name={username}")
    age_data=age_response.json()
    name=age_data['name'].title()
    age=age_data['age']
    gender_response=requests.get(f"https://api.genderize.io?name={username}")
    gender_data=gender_response.json()
    gender=gender_data['gender']
    return render_template("index.html",name=name,age=age,gender=gender)

@app.route("/blog")
def blog():
    blog_response=requests.get(" https://api.npoint.io/45d977900c38815e64d1")
    # https://api.npoint.io/45d977900c38815e64d1
    blog_data=blog_response.json()
    return render_template("blog.html",posts=blog_data)

if (__name__=="__main__"):
    app.run(debug=True)