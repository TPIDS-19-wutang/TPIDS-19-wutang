from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/habitaciones")
def rooms():
    return render_template("rooms.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)