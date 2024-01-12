from flask import Flask, render_template, request, redirect, url_for
import requests, os

app = Flask(__name__)

api_host = os.getenv("API_HOST", "api")

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200

@app.route("/", methods=["GET", "POST"])
def index():
    api_url = "http://"+api_host+":5001/api/quotes"
    if request.method == "POST":
        quote = request.form["quote"]
        author = request.form["author"]
        requests.post(
            api_url, json={"quote": quote, "author": author}
        )
        return redirect(url_for("index"))
    else:
        quotes = requests.get(api_url).json()
        return render_template("index.html", quotes=quotes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
