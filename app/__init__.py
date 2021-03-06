from flask import Flask
from config import Config
from app import app
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
#db = SQLAlchemy(app)
#migrate = Migrate(app, db)



#The lowercase "config" is the name of the Python module config.py,
# and obviously the one with the uppercase "C" is the actual class.

from app import routes