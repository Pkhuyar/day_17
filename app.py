from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

# never enable debug mode on production
@app.route('/de/<name>')
def deb(name):
    return "The name 5th character is {}".format(name)[5]


# custom error page.
@app.errorhandler(404)
def page_400(e):
    return render_template("404.html"), 404

app.run(debug=True)