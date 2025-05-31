import datetime
import random
from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    random_number=random.randint(0,9)
    current_date=datetime.date.today()
    return render_template("index.html",num=random_number,date=current_date)

if __name__=="__main__":
    app.run(debug=True)