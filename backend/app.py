from flask import Flask
from models import db, bcrypt
from api import home
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_smorest import Api

app = Flask("Wutang")

load_dotenv()

app.config["API_TITLE"] = "Wutang API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"

app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = (
    "https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.24.2/"
)

app.config["OPENAPI_REDOC_PATH"] = "/redoc"
app.config["OPENAPI_REDOC_URL"] = (
    "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("POSTGRES_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

api.register_blueprint(home, url_prefix="")

migrate = Migrate(app, db)

db.init_app(app)
bcrypt.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run("127.0.0.1", port="5001", debug=True)
