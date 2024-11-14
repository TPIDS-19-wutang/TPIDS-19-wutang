from flask import Flask, redirect, request, render_template
from http_client import HTTPClient

http_client = HTTPClient("http://wutang-lb-1220613326.us-east-2.elb.amazonaws.com")

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


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form_data = {
            "name": request.form.get("name"),
            "lastname": request.form.get("lastname"),
            "email": request.form.get("email"),
            "topic": request.form.get("topic"),
            "message": request.form.get("message"),
        }
        http_client.post("/contacts", data=form_data)
        return redirect("/")
    return render_template("contact.html")


@app.route("/habitaciones")
def rooms():
    return render_template("rooms.html")


@app.route("/reservas")
def reservas():
    return render_template("reservas.html")


if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)
