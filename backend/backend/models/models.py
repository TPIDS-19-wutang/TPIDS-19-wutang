from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Hotel(db.Model):
    __tablename__ = 'hotels'
    id_hotel = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(120))
    cant_rooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    amenities = db.Column(db.String(255), nullable=True)
    contact_info = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id_reservation = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    id_room = db.Column(db.Integer, db.ForeignKey('rooms.id_room'), nullable=False)
    id_hotel = db.Column(db.Integer, db.ForeignKey('hotels.id_hotel'), nullable=False)
    number_room = db.Column(db.Integer)
    check_in = db.Column(db.TIMESTAMP)
    check_out = db.Column(db.TIMESTAMP)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Contact(db.Model):
    __tablename__ = 'contacts'
    id_contact = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    topic = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), server_default="Pending")
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), nullable=False, unique=True)
    room_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
