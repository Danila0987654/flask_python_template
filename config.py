from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    _true_values = ['yes', 'y', 'true', '1']

    FLASK_HOST = os.getenv("HOST")
    FLASK_PORT = os.getenv("PORT")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG").lower() in _true_values
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv('DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS').lower() in _true_values
