from flask_smorest import Blueprint

home = Blueprint("home", __name__, description="Base controller")

from . import routes
