from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sql import *

app = Flask(__name__)

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