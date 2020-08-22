from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Migrate = Migrate(app, db)
api = Api(app)

from app import routes, models

# from app.api import bp as api_bp
# app.register_blueprint(api_bp)

from app.resources.contact_resource import ContactResourceList
api.add_resource(ContactResourceList, '/contact')

from app.resources.contact_resource import ContactResource
api.add_resource(ContactResource, '/contact/<contact_id>')
