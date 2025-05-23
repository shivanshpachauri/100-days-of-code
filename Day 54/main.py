# import requests
# requests.get("")

# in the terminal type:
# flask --app main run
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return"<header><h1>Hello,world</h1><a href='/app'>navigate to app</a></header><footer>this is a footer</footer>"

@app.route('/app')
def this():
    return"<main><p>navigated to the app <a href='/'>click here to navigate to main</a></p><h1><a href='/app/1'>to the dynamic styles</a></h1></main>"
if (__name__=='__main__'):
    app.run(debug=True)
# @app.route('/app/1')
# def this():
#     return"<main><p>navigated to the app <a href='/'>click here to navigate to main</a></p></main>"