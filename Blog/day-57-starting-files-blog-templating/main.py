from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_response=requests.get(" https://api.npoint.io/cabae28174c0fd805b41")

    blog_data=blog_response.json()
    return render_template("index.html",posts=blog_data)
@app.route("/read/<id>")
def blog_post(id):
    
    blog_response=requests.get(" https://api.npoint.io/cabae28174c0fd805b41")
    blog_data=blog_response.json()
    
    title=""
    subtitle=""
    body=""
    for data in blog_data:
        if(data["id"]==int(id)):
            title=data['title']
            subtitle=data['subtitle']
            body=data['body']
    return render_template("post.html",title=title,subtitle=subtitle,body=body)    

if __name__ == "__main__":
    app.run(debug=True)
