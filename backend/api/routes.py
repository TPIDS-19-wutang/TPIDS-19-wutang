from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from models import db, User, Contact, Hotel, Room
from .schema import (
    LoginSchema,
    ErrorResponseSchema,
    UserCreateRequestSchema,
    ContactCreateRequestSchema,
    ContactSchema,
    UserSchema,
)
from api import home


def handle_sqlalchemy_error(err):
    return jsonify({"error": str(err)}), 500


@home.route("/healthz", methods=["GET"])
@home.response(200)
def health_check():
    """Verificación de salud para comprobar la disponibilidad del servicio"""
    return "OK", 200


@home.errorhandler(404)
def endp_not_found(e):
    return 0


@home.route("/login", methods=["POST"])
@home.arguments(LoginSchema)
@home.response(200, UserSchema)
@home.response(401, ErrorResponseSchema)
def login(data):
    """Iniciar sesión de usuarios. Acepta email y contraseña y devuelve detalles del usuario si es válido"""
    try:
        email = data.get("email")
        password = data.get("password")
        user = User.query.filter_by(email=email).first()

        if user and user.verify_password(password):
            return jsonify(user.to_dict()), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401
    except SQLAlchemyError as err:
        return handle_sqlalchemy_error(err)


@home.route("/users", methods=["GET"])
@home.response(200, UserSchema)
@home.response(500, ErrorResponseSchema)
def get_users():
    """Obtener una lista de todos los usuarios"""
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    except SQLAlchemyError as err:
        return handle_sqlalchemy_error(err)


@home.route("/users", methods=["POST"])
@home.arguments(UserCreateRequestSchema)
@home.response(200, UserSchema)
@home.response(500, ErrorResponseSchema)
def create_user(data):
    """Crear un nuevo usuario"""
    try:
        existing_user = User.query.filter_by(email=data["email"]).first()
        if existing_user:
            return jsonify({"error": "A user with this email already exists"}), 409

        new_user = User(
            name=data["name"],
            lastname=data["lastname"],
            email=data["email"],
            phone=data["phone"],
            password=data["password"],
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except SQLAlchemyError as err:
        db.session.rollback()
        return handle_sqlalchemy_error(err)


@home.route("/users/<id>", methods=["GET"])
@home.response(200, UserSchema)
@home.response(500, ErrorResponseSchema)
def get_user_by_id(id):
    """Obtener detalles de un usuario específico por ID"""
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user.to_dict()), 200
    except SQLAlchemyError as err:
        return handle_sqlalchemy_error(err)


@home.route("/users/<id>", methods=["PUT"])
@home.arguments(UserCreateRequestSchema)
@home.response(200, UserSchema)
@home.response(500, ErrorResponseSchema)
def update_user(data, id):
    """Actualizar un usuario existente por ID"""
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        if user.email != data["email"]:
            existing_user = User.query.filter_by(email=data["email"]).first()
            if existing_user:
                return jsonify({"error": "A user with this email already exists"}), 409

        for key, value in data.items():
            if key == "password" and value:
                user.password = value
            else:
                setattr(user, key, value)
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return handle_sqlalchemy_error(err)


@home.route("/users/<id>", methods=["DELETE"])
@home.response(200, UserSchema)
@home.response(500, ErrorResponseSchema)
def delete_user(id):
    """Eliminar un usuario por ID"""
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return handle_sqlalchemy_error(err)


@home.route("/contacts", methods=["GET"])
@home.response(200, ContactSchema)
@home.response(500, ErrorResponseSchema)
def get_contacts():
    """Obtener una lista de todos los usuarios que hay que contactar"""
    try:
        contacts = Contact.query.all()
        return jsonify([contact.to_dict() for contact in contacts]), 200
    except SQLAlchemyError as err:
        return handle_sqlalchemy_error(err)


@home.route("/contacts", methods=["POST"])
@home.arguments(ContactCreateRequestSchema)
@home.response(200, ContactSchema)
@home.response(500, ErrorResponseSchema)
def create_contact(data):
    """Crear un nuevo contacto"""
    try:
        existing_contact = Contact.query.filter_by(email=data["email"]).first()
        if existing_contact:
            return jsonify({"error": "A contact with this email already exists"}), 409

        new_contact = Contact(
            name=data["name"],
            lastname=data["lastname"],
            email=data["email"],
            topic=data["topic"],
            message=data["message"],
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify(new_contact.to_dict()), 201
    except SQLAlchemyError as err:
        db.session.rollback()
        return handle_sqlalchemy_error(err)


@home.route("/contacts/<id>", methods=["GET"])
@home.response(200, ContactSchema)
@home.response(500, ErrorResponseSchema)
def get_contact_by_id(id):
    """Obtener detalles de un contacto específico por ID"""
    try:
        contact = Contact.query.get(id)
        if not contact:
            return jsonify({"error": "Contact not found"}), 404
        return jsonify(contact.to_dict()), 200
    except SQLAlchemyError as err:
        return handle_sqlalchemy_error(err)


@home.route("/contacts/<id>", methods=["PUT"])
@home.arguments(ContactCreateRequestSchema)
@home.response(200, ContactSchema)
@home.response(500, ErrorResponseSchema)
def update_contact(data, id):
    """Actualizar un contacto existente por ID"""
    try:
        contact = Contact.query.get(id)
        if not contact:
            return jsonify({"error": "Contact not found"}), 404

        if contact.email != data["email"]:
            existing_contact = Contact.query.filter_by(email=data["email"]).first()
            if existing_contact:
                return jsonify(
                    {"error": "A contact with this email already exists"}
                ), 409

        for key, value in data.items():
            setattr(contact, key, value)
        db.session.commit()
        return jsonify(contact.to_dict()), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return handle_sqlalchemy_error(err)


@home.route("/contacts/<id>", methods=["DELETE"])
@home.response(200, ContactSchema)
@home.response(500, ErrorResponseSchema)
def delete_contact(id):
    """Eliminar un contacto por ID"""
    try:
        contact = Contact.query.get(id)
        if not contact:
            return jsonify({"error": "Contact not found"}), 404

        db.session.delete(contact)
        db.session.commit()
        return jsonify(contact.to_dict()), 200
    except SQLAlchemyError as err:
        db.session.rollback()
        return handle_sqlalchemy_error(err)


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
