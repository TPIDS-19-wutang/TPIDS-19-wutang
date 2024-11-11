from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from models import db, User, Contact

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/hotel'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.errorhandler(404)
def endp_not_found(e):
    return 0

@app.route('/users', methods=["POST"])
def add_user():
    data = request.get_json()
    try:
        new_user = User(
            name=data['name'],
            lastname=data['lastname'],
            email=data['email'],
            phone=data['phone'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 201
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500
    
@app.route('/users', methods=["GET"])
def get_users():
    id = request.args.get('id')
    try:
        if id:
            user = User.query.get(id)
            if not user:
                return jsonify({'error': 'User not found'}), 404
            return jsonify({
                "id": user.id_user,
                "name": user.name,
                "lastname": user.lastname,
                "email": user.email,
                "phone": user.phone,
                "created_at": user.created_at
            })
        else:
            users = User.query.all()
            return jsonify([{
                "id": user.id_user,
                "name": user.name,
                "lastname": user.lastname,
                "email": user.email,
                "phone": user.phone,
                "created_at": user.created_at
            } for user in users])
    except SQLAlchemyError as err:
        return jsonify({'error': str(err)}), 500
    
@app.route('/contacts', methods=["GET"])
def get_contacts():
    try:
        contacts = Contact.query.all()
        contact_list = [{
            "id": contact.id_contact,
            "name": contact.name,
            "lastname": contact.lastname,
            "email": contact.email,
            "topic": contact.topic,
            "message": contact.message,
            "status": contact.status,
            "created_at": contact.created_at
        } for contact in contacts]

        return jsonify(contact_list), 200
    except SQLAlchemyError as err:
        return jsonify({'error': str(err)}), 500

@app.route('/contacts', methods=["POST"])
def contact():
    data = request.get_json()
    try:
        new_contact = Contact(
            name=data['name'],
            lastname=data['lastname'],
            email=data['email'],
            topic=data['topic'],
            message=data['message']
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"message": "Contact added successfully"}), 201
    except SQLAlchemyError as err:
        db.session.rollback()
        return jsonify({'error': str(err)}), 500

@app.route('/user', methods=["PUT"])
def update_user():
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
def get_reservations():
    return 0

if __name__ == "__main__":
    app.run("127.0.0.1", port="5001", debug=True)