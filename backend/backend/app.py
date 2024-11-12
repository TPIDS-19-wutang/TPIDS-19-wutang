from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from backend.models import db
from backend.api import home

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1/wutang'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(home, url_prefix='')

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run("127.0.0.1", port="5001", debug=True)
