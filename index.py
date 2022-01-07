import flask
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return render_template("1.html")


if __name__ == "__main__":
    app.run("0.0.0.0",5000)