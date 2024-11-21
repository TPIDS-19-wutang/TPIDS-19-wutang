from flask import Flask, request, jsonify
from sql import *
from datetime import datetime

app = Flask(__name__)

#rutas de habitaciones

@app.route('/rooms/<int:id_hotel>', methods=['GET'])
def get_rooms(id_hotel):
    result = get_rooms_by_hotel(id_hotel)
    return jsonify(result)

@app.route('/room', methods=['POST'])
def create_room():
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

@app.route('/room/<int:id_room>', methods=['PUT'])
def update_room_status(id_room):
    data = request.get_json()
    result = update_room_status(id_room, data['new_status'])
    return jsonify(result)

#rutas de reservas

@app.route('/reservations', methods=['GET'])
def get_all_reservations():
    result = get_all_reservation()
    return jsonify(result)

@app.route('/reservation/<int:id_user>', methods=['GET'])
def get_user_reservation(id_user):
    result = get_reservation(id_user)
    return jsonify(result)

@app.route('/reservation', methods=['POST'])
def add_reservation():
    data = request.get_json()
    result = add_reservation(
        id_user=data['id_user'],
        id_room=data['id_room'],
        id_hotel=data['id_hotel'],
        type_room=data['type_room'],
        check_in=data['check_in'],
        check_out=data['check_out']
    )
    return jsonify(result)

@app.route('/reservation/<int:id_user>', methods=['DELETE'])
def delete_reservation(id_user):
    result = delete_reservation(id_user)
    return jsonify(result)

@app.route('/reservations/hotel/<int:id_hotel>', methods=['GET'])
def get_reservations_by_hotel(id_hotel):
    result = get_reservations_by_hotel(id_hotel)
    return jsonify(result)

@app.route('/reservations/user/<int:id_user>', methods=['GET'])
def get_reservations_by_user(id_user):
    result = get_reservation_by_user(id_user)
    return jsonify(result)

@app.route('/reservations/active', methods=['GET'])
def get_active_reservations():
    result = get_active_reservations()
    return jsonify(result)


#rutas de hoteles

@app.route('/hotel', methods=['POST'])
def add_hotel_route():
    data = request.get_json()
    result = add_hotel(
        type_room=data['type_room'],
        title=data['title'],
        description=data['description'],
        image=data['image'],
        price=data['price'],
        cant_rooms=data['cant_rooms']
    )
    return jsonify(result)

@app.route('/hotel/<int:id_hotel>', methods=['DELETE'])
def delete_hotel(id_hotel):
    result = delete_hotel(id_hotel)
    return jsonify(result)

@app.route('/hotel/<int:id_hotel>', methods=['PUT'])
def update_hotel(id_hotel):
    data = request.get_json()
    result = update_hotel(
        id_hotel=id_hotel,
        title=data['title'],
        description=data['description'],
        image=data['image'],
        price=data['price'],
        cant_rooms=data['cant_rooms']
    )
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
