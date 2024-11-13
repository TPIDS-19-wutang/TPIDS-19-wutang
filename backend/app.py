from flask import Flask
from models import db, bcrypt
from api import home
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.logger.info("config-- %s\n", app.config)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("POSTGRES_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.logger.info("config-- %s\n", app.config)

app.register_blueprint(home, url_prefix="")

migrate = Migrate(app, db)

db.init_app(app)
bcrypt.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run("127.0.0.1", port="5001", debug=True)
