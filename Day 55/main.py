from flask import Flask
app=Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>"+function()+"</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>"+function()+"</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return"<u>"+function()+"</u>"
    return wrapper


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello():
    return("<header style='display:flex;flex-direction:column;gap:10px;align-items:center;justify-content:center;border:1px solid black'>"
    "<h1 style='text-align:center;text-transform:capitalize; '>hello</h1>"
    "<img style='width:150px;' src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWppazZyeWJlejV0cGsyNGk0aXJvZnpnMWxyZWcxbnNkODUyZHh1eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o6Zt3b4x0OaTN9hXa/100.webp'alt='kitten;'/>"
    "</header>")


@app.route("/username/<name>/<int:number>")
def greet(name,number):
    print(name,number)
    return f"<main><p style='text-align:center;text-transform:capitalize; line-height:1.25'>hello {name} {number}!</p></main>"


if(__name__=='__main__'):
    app.run(debug=True)