from ast import Try
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify
import mysql.connector
from mysql.connector import Error



DB_USER = "triviumuser"
DB_PASSWORD = "triviumpassword"
DB_HOST= "mysql-db"
DB_PORT = "3306"
DB_NAME = "triviumdb"

db_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
try:
    engine = create_engine(db_url)
    with engine.connect() as conn:
        print("Conexión exitosa con SQLAlchemy.")
except Exception as e:
    print(f"Error al conectar con SQLAlchemy: {e}")


# ------------------------------------------------------QUERYS FAQ----------------------------------------------------

QUERY_GET_FAQ = """
SELECT * FROM faq
"""

# ------------------------------------------------------QUERYS USERS----------------------------------------------------


QUERY_DELETE_USER = """
DELETE FROM users WHERE id_user = :id_user
"""

QUERY_FIND_ID_RESERVATION = """
SELECT id_reservation
FROM reservations
WHERE id_user = :id_user AND id_hotel = :id_hotel AND id_room = :id_room AND check_in = :check_in AND check_out = :check_out 
"""

QUERY_GET_USER = """
SELECT *
FROM users 
WHERE id_user = :id_user
"""

QUERY_CHECK_USER_BY_EMAIL = """
SELECT id_user FROM users WHERE email = :email
"""

QUERY_CHECK_USER_BY_PHONE = """
SELECT id_user FROM users WHERE phone = :phone
"""

QUERY_CHECK_USER_BY_DNI = """
SELECT id_user FROM users WHERE dni = :dni
"""

QUERY_GET_ID_BY_EMAIL_AND_DNI = """
SELECT id_user FROM users WHERE dni = :dni AND email = :email
"""

QUERY_GET_ALL_USERS = """
SELECT *
FROM users
"""

QUERY_ADD_USER = """
INSERT INTO users (name, lastname, email, password, dni, phone) 
VALUES (:name, :lastname, :email, :password, :dni, :phone)
"""

QUERY_UPDATE_USER = """
UPDATE users 
SET name = :name, lastname = :lastname, phone = :phone, dni = :dni 
WHERE id_user = :id_user
"""
QUERY_UPDATE_PASSWORD = """
UPDATE users SET password = :password WHERE email = :email
"""

QUERY_LOG_IN = """
SELECT * FROM users
WHERE email = :email
"""

# -----------------------------------------------------QUERYS ROOMS-----------------------------------------------------

QUERY_GET_ALL_TYPE_ROOMS = """
SELECT * FROM type_rooms
"""

QUERY_GET_TESTIMONIAL = """
SELECT * FROM testimonial
"""

QUERY_GET_ROOM = """
SELECT id_room, id_hotel, type_room, title, description, image, price, creates_at
FROM type_rooms 
WHERE id_room = :id_room
"""

QUERY_DELETE_ROOM = "DELETE FROM type_rooms WHERE id_room = :id_room"

QUERY_UPDATE_ROOM = """
UPDATE type_rooms 
SET type_room = :type_room, title = :title, description = :description, image = :image, price = :price 
WHERE id_room = :id_room
"""

QUERY_CHECK_ROOM_DUPLICATED = """
SELECT id_room 
FROM type_rooms 
WHERE id_hotel = :id_hotel AND title = :title AND description = :description AND image = :image AND price = :price
"""

QUERY_ADD_ROOM = """
INSERT INTO type_room (id_room, id_hotel, type_room, title, description, image, price) 
VALUES (NULL, :id_room, :id_hotel, :type_room, :title, :description, :image, :price)
"""

QUERY_GET_ROOMS_BY_HOTEL = """
SELECT id_room, type_room FROM reservations 
WHERE id_hotel = :id_hotel"""

QUERY_ROOMS_DISPONIBILITY = """
SELECT id_room
FROM rooms
WHERE id_hotel = :id_hotel AND id_room NOT IN (
    SELECT id_room
    FROM reservations
    WHERE check_in <= :check_in
    AND (
        check_out >= :check_in
    )
)
LIMIT 1;
"""

"""
SELECT id_room
FROM rooms
WHERE type_room = 'Doble' AND id_hotel = 1 AND id_room NOT IN (
    SELECT id_room
    FROM reservations
    WHERE (check_in < '2024-12-02' AND check_out >= '2024-12-02') 
          OR (check_in >= '2024-12-02' AND check_in < '2024-12-18')
          OR (check_out IS NULL)
)
LIMIT 1;
"""


# -----------------------------------------------------QUERYS RESERVATIONS----------------------------------------------------

QUERY_GET_ALL_RESERVATIONS = """
SELECT id_reservation, id_user, id_room, id_hotel, number_people, check_in, check_out, created_at 
FROM reservations
"""

QUERY_GET_RESERVATION = """
SELECT id_reservation, id_user, id_room, id_hotel, number_people, check_in, check_out, created_at  
FROM reservations 
WHERE id_reservation= :id_reservation
"""

QUERY_DELETE_RESERVATION = """
DELETE FROM reservations WHERE id_user = :id_user
"""

QUERY_CREATE_RESERVATION = """
INSERT INTO reservations (id_user, id_room, id_hotel, number_people,check_in, check_out) 
VALUES (:id_user, :id_room, :id_hotel, :number_people, :check_in, check_out)
"""

QUERY_ADD_RESERVATION = """
INSERT INTO reservations (id_user, id_room, id_hotel, number_people, check_in, check_out) 
VALUES (:id_user, :id_room, :id_hotel, :number_people, :check_in, :check_out)
"""

QUERY_GET_RESERVATIONS_BY_HOTEL = """
SELECT * FROM reservations WHERE id_hotel = :id_hotel;
"""

QUERY_GET_RESERVATION_BY_USER= """
SELECT * FROM reservation WHERE id_user = :id_user;
"""

QUERY_GET_ACTIVE_RESERVATIONS = """
SELECT * FROM reservations WHERE check_out > CURRENT_TIMESTAMP;
"""

QUERY_DELETE_OLD_RESERVATIONS = """
DELETE FROM reservations WHERE check_out < CURRENT_TIMESTAMP;
"""

QUERY_GET_RESERVATION_BY_ID_AND_LASTNAME ="""
SELECT r.*, u.dni, u.email, u.name, u.lastname, u.phone, h.location, h.description
FROM 
    users u
JOIN 
    reservations r ON u.id_user = r.id_user
JOIN 
    hotels h ON r.id_hotel = h.id_hotel
WHERE 
    r.id_reservation = :id_reservation
    AND u.lastname = :lastname
"""

QUERY_GET_SERVICES_BY_RESERVATION = """
SELECT s.id_service, s.name, s.description, s.price
FROM reservations AS r
LEFT JOIN reservation_services AS rs ON rs.id_reservation = r.id_reservation
LEFT JOIN services AS s ON s.id_service = rs.id_service
WHERE r.id_reservation = :id_reservation;
"""

QUERY_UPDATE_SERVICE_BY_RESERVATION = """
INSERT INTO reservation_services (id_reservation, id_service)
VALUES (:id_reservation, :id_service)
"""

QUERY_CHECK_EXISTENT_SERVICES_BY_RESERVATION = """
SELECT COUNT(*) FROM reservation_services WHERE id_reservation = :id_reservation
"""

QUERY_DELETE_SERVICE_BY_RESERVATION = """
DELETE FROM reservation_services WHERE id_reservation = :id_reservation
"""

QUERY_DELETE_SERVICE_FROM_RESERVATION = """
DELETE FROM reservation_services
WHERE id_reservation = :id_reservation AND id_service = :id_service
"""

# -----------------------------------------------------QUERYS HOTELS----------------------------------------------------

QUERY_ADD_HOTEL ="""
INSERT INTO hotels (location, description, image, cant_rooms)
VALUES (:location, :description, :image, :cant_rooms);
"""

QUERY_DELETE_HOTEL = """
DELETE FROM hotels WHERE id_hotel = :id_hotel;
"""

QUERY_UPDATE_HOTEL = """
UPDATE hotels
SET location = :location, description = :description, image = :image, cant_rooms = :cant_rooms
WHERE id_hotel = :id_hotel
"""

QUERY_GET_ALL_HOTELS = """
SELECT * FROM hotels
"""

QUERY_GET_HOTEL_BY_ID = """
SELECT location 
FROM hotels 
WHERE id_hotel = :id_hotel
"""

QUERY_GET_HOTEL_BY_LOCATION = """
SELECT id_hotel
FROM hotels 
WHERE location = :location
"""

# -----------------------------------------------------QUERYS SERVICES----------------------------------------------------

QUERY_GET_ALL_SERVICES = """
SELECT * FROM services
"""

QUERY_ADD_SERVICE = """
INSERT INTO services (name, description, price) 
VALUES (:name, :description, :price)
"""

QUERY_DELETE_SERVICE = """
DELETE FROM services WHERE id_service = :id_service
"""

QUERY_UPDATE_SERVICE = """
UPDATE services 
SET name = :name, description = :description, price = :price
WHERE id_service = :id_service
"""

def send_query(query: str, params: dict = None):
    """
    Ejecuta una consulta SQL en la base de datos y devuelve el resultado.

    :param query: Consulta SQL a ejecutar (debe ser una cadena de texto).
    :param params: Diccionario opcional con los parámetros de la consulta (por defecto es None).
    :return: Tupla (result, success) donde:
            result: El resultado de la consulta (si tiene éxito) o None (si hubo un error).
            success: Un valor booleano indicando si la operación fue exitosa.
    """
    try:
        with engine.connect() as conn:
            with conn.begin():
                result = conn.execute(text(query), params or {})
                if result.rowcount > 0:
                    return result, True
                else:
                    return None, False
    except SQLAlchemyError as err:
        print(f"Error al ejecutar la consulta: {err}")
        return None, False



def get_user(id_user: int):
    """
    Obtiene los detalles de un usuario mediante su ID.

    :param id_user: El ID del usuario cuyo detalle se desea obtener.
    :return: Un diccionario con el estado de la operación y los detalles del usuario si se encuentra, o un mensaje de error si no.
    """
    params = {"id_user": id_user}
    result, success = send_query(QUERY_GET_USER, params)
    if not success or result is None:
        return {"status": "error", "message": "No se pudo obtener el usuario"}
    
    for row in result:
        user = {
            "id_user": row[0],
            "name": row[1],
            "lastname": row[2],
            "email": row[3],
            "dni": row[5],
            "phone": row[6], 
            "created_at": row[7]
        }
    return {"status": "success", "data": user}


def get_all_users():
    """
    Obtiene todos los usuarios registrados en la base de datos.

    :return: Un diccionario con el estado de la operación y la lista de todos los usuarios, o un mensaje de error si no se pueden obtener.
    """
    result, success = send_query(QUERY_GET_ALL_USERS)
    if not success or result is None:
        return {"status": "error", "message": "No se pudo obtener los usuarios"}
    
    users = []
  
    for row in result:
        user = {
            "id_user": row[0],
            "name": row[1],
            "lastname": row[2],
            "email": row[3],
            "dni": row[5],
            "phone": row[6],
            "created_at": row[7]
        }
        users.append(user)
    
    return {"status": "success", "data": users}



def delete_user(id_user):
    """
    Elimina un usuario de la base de datos mediante su ID.

    :param id_user: El ID del usuario que se desea eliminar.
    :return: Un diccionario con el estado de la operación.
    """
    params = {"id_user": id_user}
    result, success = send_query(QUERY_DELETE_USER, params)
    if success:
        return {"status": "success", "message": f"Usuario {id_user} eliminado correctamente"}
    else:
        return {"status": "error", "message": f"No se pudo eliminar el usuario {id_user}"}




def check_user(email: str, dni: int):
    """
    Verifica si un usuario ya está registrado por email o DNI.

    :param email: El email del usuario.
    :param dni: El DNI del usuario.
    :return: Un mensaje de error si ya existe un usuario con estos datos, o None si no.
    """
    params = {"email": email}
    result_email, success_email = send_query(QUERY_CHECK_USER_BY_EMAIL, params)
    if result_email:
        return {"status": "error", "message": "El email ya está registrado"}, True
    
    params = {"dni": dni}
    result_dni, success_dni = send_query(QUERY_CHECK_USER_BY_DNI, params)

    if result_dni:
        return {"status": "error", "message": "El DNI ya está registrado"}, True

    return None, False



def register(email: str, password: str, name: str, lastname: str, dni: int, phone: int):

    params = {
        "name": name,
        "lastname": lastname,
        "email": email,
        "password": password,
        "dni": dni,
        "phone": phone
    }
    
    try:
     
        error_response, user_exists = check_user(email, dni)
        if user_exists:
            return error_response  
        
        result, success = send_query(QUERY_ADD_USER, params)

        if success:
            return {"status": "success", "message": "El usuario se creó correctamente"}
        else:
            return {"status": "error", "message": "No se ha podido crear el usuario"}
        
    except SQLAlchemyError as e:
        print(f"Error en la función de registro: {e}")
        return {"status": "error", "message": "Error en la operación de registro"}
    

def update_user(id_user, name: str, lastname: str, phone: str, dni: int):
    """
    Actualiza los datos de un usuario existente.

    :param id_user: El ID del usuario que se va a actualizar.
    :param name: El nuevo nombre del usuario.
    :param lastname: El nuevo apellido del usuario.
    :param phone: El nuevo teléfono del usuario.
  
    :param dni: El nuevo DNI del usuario.
    :return: Un diccionario con el estado de la operación.
    """
    params = {
        "id_user": id_user,
        "name": name,
        "lastname": lastname,
        "dni": dni,
        "phone": phone
    }
    result, success = send_query(QUERY_UPDATE_USER, params)
    if success:
        return {"status": "success", "message": "Usuario modificado exitosamente"}
    else:
        return {"status": "error", "message": "El usuario no existe"}
    

def get_user_by_email(email):
    """
    Función que obtiene un usuario por su correo electrónico.
    """
    result, success = send_query(QUERY_CHECK_USER_BY_EMAIL, {"email": email})
    
    if success and result:
        return result.fetchone()  # Devuelve el primer resultado encontrado
    return None

def update_user_password(email, new_password):
    """
    Función para actualizar la contraseña de un usuario en la base de datos sin encriptar.
    """
    
    params = {
        "email": email, 
        "password": new_password
        }
    result, success = send_query(QUERY_UPDATE_PASSWORD, params)
    
    return success


def log_in(email: str, password: str):
    params = {"email": email}
    result, success = send_query(QUERY_LOG_IN, params)

    if success and result:
        rows = result.fetchall()
        
        result_list = [dict(zip(result.keys(), row)) for row in rows]
        
        info_user = result_list[0]
        stored_password = info_user.get("password")
        
        if stored_password == password: 
            return {"status": "success", "message": "Inicio de sesión exitoso", "data": info_user}
        else:
            return {"status": "error", "message": "Contraseña incorrecta"}
    else:
        return {"status": "error", "message": "Usuario no encontrado"}
    
    
#--------------------------ROOMS---------------------------------


def get_all_faq():
    """
    Obtiene todos los faqs en la base de datos y los devuelve como un JSON serializable.
    :return: Un diccionario con el estado de la operación y los datos de los FAQs, o un mensaje de error si no se pueden obtener.
    """
    result, success = send_query(QUERY_GET_FAQ)   
    if success:
        rows = result.fetchall()
        faq_list = [dict(zip(result.keys(), row)) for row in rows]
        return {'status': 'success', 'data': faq_list}
    else:
        return {'status': 'error', 'message': 'Error al ejecutar la consulta'}
    
    

def get_all_testimonial():
    """
    Obtiene todos los faqs en la base de datos y los devuelve como un JSON serializable.
    :return: Un diccionario con el estado de la operación y los datos de los FAQs, o un mensaje de error si no se pueden obtener.
    """
    result, success = send_query(QUERY_GET_TESTIMONIAL)
        
    if success:
        rows = result.fetchall()
        testimonial_list = [dict(zip(result.keys(), row)) for row in rows]
        return {'status': 'success', 'data': testimonial_list}
    else:
        return {'status': 'error', 'message': 'Error al ejecutar la consulta'}
    



def get_all_type_rooms():
    """
    Obtiene todas las habitaciones disponibles en el sistema.

    :return: Un diccionario con el estado de la operación y la lista de habitaciones, o un mensaje de error si no se pueden obtener.
    """
    try:
        result, success = send_query(QUERY_GET_ALL_TYPE_ROOMS)
        if success:
            rows = result.fetchall()
        
            type_rooms_list = [dict(zip(result.keys(), row)) for row in rows]
            return {"status": "success", "data": type_rooms_list}
        else:
             return {'status': 'error', 'message': "No se pudo obtener los datos de type_rooms"}
    except SQLAlchemyError as e:
        return {'status': 'error', 'message': str(e.__dict__.get('orig'))}
    
def get_all_hotels():
    """
    Obtiene todas las habitaciones disponibles en el sistema.

    :return: Un diccionario con el estado de la operación y la lista de habitaciones, o un mensaje de error si no se pueden obtener.
    """
    try:
        result, success = send_query(QUERY_GET_ALL_HOTELS)
        if success:
            rows = result.fetchall()
        
            hotels_list = [dict(zip(result.keys(), row)) for row in rows]
            return {"status": "success", "data": hotels_list}
        else:
             return {'status': 'error', 'message': "No se pudo obtener los datos de hotels"}
    except SQLAlchemyError as e:
        return {'status': 'error', 'message': str(e.__dict__.get('orig'))}
        
        

    
def get_room(id_room):
    """
    Obtiene los detalles de una habitación específica.

    :param id_room: El ID de la habitación que se desea obtener.
    :return: Un diccionario con el estado de la operación y los detalles de la habitación, o un mensaje de error si no se puede obtener.
    """
    params = {"id_room": id_room}
    result, success = send_query(QUERY_GET_ROOM, params)
    if not success or result is None:
        return {"status": "error", "message": "No se pudo obtener la habitación"}
    
    for row in result:
        room = {
            "id_room": row[0],
            "id_hotel": row[1],
            "type_room": row[2],
            "title": row[3],
            "description": row[4],
            "image": row[5],
            "price": row[8]
        }
    
    return {"status": "success", "data": room}

def  get_user_id_by_email_and_dni(email, dni):
    """
    Obtiene el id de un usuario segun mail y dni

    :param id_room: El ID de la habitación que se desea obtener.
    :return: Un diccionario con el estado de la operación y los detalles de la habitación, o un mensaje de error si no se puede obtener.
    """
    params = {"email": email, "dni": dni}
    result, success = send_query(QUERY_GET_ID_BY_EMAIL_AND_DNI, params)
    if not success or result is None:
        return {"status": "error", "message": "No se pudo obtener el id"}
    
    row = result.fetchone()
    if row:
        id_user = row[0]
    
    return {"status": "success", "data": id_user}

def delete_room(id_room):
    """
    Elimina una habitación del sistema.

    :param id_room: El ID de la habitación que se desea eliminar.
    :return: Un diccionario con el estado de la operación.
    """
    params = {"id_room": id_room}
    result, success = send_query(QUERY_DELETE_ROOM, params)
    if success:
        return {"status": "success", "message": f"Habitación {id_room} eliminada correctamente"}
    else:
        return {"status": "error", "message": f"No se pudo eliminar la habitación {id_room}"}


def update_room(id_room, id_hotel: str, type_room: str, title: str, description: str, image: str, price: int):
    """
    Actualiza los detalles de una habitación existente.

    :param id_room: El ID de la habitación que se va a actualizar.
    :param id_hotel: El ID del hotel al que pertenece la habitación.
    :param type_room: El número de la habitación.
    :param title: El título de la habitación.
    :param description: La descripción de la habitación.
    :param image: La imagen de la habitación.
    :param price: El precio de la habitación.
    :return: Un diccionario con el estado de la operación.
    """
    params = {
        "id_room": id_room,
        "id_hotel": id_hotel,
        "type_room": type_room,
        "title": title,
        "description": description,
        "image": image,
        "price": price
    }
    result, success = send_query(QUERY_UPDATE_ROOM, params)
    if success:
        return {"status": "success", "message": "Habitación modificada exitosamente"}
    else:
        return {"status": "error", "message": "La habitación no existe"}


def check_room(id_hotel: int, type_room: int, title: str, description: str, image: str, max_guests: int, price: float):
    """
    Verifica si una habitación ya existe en la base de datos por los parámetros dados.

    :param id_hotel: El ID del hotel donde se encuentra la habitación.
    :param type_room: El número de la habitación.
    :param title: El título de la habitación.
    :param description: La descripción de la habitación.
    :param image: La imagen de la habitación.
    :param price: El precio de la habitación.
    :return: Un mensaje de error si ya existe una habitación con esos datos, o None si no existe.
    """
    params = {
        "id_hotel": id_hotel,
        "type_room": type_room,
        "title": title,
        "description": description,
        "image": image,
        "price": price
    }
    result, success = send_query(QUERY_CHECK_ROOM_DUPLICATED, params)
    if result:
        return {"status": "error", "message": "La habitación ya existe"}, True
    
    return None, False

    
def create_room(id_hotel: int, type_room: int, title: str, description: str, image: str, status: str, max_guests: int, price: float):
    """
    Crea una nueva habitación en la base de datos, verificando que no se repita.

    :param id_hotel: El ID del hotel donde se agregará la habitación.
    :param type_room: El número de la habitación.
    :param title: El título de la habitación.
    :param description: La descripción de la habitación.
    :param image: La imagen de la habitación.
    :param price: El precio de la habitación.
    :return: Un diccionario con el estado de la operación.
    """
    result, success = check_room(id_hotel, type_room, title, description, image, max_guests, price)
    if success:
        return result
    else:
        params = {
            "id_hotel": id_hotel,
            "type_room": type_room,
            "title": title,
            "description": description,
            "image": image,
            "price": price
        }
        result, success = send_query(QUERY_ADD_ROOM, params)
        if success:
            return {"status": "success", "message": "Habitación agregada exitosamente"}
        else:
            return {"status": "error", "message": "Hubo un error al agregar la habitación"}


def get_rooms_by_hotel(id_hotel):
    """
    Devuelve una lista de habitaciones asociadas a un hotel específico.

    :param id_hotel: ID del hotel a buscar.
    :return: Diccionario con el estado de la consulta y los datos o un mensaje de error.
    """
    params = {"id_hotel": id_hotel}
    result, success = send_query(QUERY_GET_ROOMS_BY_HOTEL, params)
    if not success or not result:
        return {"status": "error", "message": f"No se encontraron habitaciones para el hotel con ID {id_hotel}"}
    rooms = []
    for row in result:
        room = {
            "id_room": row[0],
            "type_room": row[1],
        }
        rooms.append(room)

    return {"status": "success", "data": rooms}

def check_room_availability(type_room, id_hotel, check_in):
    params = {
        'type_room': type_room,
        'id_hotel': id_hotel,
        'check_in': check_in
    }
    result, success = send_query(QUERY_ROOMS_DISPONIBILITY, params)
    if success:
        if result:  
            room = result.fetchone()  
            if room:  
                return {"status": "success", "message": f"Habitación disponible encontrada: ID {room[0]}", "data": room[0]}
            else:
                return {"status": "error", "message": "No se encontraron habitaciones disponibles con los criterios dados."}
        else:
            return {"status": "error", "message": "La consulta no devolvió resultados."}
    else:
        return {"status": "error", "message": "Error al ejecutar la consulta."}

#------------------------------------------------------RESERVATIONS------------------------------------------------------------
        
def get_all_reservations():
    """
    Devuelve una lista con todas las reservas en la base de datos.

    :return: Diccionario con el estado de la consulta y los datos o un mensaje de error.
    """
    result, success = send_query(QUERY_GET_ALL_RESERVATIONS)

    if not success or result is None:
        return {"status": "error", "message": "No se pudo obtener las reservas"}

    reservations = {}
    for row in result:
        id_reservation = row[0]
        reservations[id_reservation] = {
            "id_user": row[1],
            "id_room": row[2],
            "id_hotel": row[3],
            "type_room": row[4],
            "number_people": row[5],
            "check_in": row[6],
            "check_out": row[7]
        }
    return {"status": "success", "data": reservations}

def get_reservation(id_reservation):
    """
    Devuelve la reserva asociada a un usuario específico.

    :param id_user: ID del usuario para buscar la reserva.
    :return: Diccionario con el estado de la consulta y los datos o un mensaje de error.
    """
    params = {"id_reservation": id_reservation}
    result, success = send_query(QUERY_GET_RESERVATION, params)

    if not success or result is None:
        return {"status": "error", "message": "No se pudo obtener la reserva"}

    reservation = None
    for row in result:
        reservation = {
            "id_reservation": row[0],
            "id_user": row[1],
            "id_room": row[2],
            "id_hotel": row[3],
            "number_people": row[4],
            "check_in": row[5],
            "check_out": row[6]
        }

    if reservation:
        return {"status": "success", "data": reservation}
    else:
        return {"status": "error", "message": "No se encontró reserva para el usuario"}

def get_reservation_by_id_and_lastname(id_reservation, lastname):
    """
    Devuelve la reserva asociada a un código de reserva y apellido.

    :param id_reservation: Código de reserva para buscar la reserva.
    :param lastname: Apellido del usuario para buscar la reserva.
    :return: Diccionario con el estado de la consulta y los datos o un mensaje de error.
    """
    params = {"id_reservation": id_reservation, "lastname": lastname}
    reservation, success = send_query(QUERY_GET_RESERVATION_BY_ID_AND_LASTNAME, params)
    print(reservation, success)

    if not success or reservation is None:
        return {"status": "error", "message": "No se pudo obtener la reserva"}

    reservation_details = [{
        "id_reservation": detail.id_reservation,
        "id_user": detail.id_user,
        "id_room": detail.id_room,
        "number_people": detail.number_people,
        "check_in": detail.check_in,
        "check_out": detail.check_out,
        "dni": detail.dni,
        "email": detail.email,
        "name": detail.name,
        "lastname": detail.lastname,
        "phone": detail.phone,
        "location": detail.location,
        "description": detail.description
    } for detail in reservation]

    return {"status": "success", "data": reservation_details[0]}

def delete_reservation(id_user):
    """
    Elimina la reserva de un usuario específico.

    :param id_user: ID del usuario cuya reserva se quiere eliminar.
    :return: Diccionario con el estado de la operación.
    """
    params = {"id_user": id_user}
    result, success = send_query(QUERY_DELETE_RESERVATION, params)

    if success:
        return {"status": "success", "message": f"Reserva del usuario con ID {id_user} eliminada correctamente"}
    else:
        return {"status": "error", "message": f"No se pudo eliminar la reserva del usuario con ID {id_user}"}


def add_reservation(id_user, id_room, id_hotel, number_people, check_in, check_out):
    """
    Agrega una nueva reserva a la base de datos.

    :param id_user: ID del usuario que realiza la reserva.
    :param id_room: ID de la habitación reservada.
    :param id_hotel: ID del hotel donde se hace la reserva.
    :param type_room: Número de la habitación reservada.
    :param check_in: Fecha y hora de check-in.
    :param check_out: Fecha y hora de check-out.
    :return: Diccionario con el estado de la operación.
    """
    params = {
        "id_user": id_user,
        "id_room": id_room,
        "id_hotel": id_hotel,
        "number_people": number_people,
        "check_in": check_in,
        "check_out": check_out,
    }
    result, success = send_query(QUERY_ADD_RESERVATION, params)

    if success:
        id_reservation_result, success = send_query(QUERY_FIND_ID_RESERVATION, params)

        if id_reservation_result and id_reservation_result.rowcount > 0:
            row = id_reservation_result.fetchone()
            columns = id_reservation_result.keys() 
            id_reservation_dict = dict(zip(columns, row))
            id_reservation = id_reservation_dict.get('id_reservation')
            return {"status": "success", "message": "Reserva agregada exitosamente", "id_reservation": id_reservation}
    else:
        return {"status": "error", "message": "No se pudo agregar la reserva"}
    
def get_reservations_by_hotel(id_hotel):
    """
    Obtiene todas las reservas de un hotel específico.

    :param id_hotel: ID del hotel para obtener sus reservas.
    :return: Diccionario con el estado de la operación y los datos de las reservas.
    """
    params = {"id_hotel": id_hotel}
    result, success = send_query(QUERY_GET_RESERVATIONS_BY_HOTEL, params)
    
    if not success or not result:
        return {"status": "error", "message": "No se encontraron reservas para este hotel"}

    reservations = []
    for row in result:
        reservation = {
            "id_user": row[0],
            "id_room": row[1],
            "id_hotel": row[2],
            "type_room": row[3],
            "check_in": row[4],
            "check_out": row[5],
        }
        reservations.append(reservation)
    
    return {"status": "success", "data": reservations}

def get_reservation_by_user(id_user):
    """
    Obtiene las reservas de un usuario específico.

    :param id_user: ID del usuario cuya reserva se desea obtener.
    :return: Diccionario con el estado de la operación y las reservas del usuario.
    """
    params = {"id_user": id_user}
    result, success = send_query(QUERY_GET_RESERVATION_BY_USER, params)

    if not success or not result:
        return {"status": "error", "message": f"No se encontraron reservas para el usuario con ID {id_user}"}

    reservations = []
    for row in result:
        reservation = {
            "id_user": row[0],
            "id_room": row[1],
            "id_hotel": row[2],
            "type_room": row[3],
            "check_in": row[4],
            "check_out": row[5],
        }
        reservations.append(reservation)

    return {"status": "success", "data": reservations}


def get_active_reservations():
    """
    Obtiene todas las reservas activas (en curso) de la base de datos.

    :return: Diccionario con el estado de la operación y los datos de las reservas activas.
    """
    result, success = send_query(QUERY_GET_ACTIVE_RESERVATIONS)
    
    if not success or not result:
        return {"status": "error", "message": "No se encontraron reservas activas"}

    reservations = []
    for row in result:
        reservation = {
            "id_user": row[0],
            "id_room": row[1],
            "id_hotel": row[2],
            "type_room": row[3],
            "check_in": row[4],
            "check_out": row[5],
        }
        reservations.append(reservation)
    
    return {"status": "success", "data": reservations}

def delete_reservation(id_user):
    """
    Elimina la reserva de un usuario específico.

    :param id_user: ID del usuario cuya reserva se quiere eliminar.
    :return: Diccionario con el estado de la operación.
    """
    params = {"id_user": id_user}
    result, success = send_query(QUERY_DELETE_RESERVATION, params)

    if success:
        return {"status": "success", "message": f"Reserva del usuario con ID {id_user} eliminada correctamente"}
    else:
        return {"status": "error", "message": f"No se pudo eliminar la reserva del usuario con ID {id_user}"}

def get_services_by_reservation(id_reservation):
    """
    Devuelve un diccionario con los servicios contratados y disponibles para una reserva específica.

    :param id_reservation: ID de la reserva.
    :return: Diccionario con los servicios contratados y disponibles.
    """
    params = {"id_reservation": id_reservation}
    contracted_services, success_contracted = send_query(QUERY_GET_SERVICES_BY_RESERVATION, params)

    if not success_contracted or contracted_services is None:
        return {"status": "error", "message": "No se pudo obtener los servicios contratados"}

    all_services, success_all = send_query(QUERY_GET_ALL_SERVICES)

    if not success_all or all_services is None:
        return {"status": "error", "message": "No se pudo obtener todos los servicios disponibles"}

    contracted_services_list = [
        {"id_service": row[0], "name": row[1], "description": row[2], "price": row[3]}
        for row in contracted_services
        if row[0] is not None
    ]

    all_services_list = [
        {"id_service": row[0], "name": row[1], "description": row[2], "price": row[3]}
        for row in all_services
    ]

    contracted_ids = {service["id_service"] for service in contracted_services_list}

    available_services_list = [service for service in all_services_list if service["id_service"] not in contracted_ids]

    return {
        "status": "success",
        "data": {
            "contracted_services": contracted_services_list,
            "available_services": available_services_list
        }
    }

def update_services_by_reservation(id_reservation, new_services):
    """
    Función para actualizar los servicios contratados de una reserva.

    :param id_reservation: ID de la reserva.
    :param new_services: Lista de IDs de los nuevos servicios a contratar.
    :return: Diccionario con el estado de la operación.
    """
    print(id_reservation, new_services)
    params = {"id_reservation": id_reservation}
    existing_services, check_success = send_query(QUERY_CHECK_EXISTENT_SERVICES_BY_RESERVATION, params)

    if check_success and existing_services.fetchone()[0] != 0:
        delete_query = "DELETE FROM reservation_services WHERE id_reservation = :id_reservation"
        delete_result, delete_success = send_query(delete_query, {"id_reservation": id_reservation})
        if not delete_success:
            return {"status": "error", "message": "No se pudieron eliminar los servicios existentes"}

    for service_id in new_services:
        insert_params = {"id_reservation": id_reservation, "id_service": service_id}
        insert_result, insert_success = send_query(QUERY_UPDATE_SERVICE_BY_RESERVATION, insert_params)
        if not insert_success:
            return {"status": "error", "message": f"No se pudo agregar el servicio con ID {service_id}"}

    return {"status": "success", "message": "Servicios contratados actualizados correctamente"}

def delete_service_from_reservation(id_reservation, id_service):
    """
    Función para eliminar un servicio específico asociado a una reserva.

    :param id_reservation: ID de la reserva.
    :param id_service: ID del servicio a eliminar.
    :return: Diccionario con el estado de la operación.
    """
    params = {"id_reservation": id_reservation, "id_service": id_service}
    result, success = send_query(QUERY_DELETE_SERVICE_FROM_RESERVATION, params)
    if success:
        return {"status": "success", "message": f"Servicio con ID {id_service} eliminado de la reserva {id_reservation}"}
    else:
        return {"status": "error", "message": f"No se pudo eliminar el servicio con ID {id_service} de la reserva {id_reservation}"}

#-------------------------------------------------HOTEL------------------------------------------------
    
def add_hotel(title, description, image, cant_rooms):
    params = {
        "title": title,
        "description": description,
        "image": image,
        "cant_rooms": cant_rooms
    }
    result, success = send_query(QUERY_ADD_HOTEL, params)
    if success:
        return {"status": "success", "message": "Hotel agregado exitosamente"}
    else:
        return {"status": "error", "message": "No se pudo agregar el hotel"}

def delete_hotel(id_hotel):
    """
    Elimina un hotel específico de la base de datos.

    :param id_hotel: ID del hotel que se desea eliminar.
    :return: Diccionario con el estado de la operación.
    """
    params = {"id_hotel": id_hotel}
    result, success = send_query(QUERY_DELETE_HOTEL, params)

    if success:
        return {"status": "success", "message": f"Hotel con ID {id_hotel} eliminado correctamente"}
    else:
        return {"status": "error", "message": f"No se pudo eliminar el hotel con ID {id_hotel}"}

def update_hotel(id_hotel, title, description, image, cant_rooms):
    """
    Actualiza la información de un hotel específico en la base de datos.

    :param id_hotel: ID del hotel que se desea actualizar.
    :param title: Nuevo título para el hotel.
    :param description: Nueva descripción para el hotel.
    :param image: Nueva imagen para el hotel.
    :param cant_rooms: Nueva cantidad de habitaciones para el hotel.
    :return: Diccionario con el estado de la operación.
    """
    params = {
        "id_hotel": id_hotel,
        "title": title,
        "description": description,
        "image": image,
        "cant_rooms": cant_rooms,
    }
    result, success = send_query(QUERY_UPDATE_HOTEL, params)

    if success:
        return {"status": "success", "message": f"Hotel con ID {id_hotel} actualizado correctamente"}
    else:
        return {"status": "error", "message": f"No se pudo actualizar el hotel con ID {id_hotel}"}

def get_hotel_by_id(id_hotel):
    """
    Obtiene la ubicación (location) de un hotel mediante su ID.

    :param id_hotel: El ID del hotel cuyo detalle se desea obtener.
    :return: Un diccionario con el estado de la operación y los detalles del hotel si se encuentra, o un mensaje de error si no.
    """
    try:
        params = {"id_hotel": id_hotel}
        result, success = send_query(QUERY_GET_HOTEL_BY_ID, params)
        
        if not success or result is None:
            return {"status": "error", "message": f"Hotel con ID {id_hotel} no encontrado"}
        
        row = result.mappings().fetchone()
        
        if row is None:
            return {"status": "error", "message": f"Hotel con ID {id_hotel} no encontrado"}

        return {"status": "success", "data": {"location": row["location"]}}

    except Exception as e:
        return {"status": "error", "message": f"Error interno: {str(e)}"}

def get_hotel_by_location(location):
    """
    Obtiene la ubicación el id de un hotel mediante su ubicacion.

    :param id_hotel: El ID del hotel cuyo detalle se desea obtener.
    :return: Un diccionario con el estado de la operación y los detalles del hotel si se encuentra, o un mensaje de error si no.
    """
    try:
        params = {"location": location}
        result, success = send_query(QUERY_GET_HOTEL_BY_LOCATION, params)
        
        if not success or result is None:
            return {"status": "error", "message": f"Hotel  no encontrado"}
        
        row = result.mappings().fetchone()
        
        if row is None:
            return {"status": "error", "message": f"Hotel no encontrado"}

        return {"status": "success", "data": {"data": row["id_hotel"]}}

    except Exception as e:
        return {"status": "error", "message": f"Error interno: {str(e)}"}
    
#------------------------------------------------------SERVICES------------------------------------------------------------
        
def get_all_services():
    """
    Devuelve una lista con todos los servicios en la base de datos.

    :return: Diccionario con el estado de la consulta y los datos o un mensaje de error.
    """
    services, success = send_query(QUERY_GET_ALL_SERVICES)

    if not success or services is None:
        return {"status": "error", "message": "No se pudo obtener los servicios"}
    
    services_list = [{"id_service": service.id_service, "name": service.name, "description": service.description, "price": service.price} for service in services]
    return {"status": "success", "data": services_list}

def add_service(name, description, price):
    """
    Función para agregar un nuevo servicio al sistema.

    :param name: Nombre del servicio.
    :param description: Descripción del servicio.
    :param price: Precio del servicio.
    :return: Diccionario con el estado de la operación.
    """
    params = {"name": name, "description": description, "price": price}
    result, success = send_query(QUERY_ADD_SERVICE, params)
    if success:
        return {"status": "success", "message": "Servicio agregado exitosamente"}
    else:
        return {"status": "error", "message": "No se pudo agregar el servicio"}


def delete_service(id_service):
    """
    Función para eliminar un servicio del sistema.

    :param id_service: ID del servicio a eliminar.
    :return: Diccionario con el estado de la operación.
    """
    params = {"id_service": id_service}
    result, success = send_query(QUERY_DELETE_SERVICE, params)
    if success:
        return {"status": "success", "message": f"Servicio con ID {id_service} eliminado correctamente"}
    else:
        return {"status": "error", "message": f"No se pudo eliminar el servicio con ID {id_service}"}

def update_service(id_service, name, description, price):
    """
    Función para actualizar los detalles de un servicio.

    :param id_service: ID del servicio a actualizar.
    :param name: Nuevo nombre del servicio.
    :param description: Nueva descripción del servicio.
    :param price: Nuevo precio del servicio.
    :return: Diccionario con el estado de la operación.
    """
    params = {
        "id_service": id_service,
        "name": name,
        "description": description,
        "price": price
    }
    result, success = send_query(QUERY_UPDATE_SERVICE, params)
    if success:
        return {"status": "success", "message": f"Servicio con ID {id_service} actualizado correctamente"}
    else:
        return {"status": "error", "message": f"No se pudo actualizar el servicio con ID {id_service}"}