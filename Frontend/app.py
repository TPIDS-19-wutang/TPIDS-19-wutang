from flask import Flask, redirect, request, render_template, session, url_for
import requests
from flask_mail import Mail, Message


url = "http://backend:5001"

app = Flask(__name__)
app.secret_key = 'Trivium23246568!'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Cambia según el servidor SMTP
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'iblanco@fi.uba.ar'  # Tu correo
app.config['MAIL_PASSWORD'] = 'JQjX-aa?'        # Contraseña o App Password
app.config['MAIL_DEFAULT_SENDER'] = 'iblanco@fi.uba.ar'

mail = Mail(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route("/")
def index():
     try:
        # Hacer la solicitud GET
        response_hoteles = requests.get(f'{url}/hoteles_end')
        response_testimonios = requests.get(f'{url}/testimonial_end')
    
        # Verificar el codigo de estado de la respuesta
        if response_hoteles.status_code == 200 and  response_testimonios.status_code == 200:
            # Decodificar el JSON de la respuesta
            data_hoteles = response_hoteles.json()
            data_testimonios = response_testimonios.json()
            
            if data_hoteles.get("status") == "success" and data_testimonios.get("status") == "success":
                hotels_data = {
                    hotels["id_hotel"]: {
                        "location":hotels["location"],
                        "description":hotels["description"],
                        "image":hotels["image"],
                        "cant_rooms":hotels["cant_rooms"],
                        "floors":hotels["floors"],
                        "stars":hotels["stars"]} 
                    for hotels in data_hoteles.get("data", [])
                }
                
                testimonios = [
                    {
                        "testimonio": testimonial["testimonio"],
                        "name": testimonial["name"],
                        "location": testimonial["location"]
                    }  for testimonial in data_testimonios.get("data", [])
                ]
            else:
                print(f"Error en el backend: {data.get('message', 'Sin mensaje')}")
                hotels_data = {}
                testimonios = []
        else:
            print(f"Error en la solicitud: {response.status_code} - {response.reason}")
            hotels_data = {}
            testimonios = []
     except requests.RequestException as e:
        print(f"Error al conectarse con el servidor: {e}")
        hotels_data = {}
        testimonios = []
     return render_template("index.html",hoteles=hotels_data, limite_id = 3, testimonios=testimonios)


@app.route("/base", methods=["GET", "POST"])
def base():
    return render_template("base.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        form_data = {
            "email": request.form["email"],
            "password": request.form["password"],
        }
        response = requests.post(f'{url}/login_user', data=form_data)
        
        if response.status_code == 200 and response.json().get("status") == "success":
            session['username'] = request.form["email"]
            session.permanent = False
            return redirect("/")
        
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        form_data = {
            "email": request.form["email"],
            "password": request.form["password"],
            "name": request.form["name"],
            "lastname": request.form["lastname"],
            "dni": request.form["dni"],
            "phone": request.form["phone"]
        }
        response = requests.post(f'{url}/register_user', data=form_data)
        if response.status_code == 200 and response.json().get("status") == "success":
            return redirect("/")
    return render_template("register.html")

@app.route("/recover", methods=["GET", "POST"])
def recover():
    if request.method == "POST":
        form_data = {
            "email": request.form["email"],
            "password": request.form["password"],
        }
        try:
            response = requests.post(f'{url}/recover_pass', data=form_data)
            if response.status_code == 200:
                return redirect("/login")
            else:
                return f"Error: {response.json().get('message', 'No se pudo actualizar la contraseña')}", 400
        except Exception as e:
            return f"Error al conectarse con el backend: {str(e)}", 500
    return render_template("recover.html")


@app.route("/FAQ")
def FAQ():
    try:
        # Hacer la solicitud GET
        response = requests.get(f'{url}/faq_end')
    
        # Verificar el c�digo de estado de la respuesta
        if response.status_code == 200:
            # Decodificar el JSON de la respuesta
            data = response.json()
            if data.get("status") == "success":
                faq_data = {
                    faq["question"]: faq["answer"] for faq in data.get("data", [])
                }
            else:
                print(f"Error en el backend: {data.get('message', 'Sin mensaje')}")
                faq_data = {}
        else:
            print(f"Error en la solicitud: {response.status_code} - {response.reason}")
            faq_data = {}
    except requests.RequestException as e:
        print(f"Error al conectarse con el servidor: {e}")
        faq_data = {}
    return render_template("FAQ.html", secciones=faq_data)


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
    try:

        response = requests.get(f'{url}/type_rooms')
        
        if response.status_code == 200:
           
            data = response.json()
            cuartos = data.get("data", [])

            if data.get("status") == "success":
                cuartos = {
                    index: {
                        "type_room": type_room["type_room"],
                        "image": type_room["image"],
                        "description": type_room["description"]
                    } for index, type_room in enumerate(data.get("data", []))
                }
            else:
                print(f"Error en el backend: {data.get('message', 'Sin mensaje')}")
                cuartos = {}
        else:
            print(f"Error en la solicitud: {response.status_code} - {response.reason}")
            cuartos = {}
    except requests.RequestException as e:
        print(f"Error al conectarse con el servidor: {e}")
        cuartos = {}
    return render_template("rooms.html", cuartos=cuartos)


def send_reservation_email(to_email, reservation_id):
    if not reservation_id:
        print("No se ha recibido un ID de reserva válido.")
        return
    subject = "Confirmación de reserva"
    html_content = f"""
    <html>
    <body>
        <h1>Reserva confirmada</h1>
        <p>Gracias por realizar tu reserva. Aquí están los detalles:</p>
        <p><strong>ID de la reserva:</strong> {reservation_id}</p>
        <p>Si tienes alguna pregunta, no dudes en contactarnos.</p>
    </body>
    </html>
    """

    try:
        msg = Message(subject=subject, recipients=[to_email])
        msg.html = html_content
        mail.send(msg)
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error enviando correo: {str(e)}")

@app.route("/reservas", methods=["GET", "POST"])
def reservas():
    if 'username' in session:
        hotels = requests.get(f'{url}/hoteles_end')
        hotel_json = hotels.json()
        hoteles = hotel_json.get("data", [])

        if hotel_json.get("status") == "success":
          pass
        else:
            print(f"Error en el backend: {data.get('message', 'Sin mensaje')}")
            hoteles = []      
        if request.method == "POST":
            id_hotel = request.form.get("id_hotel")
            location = request.form.get("location")
            print(f"ID Hotel: {id_hotel}, Location: {location}")  # Depuración

            form_data = {
                    "id_hotel": id_hotel,
                    "name": request.form["name"],
                    "lastname": request.form["lastname"],
                    "email": request.form["email"],
                    "phone": request.form["phone"],
                    "dni": request.form["dni"],
                    "location": location,
                    "number_people": request.form["NumberOfPeople"],
                    "type_room": request.form["RoomType"],
                    "check_in": request.form["Checkin"],
                    "check_out": request.form["Checkout"],
            }
            response = requests.post(f'{url}/reservation', data=form_data)
            

            if response.status_code == 200:
                
                id_reservation = response.json().get("id_reservation")
                print(f"ID de reserva recibido: {id_reservation}")
                send_reservation_email(form_data["email"], id_reservation)


            return redirect("/")
        return render_template("reservas.html", hoteles=hoteles)
    else:
        return redirect(url_for('login'))

@app.route("/consultar-reserva", methods=["GET", "POST"])
def consultar_reserva():
    if request.method == "POST":
        reservation_code = request.form.get("reservation_code")
        lastname = request.form.get("lastname")

        if not reservation_code or not lastname:
            error_message = "Por favor, ingrese el código de reserva y el apellido."
            return render_template("consultar_reserva.html", reservation=None, error_message=error_message)

        try:
            response = requests.get(f'{url}/reservation/{reservation_code}', params={"lastname": lastname})
            datos_json = response.json()

            if datos_json.get("status") == "success":
                reservation_data = datos_json.get("data", {})
                return render_template("consultar_reserva.html", reservation=reservation_data, error_message=None)
            else:
                error_message = "No se encontró ninguna reserva con el código y apellido proporcionado."
        except Exception as e:
            error_message = f"Error al procesar la reserva: ingrese formato valido"

        return render_template("consultar_reserva.html", reservation=None, error_message=error_message)
    
    return render_template("consultar_reserva.html", reservation=None, error_message=None)



if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
