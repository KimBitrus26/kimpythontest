from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from config import Config


#instantiate flask class
app = Flask(__name__)

app.config.from_object(Config)

#creating db object
db = SQLAlchemy(app)

#initialize marshmallow
ma = Marshmallow(app)

#initialize migrate object
migrate = Migrate(app, db)

#seperation of concerns
from app import routes, models
