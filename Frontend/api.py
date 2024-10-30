from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route("/")
def curriculum():
    return render_template("index.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)