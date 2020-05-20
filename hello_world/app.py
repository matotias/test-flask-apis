from flask import Flask

app = Flask(__name__)


@app.route('/')  # '/' indicates that it's the homepage
def home():
    return "Hello World!"


app.run(port=5000)
