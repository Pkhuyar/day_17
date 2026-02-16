from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)


#response = requests.get(url, params={"userId": user_id})

@app.route('/', methods=["GET"])
def Home():
    user_id = request.args.get("userid")
    posts = []

    #print(response)
    if user_id:
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url, params={"userId": user_id})
        #print(posts)
        if response.status_code == 200:
            posts = response.json()

    return render_template("home.html",posts=posts)


app.run(debug=True)
