from flask import Flask
from .database import database
from app import models
from app import config
from app.routes import create_router

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
database.init_app(app)


def create_app():
    create_router(app)
    return app
