from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Placeholder"

app.run(debug=True)