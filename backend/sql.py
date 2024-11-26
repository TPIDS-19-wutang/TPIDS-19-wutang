from ast import Try
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from flask import jsonify
import mysql.connector
from mysql.connector import Error




DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST= "localhost"
DB_PORT = "3306"
DB_NAME = "triviumdb"

db_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
try:
    engine = create_engine(db_url)
    with engine.connect() as conn:
        print("Conexión exitosa con SQLAlchemy.")
except Exception as e:
    print(f"Error al conectar con SQLAlchemy: {e}")

# Verificación de conexión usando mysql.connector
try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    if connection.is_connected():
        print("Conexión exitosa con mysql.connector.")
        connection.close()  # Cerrar conexión después de verificar
except Error as e:
    print(f"Error al conectar con mysql.connector: {e}")

# ------------------------------------------------------QUERYS USERS----------------------------------------------------

QUERY_DELETE_USER = """
DELETE FROM users WHERE id_user = :id_user
"""

QUERY_GET_FAQ = """
SELECT * FROM faq
"""

QUERY_GET_USER = """
SELECT id_user, name, lastname, email, phone, dni, created_at 
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

QUERY_GET_ALL_USERS = """
SELECT id_user, name, lastname, email, phone, dni, created_at 
FROM users
"""

QUERY_ADD_USER = """
INSERT INTO users (name, lastname, email, phone, dni) 
VALUES (:name, :lastname, :email, :phone, :dni)
"""

QUERY_UPDATE_USER = """
UPDATE users 
SET name = :name, lastname = :lastname, phone = :phone, dni = :dni 
WHERE id_user = :id_user
"""
QUERY_CHANGE_DISPONIBILITY = """

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

QUERY_UPDATE_ROOM_STATUS = """
UPDATE rooms_disponibility
SET status = :status
WHERE id_room = :id_room
"""

# -----------------------------------------------------QUERYS RESERVATIONS----------------------------------------------------

QUERY_GET_ALL_RESERVATIONS = """
SELECT id_reservation, id_user, id_room, id_hotel, number_people, type_room, check_in, check_out, created_at 
FROM reservations
"""

QUERY_GET_RESERVATION = """
SELECT id_reservation, id_user, id_room, id_hotel, number_people, type_room, check_in, check_out, created_at  
FROM reservations 
WHERE id_user = :id_user
"""

QUERY_DELETE_RESERVATION = "DELETE FROM reservations WHERE id_user = :id_user"

QUERY_CREATE_RESERVATION = """
INSERT INTO reservations (id_user, id_room, id_hotel, number_people, type_room, check_in, check_out) 
VALUES (:id_user, :id_room, :id_hotel, :number_people, :type_room, :check_in, check_out)
"""
QUERY_ADD_RESERVATION = """
INSERT INTO reservations (id_user, id_room, id_hotel, number_people, type_room, check_in, check_out) 
VALUES (:id_user, :id_room, :id_hotel, :number_people, :type_room, :check_in, check_out)
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
            result = conn.execute(text(query), params or {})
            return result, True
    except SQLAlchemyError as err:
        return None, False

def get_user(id_user):
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
            "phone": row[4], 
            "created_at": row[6]
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
            "phone": row[4],
            "created_at": row[6]
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




def check_user(email: str, phone: str, dni: int):
    """
    Verifica si un usuario ya está registrado por email, teléfono o DNI.

    :param email: El email del usuario.
    :param phone: El teléfono del usuario.
    :param dni: El DNI del usuario.
    :return: Un mensaje de error si ya existe un usuario con estos datos, o None si no.
    """
    params = {"email": email}
    result_email, success_email = send_query(QUERY_CHECK_USER_BY_EMAIL, params)
    if result_email:
        return {"status": "error", "message": "El email ya está registrado"}, True

    params = {"phone": phone}
    result_phone, success_phone = send_query(QUERY_CHECK_USER_BY_PHONE, params)
    
    if result_phone:
        return {"status": "error", "message": "El teléfono ya está registrado"}, True
    
    params = {"dni": dni}
    result_dni, success_dni = send_query(QUERY_CHECK_USER_BY_DNI, params)

    if result_dni:
        return {"status": "error", "message": "El DNI ya está registrado"}, True

    return None, False



def add_user(name: str, lastname: str, email: str, phone: str, password: str, dni: int):
    """
    Agrega un nuevo usuario a la base de datos, verificando que no se repitan los datos de email, teléfono o DNI.

    :param name: El nombre del usuario.
    :param lastname: El apellido del usuario.
    :param email: El email del usuario.
    :param dni: El DNI del usuario.
    :param phone: El teléfono del usuario.
    :return: Un diccionario con el estado de la operación.
    """
    result, success = check_user(email, phone, dni)

    if success:
        return result
    else:
        params = {
            "name": name,
            "lastname": lastname,
            "email": email,
            "dni": dni,
            "phone": phone
        }
        result, success = send_query(QUERY_ADD_USER, params)
        if success:
            return {"status": "success", "message": "Usuario agregado exitosamente"}
        else:
            return {"status": "error", "message": "Hubo un error al agregar el usuario"}


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

    
#--------------------------ROOMS---------------------------------


def get_all_faq():
    """
    Obtiene todos los faqs en la base de datos y los devuelve como un JSON serializable.
    :return: Un diccionario con el estado de la operación y los datos de los FAQs, o un mensaje de error si no se pueden obtener.
    """
    try:
        # Ejecutar la consulta
        result, success = send_query(QUERY_GET_FAQ)
        
        if success:
            # Usamos .fetchall() para obtener todas las filas
            rows = result.fetchall()

            # Convertir las filas en una lista de diccionarios usando las claves de las columnas
            faq_list = [dict(zip(result.keys(), row)) for row in rows]

            # Retornar los datos como un JSON
            return {'status': 'success', 'data': faq_list}
        else:
            # Si la consulta no fue exitosa, retornar un mensaje de error
            return {'status': 'error', 'message': 'Error al ejecutar la consulta'}
    
    except SQLAlchemyError as e:
        # Manejar errores relacionados con SQLAlchemy y retornar el error como JSON
        return {'status': 'error', 'message': str(e.__dict__.get('orig'))}
    

def get_all_testimonial():
    """
    Obtiene todos los faqs en la base de datos y los devuelve como un JSON serializable.
    :return: Un diccionario con el estado de la operación y los datos de los FAQs, o un mensaje de error si no se pueden obtener.
    """
    try:
        # Ejecutar la consulta
        result, success = send_query(QUERY_GET_TESTIMONIAL)
        
        if success:
            # Usamos .fetchall() para obtener todas las filas
            rows = result.fetchall()

            # Convertir las filas en una lista de diccionarios usando las claves de las columnas
            testimonial_list = [dict(zip(result.keys(), row)) for row in rows]

            # Retornar los datos como un JSON
            return {'status': 'success', 'data': testimonial_list}
        else:
            # Si la consulta no fue exitosa, retornar un mensaje de error
            return {'status': 'error', 'message': 'Error al ejecutar la consulta'}
    
    except SQLAlchemyError as e:
        # Manejar errores relacionados con SQLAlchemy y retornar el error como JSON
        return {'status': 'error', 'message': str(e.__dict__.get('orig'))}



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

def update_room_status(id_room, status):
    """
    Actualiza el estado de una habitación en la base de datos.

    :param id_room: ID de la habitación cuya disponibilidad se desea actualizar.
    :param status: Nuevo estado para la habitación. Ejemplo: 'disponible', 'ocupada', 'reservada'.
    :return: Diccionario con el estado de la operación.
    """
    
    valid_status = ['disponible', 'ocupada', 'reservada']
    if status not in valid_status:
        return {"status": "error", "message": "Estado no válido. Los estados permitidos son: 'disponible', 'ocupada', 'reservada'."}

    
    params = {
        "id_room": id_room,
        "status": status
    }

    result, success = send_query(QUERY_UPDATE_ROOM_STATUS, params)

    if success:
        return {"status": "success", "message": f"Estado de la habitación con ID {id_room} actualizado correctamente a '{status}'."}
    else:
        return {"status": "error", "message": f"No se pudo actualizar el estado de la habitación con ID {id_room}."}


    

#------------------------------------------------------RESERVATIONS------------------------------------------------------------
        
def get_all_reservation():
    """
    Devuelve una lista con todas las reservas en la base de datos.

    :return: Diccionario con el estado de la consulta y los datos o un mensaje de error.
    """
    result, success = send_query(QUERY_GET_ALL_RESERVATIONS)

    if not success or result is None:
        return {"status": "error", "message": "No se pudo obtener las reservas"}

    reservations = []
    for row in result:
        reservation = {
            "id_user": row[0],
            "id_room": row[1],
            "id_hotel": row[2],
            "type_room": row[3],
            "check_in": row[4],
            "check_out": row[5]
        }
        reservations.append(reservation)

    return {"status": "success", "data": reservations}

def get_reservation(id_user):
    """
    Devuelve la reserva asociada a un usuario específico.

    :param id_user: ID del usuario para buscar la reserva.
    :return: Diccionario con el estado de la consulta y los datos o un mensaje de error.
    """
    params = {"id_user": id_user}
    result, success = send_query(QUERY_GET_RESERVATION, params)

    if not success or result is None:
        return {"status": "error", "message": "No se pudo obtener la reserva"}

    reservation = None
    for row in result:
        reservation = {
            "id_user": row[0],
            "id_room": row[1],
            "id_hotel": row[2],
            "type_room": row[3],
            "check_in": row[4],
            "check_out": row[5]
        }

    if reservation:
        return {"status": "success", "data": reservation}
    else:
        return {"status": "error", "message": "No se encontró reserva para el usuario"}

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


def add_reservation(id_user, id_room, id_hotel, type_room, check_in, check_out):
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
        "type_room": type_room,
        "check_in": check_in,
        "check_out": check_out,
    }
    result, success = send_query(QUERY_ADD_RESERVATION, params)

    if success:
        return {"status": "success", "message": "Reserva agregada exitosamente"}
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
