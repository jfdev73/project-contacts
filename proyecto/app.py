from flask import Flask  # Importación de terceros (primero)

from flask_sqlalchemy import SQLAlchemy

from routes.contacts import contacts


app = Flask(__name__)


app.register_blueprint(contacts)
