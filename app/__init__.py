from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
migr = Migrate(db=db)

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migr.init_app(app)

from app.routes.errors import bp as error_bp
print(error_bp)
app.register_blueprint(error_bp)

from app.routes.main import bp as main_bp
app.register_blueprint(main_bp)

from app.models.user import User
