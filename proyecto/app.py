from flask import Flask  # Importación de terceros (primero)

from flask_sqlalchemy import SQLAlchemy

from routes.contacts import contacts

from flask_sqlalchemy import SQLAlchemy

from utils.db import db


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg2://postgres:1234@localhost:5432/contactsdb"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


app.register_blueprint(contacts)
