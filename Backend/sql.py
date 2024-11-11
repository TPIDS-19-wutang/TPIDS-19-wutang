from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError\
from flask import jsonify

engine = create_engine("mysql+mysqlconnector://root:@localhost/hotel")

QUERY_DELETE_USER = "DELETE from `users` WHERE id = :id"

QUERY_GET_USER = "SELECT id, nombre, apellido, email, telefono, auth_level, created_at FROM `users`" + " WHERE id = :id"

QUERY_LOG_IN = "SELECT id, nombre, apellido, email, telefono, auth_level, created_at FROM `users`" + " WHERE email = :email and password = :password"

QUERY_CHECK_USER_BY_EMAIL = "SELECT id FROM `users` WHERE email = :email"

QUERY_CHECK_USER_BY_PHONE = "SELECT id FROM `users` WHERE telefono = :telefono"

QUERY_GET_ALL_USERS = "SELECT id, nombre, apellido, email, telefono, auth_level, created_at FROM `users`"

QUERY_ADD_USER = "INSERT INTO `users` (`id`, `nombre`, `apellido`, `email`, `telefono`, `password`, `auth_level`) VALUES (NULL, :nombre, :apellido, :email, :telefono, :password)"

QUERY_UPDATE_USER = " UPDATE `users` SET `nombre` = :nombre, `apellido` = :apellido, `telefono` = :telefono, `password` = :password WHERE `id` = :id"

def send_query(query: str, params: dict = None):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), params or {})
            success = True
    except SQLAlchemyError as err:
        success = False
        return None, jsonify({'error': str(err)}), 500
    return result, success

def get_user(id) -> dict:

    params = {"id": id}
    result, success = send_query(QUERY_GET_USER, params)
    if not success:
        return {"status": "error", "message": "No se pudo obtener el usuario"}
    for row in result:
        user = {
                "id": row[0],
                "nombre": row[1],
                "apellido": row[2],
                "email": row[3],
                "telefono": row[4], 
                "auth_level": row[5],
                "created_at": row[6]
                }
    return user

def get_all_users() -> list:

    result, success = send_query(QUERY_GET_ALL_USERS)
    if not success:
        return {"status": "error", "message": "No se pudo obtener los usuarios"}
    
    users = []
    for row in result:
        user = {
            "id": row[0],
            "nombre": row[1],
            "apellido": row[2],
            "email": row[3],
            "telefono": row[4],
            "auth_level": row[5],
            "created_at": row[6]
        }
        users.append(user)
    return users

def delete_user(id):
    params = {"id": id}
    result, success = send_query(QUERY_DELETE_USER, params)
    if success:
        return {"status": "success", "message": f"Usuario {id} eliminado correctamente"}
    else:
        return {"status": "error", "message": f"No se pudo eliminar el usuario {id}"}
 

def log_in(email: str, password: str) :
    params = {
            "email": email,
            "password": password 
            }
    success, result = send_query(QUERY_LOG_IN, params)
    if not success:
        return {"message": "El email o la contrasenia son incorrectos"}
    
    return success

def check_user(email: str, telefono: str):
    params = {"email": email}
    result_email, success_email = send_query(QUERY_CHECK_USER_BY_EMAIL, params)
    if result_email:
        return {"message": "El email ya está registrado"}, True

    params = {"telefono": telefono}
    result_phone, success_phone = send_query(QUERY_CHECK_USER_BY_PHONE, params)
    
    
    if result_phone:
        return {"message": "El teléfono ya está registrado"}, True

    return None, False

def add_user(nombre: str, apellido: str, email: str, telefono: str, password: str):

    result, success = check_user(email, telefono)

    if success:
        return result
    else:
        params = {
                "nombre": nombre,
                "apellido": apellido,
                "email": email,
                "telefono": telefono,
                "password": password
                }
        result, success= send_query(QUERY_ADD_USER, params)
        if success:
            return {"message": "Usuario agregado exitosamente"}
        else:
            return {"message": "Hubo un error al agregar el usuario"}

def update_user(id, nombre: str, apellido: str, telefono: str, password: str):
    params = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "password": password
    }
    result, success = send_query(QUERY_UPDATE_USER, params)
    if success:
        return {"message": "Usuario modificado exitosamente"}
    else:
        return {"message": "El usuario no existe"}
    
