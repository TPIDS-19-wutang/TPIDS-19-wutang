from flask import Flask, request, jsonify
from sql import *
from datetime import datetime

app = Flask(__name__)

app.json_provider_class.ensure_ascii = False


#--------------------------------------------------USERS------------------------------------------------------------------------

@app.route('/user/<int:id_user>', methods=['GET'])
def user_details_endp(id_user):
    """
    Endpoint para obtener los detalles de un usuario especifico.
    Recupera la informacion del usuario con el id proporcionado.
    """
    response = get_user(id_user)
    return jsonify(response)

@app.route('/login_user', methods=['POST'])
def user_login_endp():
    """
    Endpoint para obtener los detalles de un usuario especifico.
    Recupera la informacion del usuario con el id proporcionado.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    
    response = log_in(email, password)
    return jsonify(response)

@app.route('/register_user', methods=['POST'])
def user_register_endp():
    """
    Endpoint para obtener los detalles de un usuario especifico.
    Recupera la informacion del usuario con el id proporcionado.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    name = request.form.get('name')
    lastname = request.form.get('lastname')
    dni = request.form.get('dni')
    phone = request.form.get('phone')
    
    response = register(email, password, name, lastname, dni, phone)
    return jsonify(response)


@app.route('/users', methods=['GET'])
def users_list_endp():
    """
    Endpoint para obtener una lista de todos los usuarios.
    Recupera todos los usuarios almacenados en el sistema.
    """
    response = get_all_users()
    return jsonify(response)

@app.route('/user/<int:id_user>', methods=['DELETE'])
def remove_user_endp(id_user):
    """
    Endpoint para eliminar un usuario especifico.
    Elimina el usuario con el id proporcionado.
    """
    response = delete_user(id_user)
    return jsonify(response)


@app.route('/user/<int:id_user>', methods=['PUT'])
def update_user_details(id_user):
    """
    Endpoint para actualizar los detalles de un usuario especifico.
    Actualiza los datos del usuario con el id proporcionado con los nuevos datos.
    """
    data = request.get_json()
    name = data.get('name')
    lastname = data.get('lastname')
    phone = data.get('phone')
    dni = data.get('dni')

    response = update_user(id_user, name, lastname, phone, dni)
    return jsonify(response)

#--------------------------------------------------HABITACIONES-----------------------------------------------------------------

@app.route('/type_rooms', methods=['GET'])
def get_all_type_rooms_end():
    """
    Endpoint para obtener todas las habitaciones.
    """
    result = get_all_type_rooms()
    return jsonify(result)


@app.route('/hoteles_end', methods=['GET'])
def get_all_hotels_end():
    """
    Endpoint para obtener todos los hoteles.
    """
    result = get_all_hotels()
    return jsonify(result)

@app.route('/testimonial_end', methods=['GET'])
def get_all_testimonial_end():
    """
    Endpoint para obtener todas los testimonios.
    """
    result = get_all_testimonial()
    return jsonify(result)




@app.route('/rooms/<int:id_hotel>', methods=['GET'])
def get_rooms(id_hotel):
    """
    Endpoint para obtener todas las habitaciones.
    """
    result = get_rooms_by_hotel(id_hotel)
    return jsonify(result)

@app.route('/room', methods=['POST'])
def create_room_endp():
    """
    Endpoint para agregar una habitacion.
    """
    data = request.get_json()
    result = create_room(
        id_hotel=data['id_hotel'],
        type_room=data['type_room'],
        title=data['title'],
        description=data['description'],
        image=data['image'],
        price=data['price']
    )
    return jsonify(result)

@app.route('/rooms/<int:id_room>', methods=['DELETE'])
def delete_room_endpoint(id_room):
    """
    Endpoint para eliminar una habitacin.
    """
    result = delete_room(id_room)
    return jsonify(result)

@app.route('/rooms/<int:id_room>', methods=['PUT'])
def update_room_endpoint(id_room):
    """
    Endpoint para actualizar los detalles de una habitacion existente.
    """
    data = request.get_json()
    result = update_room(
        id_room,
        data['id_hotel'],
        data['type_room'],
        data['title'],
        data['description'],
        data['image'],
        data['price']
    )
    return jsonify(result)


@app.route('/rooms/availability', methods=['GET'])
def endp_room_availability():
    """
    Endpoint para verificar la disponibilidad de una habitación.
    :return: JSON con el estado de la operación (éxito o error).
    """
   
    type_room = request.args.get('type_room')
    id_hotel = request.args.get('id_hotel')    
    check_in = request.args.get('check_in')  

    if not type_room or not id_hotel or not check_in:
        return jsonify({"status": "error", "message": "Faltan parámetros en la solicitud."}), 400

    check_in_date = None
    try:
        check_in_date = datetime.strptime(check_in, '%Y-%m-%d')
    except ValueError:
        return jsonify({"status": "error", "message": "El parámetro 'check_in' tiene un formato incorrecto. Debe ser YYYY-MM-DD."}), 400

    response = check_room_availability(type_room, id_hotel, check_in_date)

    if response['status'] == 'success':
        return jsonify(response), 200
    else:
        return jsonify(response), 404



#----------------------------------------------------------RESERVAS----------------------------------------------------------------

@app.route('/reservations', methods=['GET'])
def get_all_reservations_endp():
    """
    Endpoint para obtener todas las reservaciones.
    Recupera todas las reservaciones almacenadas en el sistema.
    """
    result = get_all_reservations()
    return jsonify(result)

@app.route('/reservation/<int:id_reservation>', methods=['GET'])
def get_reservation_by_id_and_lastname_endp(id_reservation):
    """
    Endpoint para obtener una reserva específica asociadas al código de reserva y apellido proporcionado.
    """
    lastname = request.args.get('lastname')
    if not lastname:
        return jsonify({"status": "error", "message": "Falta el apellido en la solicitud."}), 400
    
    result = get_reservation_by_id_and_lastname(id_reservation, lastname)
    return jsonify(result)


@app.route('/reservation', methods=['POST'])
def add_reservation_endp():
    """
    Endpoint para crear una nueva reservacion.
    Crea una nueva reservacion con los datos proporcionados en el cuerpo de la solicitud.
    """

    data = request.form
    
    user = get_user_id_by_email_and_dni(data.get('email'), data.get('dni'))

    if not user:
        return jsonify({"error": "Usuario no encontrado"})
    id_user = user.get('data')
    
    id_hotel=data.get('id_hotel')
    number_people=data.get('number_people')
    type_room= data.get('type_room')
    check_in=data.get('check_in')
    check_out=data.get('check_out') 
    
    room_response = check_room_availability(type_room, id_hotel, check_in)
    
    if room_response['status'] == "error":
        return jsonify(room_response)  
        
    id_room = room_response['data']
    
    result = add_reservation(id_user, id_room, id_hotel, number_people, check_in, check_out)

    return jsonify(result)

@app.route('/reservation/<int:id_user>', methods=['DELETE'])
def delete_reservation_endp(id_user):
    """
    Endpoint para eliminar la reservacion de un usuario especifico.
    Elimina la reservacion asociada al usuario con el id proporcionado.
    """
    result = delete_reservation(id_user)
    return jsonify(result)

@app.route('/reservations/hotel/<int:id_hotel>', methods=['GET'])
def get_reservations_by_hotel_endp(id_hotel):
    """
    Endpoint para obtener todas las reservaciones de un hotel especifico.
    Recupera todas las reservaciones asociadas al hotel con el id proporcionado.
    """
    result = get_reservations_by_hotel(id_hotel)
    return jsonify(result)

@app.route('/reservations/user/<int:id_user>', methods=['GET'])
def get_reservations_by_user_endp(id_user):
    """
    Endpoint para obtener todas las reservaciones de un usuario especifico.
    Recupera todas las reservaciones asociadas al usuario con el id proporcionado.
    """
    result = get_reservation_by_user(id_user)
    return jsonify(result)


@app.route("/recover_pass", methods=["POST"])
def recover_endp():
    """
    Endpoint para recuperar o modificar la contraseña de un usuario.
    Este endpoint recibe el email y la nueva contraseña, y la actualiza en la base de datos.
    """
    data = request.form
    email = data.get("email")
    new_password = data.get("password")

    # Verificar si el usuario existe en la base de datos
    user = get_user_by_email(email)
    if not user:
        return jsonify({"status": "error", "message": "Usuario no encontrado"})

    # Actualizar la contraseña del usuario en la base de datos (sin encriptar)
    success = update_user_password(email, new_password)
    if success:
        return jsonify({"status": "success", "message": "Contraseña actualizada exitosamente"})
    else:
        return jsonify({"status": "error", "message": "No se pudo actualizar la contraseña"})


@app.route('/reservations/active', methods=['GET'])
def get_active_reservations_endp():
    """
    Endpoint para obtener todas las reservaciones activas.
    Recupera todas las reservaciones que estan activas (no canceladas ni finalizadas).
    """
    result = get_active_reservations()
    return jsonify(result)

@app.route('/faq_end', methods=['GET'])
def get_faq_endp():
    """
    Endpoint para obtener todas las reservaciones activas.
    Recupera todas las reservaciones que estan activas (no canceladas ni finalizadas).
    """
    return jsonify(get_all_faq())

@app.route('/reservations/<int:id_reservation>/services', methods=['GET'])
def get_services_by_reservation_endp(id_reservation):
    """
    Endpoint para obtener todos los servicios asociados a una reserva.
    """
    result = get_services_by_reservation(id_reservation)
    return jsonify(result)

@app.route('/reservations/<int:id_reservation>/services', methods=['PUT'])
def update_services_by_reservation_endp(id_reservation):
    """
    Endpoint para actualizar los servicios contratados de una reserva.
    Recibe una lista de IDs de servicios a contratar y actualiza los servicios asociados a la reserva.
    """
    data = request.get_json()
    if not data or 'services' not in data:
        return jsonify({"status": "error", "message": "La lista de servicios no es válida"}), 400

    services = data['services']
    result = update_services_by_reservation(id_reservation, services)
    return jsonify(result)

@app.route('/reservations/<int:id_reservation>/services/<int:id_service>', methods=['DELETE'])
def delete_service_from_reservation_endp(id_reservation, id_service):
    """
    Endpoint para eliminar un servicio específico de una reserva.
    """
    result = delete_service_from_reservation(id_reservation, id_service)
    return jsonify(result)

#---------------------------------------------------HOTELES-----------------------------------------------------------------

@app.route('/hotel', methods=['POST'])
def add_hotel_endp():
    """
    Endpoint para agregar un nuevo hotel al sistema.
    Crea un nuevo hotel con los datos proporcionados en el cuerpo de la solicitud.
    """
    data = request.get_json()
    result = add_hotel(
        location=data['location'],
        description=data['description'],
        image=data['image'],
        cant_rooms=data['cant_rooms']
    )
    return jsonify(result)

@app.route('/hotel/<int:id_hotel>', methods=['DELETE'])
def delete_hotel_endp(id_hotel):
    """
    Endpoint para eliminar un hotel especifico del sistema.
    Elimina el hotel con el id proporcionado.
    """
    result = delete_hotel(id_hotel)
    return jsonify(result)

@app.route('/hotel/<int:id_hotel>', methods=['PUT'])
def update_hotel_endp(id_hotel):
    """
    Endpoint para actualizar los detalles de un hotel existente.
    Actualiza los detalles del hotel con el id proporcionado con los nuevos datos.
    """
    data = request.get_json()
    result = update_hotel(
        id_hotel=id_hotel,
        title=data['title'],
        description=data['description'],
        image=data['image'],
        cant_rooms=data['cant_rooms']
    )
    return jsonify(result)

@app.route('/hotel/<int:id_hotel>', methods=['GET'])
def get_hotel_endp(id_hotel):
    """
    Endpoint para obtener los detalles de un hotel específico.
    """
    response = get_hotel_by_id(id_hotel)
    
    return jsonify(response)
    
#---------------------------------------------------SERVICES-----------------------------------------------------------------

@app.route('/services', methods=['GET'])
def get_all_services_endp():
    """
    Endpoint para obtener todos los servicios disponibles.
    """
    services = get_all_services()
    return jsonify(services)

@app.route('/services', methods=['POST'])
def add_service_endp():
    """
    Endpoint para agregar un nuevo servicio al sistema.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"status": "error", "message": "Faltan datos requeridos (name, description, price)"}), 400

    result = add_service(
        name=data['name'],
        description=data['description'],
        price=data['price']
    )
    return jsonify(result)

@app.route('/services/<int:id_service>', methods=['PUT'])
def update_service_endp(id_service):
    """
    Endpoint para actualizar los detalles de un servicio específico.
    """
    data = request.get_json()
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"status": "error", "message": "Faltan datos requeridos (name, description, price)"}), 400

    result = update_service(
        id_service=id_service,
        name=data['name'],
        description=data['description'],
        price=data['price']
    )
    return jsonify(result)


@app.route('/services/<int:id_service>', methods=['DELETE'])
def delete_service_endp(id_service):
    """
    Endpoint para eliminar un servicio específico del sistema.
    """
    result = delete_service(id_service)
    return jsonify(result)

if __name__ == '__main__':
     app.run(port="5001", host="0.0.0.0")