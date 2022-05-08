from flask import Flask, render_template, request

app = Flask(__name__)

#alright now lets try to download and run flask once we have a bit more of the cosmetics

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/sources")
def sources():
    return render_template('sources.html')
  