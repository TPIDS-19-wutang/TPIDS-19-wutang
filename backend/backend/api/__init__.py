from flask import Blueprint
from . import routes

home = Blueprint("home", __name__)

__all__ = ["routes"]
