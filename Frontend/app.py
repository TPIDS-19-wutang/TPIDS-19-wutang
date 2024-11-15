from flask import Flask, redirect, request, render_template
import requests

url = "http://wutang-lb-1220613326.us-east-2.elb.amazonaws.com"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/base", methods=["GET", "POST"])
def base():
    return render_template("base.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form_data = {
            "name": request.form["name"],
            "lastname": request.form["lastname"],
            "email": request.form["email"],
            "topic": request.form["topic"],
            "message": request.form["message"],
        }
        requests.post(f'{url}/contacts', data=form_data)
        return redirect("/")
    return render_template("contact.html")


@app.route("/habitaciones")
def rooms():
    return render_template("rooms.html")


@app.route("/reservas", methods=["GET", "POST"])
def reservas():
    
    if request.method == "POST":
        form_data = {
            "personalDetails": {
                "name": request.form["name"],
                "lastname": request.form["lastname"],
                "email": request.form["email"],
                "phone": request.form["phone"],
                "dni": request.form["dni"],
            },
            "reservationDetails": {
                "Location": request.form["Location"],
                "NumberOfPeople": request.form["NumberOfPeople"],
                "RoomType": request.form["RoomType"],
                "Checkin": request.form["Checkin"],
                "Checkout": request.form["Checkout"],
            },
        }    
        requests.post(f'{url}/reservas', data=form_data)
        return redirect("/")
    return render_template("reservas.html")


if __name__ == "__main__":
    app.run("127.0.0.1", port="8080", debug=True)
