from flask import Flask, redirect, request, render_template
import requests

url = "http://wutang-lb-1220613326.us-east-2.elb.amazonaws.com"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/base", methods=["GET", "POST"])
def base():
    if request.method == "POST":
        form_Type = request.args.get("form")

        if form_Type == "register":
            form_data = {
                "email": request.form.get("email"),
                "password": request.form.get("password"),
            }

            print("Datos de Registro:", form_data)

        else:
            form_data = {
                "email": request.form.get("email"),
                "password": request.form.get("password"),
            }

            print("Datos de Inicio de Sesión:", form_data)


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
                "name": request.form.get("name"),
                "lastname": request.form.get("lastname"),
                "email": request.form.get("email"),
            },
            "reservationDetails": {
                "Location": request.form.get("Location"),
                "NumberOfPeople": request.form.get("NumberOfPeople"),
                "NumberOfAdults": request.form.get("NumberOfAdults"),
                "NumberOfChildrens": request.form.get("NumberOfChildrens"),
                "RoomType": request.form.get("RoomType"),
            },
            "paymentDetails": {
                "payerName": request.form.get("payerName"),
                "payerLastname": request.form.get("payerLastname"),
                "CardNumber": request.form.get("CardNumber"),
                "ExpirationDate": request.form.get("ExpirationDate"),
                "CVV": request.form.get("CVV"),
            }
        }    
        requests.post(f'{url}/reservas', data=form_data)
        return redirect("/")
    return render_template("reservas.html")


if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)
