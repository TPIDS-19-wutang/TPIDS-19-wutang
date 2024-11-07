from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine("mysql+mysqlconnector://root:@localhost/hotel")

app = Flask(__name__)

def send_query(query: str):

    try:
        conn = engine.connect()
        result = conn.execute(text(query))
        conn.commit()
        conn.close()
    except SQLAlchemyError as err:
       
        return jsonify({'error': str(err)}), 500
    return result

def get_users(id = None) -> list :
    
    query = f"SELECT id, nombre, apellido, email, FROM `users`" + (f" WHERE id={id};" if id else ";")
    success, result = send_query(query)
    if not success:
        return False
    users = []
    for row in result:
        user = {"id": row[0], "name": row[1], "surname": row[2], "email": row[3], "auth_level": row[4], "created_at": row[5], "updated_at": row[6]}
        users.append(user)
    return users

def add_user(nombre: str, apellido: str, email: str)  :
    
    query = f"INSERT INTO `users` (`id`, `name`, `surname`, `email`, `password`, `auth_level`) VALUES (NULL, '{nombre}', '{apellido}', '{email}'"
    result = send_query(query)

    return result, 200

@app.errorhandler(404)
def endp_not_found(e):
    return 0

#-------------------POSIBLES ENDPOINTS-------------------------
@app.route('/user', methods=["POST"])
def add_user():
    return 0

@app.route('/user', methods=["PUT"])
def update_user():
    return 0

@app.route('/user', methods=["GET"])
def log_in():
    return 0

@app.route('/rooms', methods=["POST"])
def add_room():
    return 0

@app.route('/rooms', methods=["DELETE"])
def delete_room():
    return 0

@app.route('/rooms', methods=["PUT"])
def update_room():
    return 0

@app.route('/reservation', methods=["POST"])
def create_reservation():
    return 0

@app.route('/reservation', methods=["PUT"])
def update_reservation():
    return 0

@app.route('/reservation', methods=["DELETE"])
def delete_reservation():
    return 0

@app.route('/reservation', methods=["GET"])
def add_user():
    return 0



if __name__ == "__main__":
    app.run("127.0.0.1", port="5000", debug=True)