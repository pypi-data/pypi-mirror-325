from flask_sqlalchemy import SQLAlchemy
from config.settings import app

db = SQLAlchemy(app)