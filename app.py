from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    algorithm = request.form["algorithm"]
    benchmark = request.form["benchmark"]
    upper_limit = int(request.form["upperLimit"])
    num_processes = int(request.form["numProcesses"])

    return (
        f"Algorithm: {algorithm}<br>"
        f"Benchmark: {benchmark}<br>"
        f"Upper Limit: {upper_limit}<br>"
        f"Processes: {num_processes}<br>"
    )

if __name__ == "__main__":
    app.run(debug=True)