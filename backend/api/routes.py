from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from models import db, User, Contact, Hotel, Room
from api import home


@home.errorhandler(404)
def endp_not_found(e):
    return 0


@home.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if user and user.verify_password(password):
        return jsonify({"message": "Login successful", "user_id": user.id}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401


@home.route("/users", methods=["GET"])
def get_users():
    id = request.args.get("id")
    try:
        if id:
            user = User.query.get(id)
            if not user:
                return jsonify({"error": "User not found"}), 404
            return jsonify(
                {
                    "id": user.id,
                    "name": user.name,
                    "lastname": user.lastname,
                    "email": user.email,
                    "phone": user.phone,
                    "created_at": user.created_at,
                }
            )
        else:
            users = User.query.all()
            return jsonify(
                [
                    {
                        "id": user.id,
                        "name": user.name,
                        "lastname": user.lastname,
                        "email": user.email,
                        "phone": user.phone,
                        "created_at": user.created_at,
                    }
                    for user in users
                ]
            )
    except SQLAlchemyError as err:
        return jsonify({"error": str(err)}), 500


@home.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    try:
        new_user = User(
            name=data["name"],
            lastname=data["lastname"],
            email=data["email"],
            phone=data["phone"],
            password=data["password"],
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 201
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/users", methods=["PUT"])
def update_user():
    data = request.get_json()
    try:
        user = User.query.get(data["id"])
        if not user:
            return jsonify({"error": "User not found"}), 404

        user.name = data.get("name", user.name)
        user.lastname = data.get("lastname", user.lastname)
        user.email = data.get("email", user.email)
        user.phone = data.get("phone", user.phone)

        if "password" in data and data["password"]:
            user.password = data["password"]

        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/users", methods=["DELETE"])
def delete_user():
    id = request.args.get("id")
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/contacts", methods=["GET"])
def get_contacts():
    try:
        contacts = Contact.query.all()
        contact_list = [
            {
                "id": contact.id_contact,
                "name": contact.name,
                "lastname": contact.lastname,
                "email": contact.email,
                "topic": contact.topic,
                "message": contact.message,
                "status": contact.status,
                "created_at": contact.created_at,
            }
            for contact in contacts
        ]

        return jsonify(contact_list), 200
    except SQLAlchemyError as err:
        return jsonify({"error": str(err)}), 500


@home.route("/contacts", methods=["POST"])
def add_contact():
    data = request.get_json()
    try:
        new_contact = Contact(
            name=data["name"],
            lastname=data["lastname"],
            email=data["email"],
            topic=data["topic"],
            message=data["message"],
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"message": "Contact added successfully"}), 201
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/contacts", methods=["PUT"])
def update_contact():
    data = request.get_json()
    try:
        contact = Contact.query.get(data["id"])
        if not contact:
            return jsonify({"error": "Contact not found"}), 404

        contact.name = data.get("name", contact.name)
        contact.lastname = data.get("lastname", contact.lastname)
        contact.email = data.get("email", contact.email)
        contact.topic = data.get("topic", contact.topic)
        contact.message = data.get("message", contact.message)
        contact.status = data.get("status", contact.status)

        db.session.commit()
        return jsonify({"message": "Contact updated successfully"}), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/contacts", methods=["DELETE"])
def delete_contact():
    id = request.args.get("id")
    try:
        contact = Contact.query.get(id)
        if not contact:
            return jsonify({"error": "Contact not found"}), 404

        db.session.delete(contact)
        db.session.commit()
        return jsonify({"message": "Contact deleted successfully"}), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/hotels", methods=["GET"])
def get_hotels():
    try:
        hotels = Hotel.query.all()
        hotel_list = [
            {
                "id_hotel": hotel.id_hotel,
                "name": hotel.name,
                "description": hotel.description,
                "image": hotel.image,
                "cant_rooms": hotel.cant_rooms,
                "location": hotel.location,
                "rating": hotel.rating,
                "amenities": hotel.amenities,
                "contact_info": hotel.contact_info,
                "created_at": hotel.created_at,
            }
            for hotel in hotels
        ]

        return jsonify(hotel_list), 200
    except SQLAlchemyError as err:
        return jsonify({"error": str(err)}), 500


@home.route("/hotels", methods=["POST"])
def add_hotel():
    data = request.get_json()
    try:
        new_hotel = Hotel(
            name=data["name"],
            description=data["description"],
            image=data["image"],
            cant_rooms=data["cant_rooms"],
            location=data["location"],
            rating=data["rating"],
            amenities=data.get("amenities", ""),
            contact_info=data.get("contact_info", ""),
        )
        db.session.add(new_hotel)
        db.session.commit()
        return jsonify({"message": "Hotel added successfully"}), 201
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/hotels", methods=["PUT"])
def update_hotel():
    data = request.get_json()
    try:
        hotel = Hotel.query.get(data["id"])
        if not hotel:
            return jsonify({"error": "Hotel not found"}), 404

        hotel.name = data.get("name", hotel.name)
        hotel.description = data.get("description", hotel.description)
        hotel.image = data.get("image", hotel.image)
        hotel.cant_rooms = data.get("cant_rooms", hotel.cant_rooms)
        hotel.location = data.get("location", hotel.location)
        hotel.rating = data.get("rating", hotel.rating)
        hotel.amenities = data.get("amenities", hotel.amenities)
        hotel.contact_info = data.get("contact_info", hotel.contact_info)

        db.session.commit()
        return jsonify({"message": "Hotel updated successfully"}), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/hotels", methods=["DELETE"])
def delete_hotel():
    id = request.args.get("id")
    try:
        hotel = Hotel.query.get(id)
        if not hotel:
            return jsonify({"error": "Hotel not found"}), 404

        db.session.delete(hotel)
        db.session.commit()
        return jsonify({"message": "Hotel deleted successfully"}), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/rooms", methods=["GET"])
def get_rooms():
    id = request.args.get("id")
    try:
        if id:
            room = Room.query.get(id)
            if not room:
                return jsonify({"error": "Room not found"}), 404
            return jsonify(
                {
                    "id": room.id,
                    "room_number": room.room_number,
                    "room_type": room.room_type,
                    "price": room.price,
                    "available": room.available,
                    "created_at": room.created_at,
                }
            ), 200
        else:
            rooms = Room.query.all()
            room_list = [
                {
                    "id": room.id,
                    "room_number": room.room_number,
                    "room_type": room.room_type,
                    "price": room.price,
                    "available": room.available,
                    "created_at": room.created_at,
                }
                for room in rooms
            ]
            return jsonify(room_list), 200
    except SQLAlchemyError as err:
        return jsonify({"error": str(err)}), 500


@home.route("/rooms", methods=["POST"])
def add_room():
    data = request.get_json()
    try:
        new_room = Room(
            room_number=data["room_number"],
            room_type=data["room_type"],
            price=data["price"],
            available=data["available"],
        )
        db.session.add(new_room)
        db.session.commit()
        return jsonify({"message": "Room added successfully"}), 201
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/rooms", methods=["PUT"])
def update_room():
    data = request.get_json()
    try:
        room = Room.query.get(data["id"])
        if not room:
            return jsonify({"error": "Room not found"}), 404

        room.room_number = data.get("room_number", room.room_number)
        room.room_type = data.get("room_type", room.room_type)
        room.price = data.get("price", room.price)
        room.available = data.get("available", room.available)

        db.session.commit()
        return jsonify({"message": "Room updated successfully"}), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/rooms", methods=["DELETE"])
def delete_room():
    id = request.args.get("id")
    try:
        room = Room.query.get(id)
        if not room:
            return jsonify({"error": "Room not found"}), 404

        db.session.delete(room)
        db.session.commit()
        return jsonify({"message": "Room deleted successfully"}), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({"error": str(err)}), 500


@home.route("/reservation", methods=["POST"])
def create_reservation():
    return 0


@home.route("/reservation", methods=["PUT"])
def update_reservation():
    return 0


@home.route("/reservation", methods=["DELETE"])
def delete_reservation():
    return 0


@home.route("/reservation", methods=["GET"])
def get_reservations():
    return 0
