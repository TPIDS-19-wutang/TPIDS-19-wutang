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

@app.route("/FAQ")
def FAQ():
    secciones = {
    "Section 1": "Contenido de la seccion 1",
    "Section 2": "Contenido de la seccion 2",
    "Section 3": "Contenido de la seccion 3",
}
    return render_template("FAQ.html", secciones=secciones)


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
    cuartos ={"1":{
              "descripcion":"Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero sed incidunt a vel expedita beatae, assumenda ad ex dolor ea dignissimos ipsa esse voluptas praesentium laudantium dolorem inventore quae architecto",
              "imagen":"/images/habitacion_classic.jpg",
              "tipo":"Classic"},
              
              "2":{
              "descripcion":"Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero sed incidunt a vel expedita beatae, assumenda ad ex dolor ea dignissimos ipsa esse voluptas praesentium laudantium dolorem inventore quae architecto",
              "imagen":"/images/habitacion_doble.jpg",
              "tipo":"Doble"},
              
              "3":{
              "descripcion":"Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero sed incidunt a vel expedita beatae, assumenda ad ex dolor ea dignissimos ipsa esse voluptas praesentium laudantium dolorem inventore quae architecto",
              "imagen":"/images/habitacion_premium.jpg",
              "tipo":"Premium"},
              
              "4":{
              "descripcion":"Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero sed incidunt a vel expedita beatae, assumenda ad ex dolor ea dignissimos ipsa esse voluptas praesentium laudantium dolorem inventore quae architecto",
              "imagen":"/images/habitacion_deluxe.jpg",
              "tipo":"Deluxe"}
                   
              }
    return render_template("rooms.html", cuartos=cuartos)


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
