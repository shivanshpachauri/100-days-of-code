import random
from flask import Flask
app=Flask(__name__)


@app.route("/")
def guess():
    return"<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"
random1=random.randint(0,9)
print(random1)

@app.route("/<int:number>")
def number(number):
    if(number>random1):
        return "<h1 style='font-color:red;'>Too high,try again!</h1>" \
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    if(number<random1):
        return "<h1 style='font-color:red;'>Too low,try again!</h1>" \
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    if (number==random1):
        return"<h1 style='font-color:red;'>Correct</h1>" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if(__name__=="__main__"):
    app.run(debug=True)