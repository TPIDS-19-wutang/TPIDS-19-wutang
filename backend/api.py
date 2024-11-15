from flask import Flask
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

api = Flask(__name__)

if __name__ == '__main__':
    api.run(debug=True)