import pytest

from app import app as main_app, db
from app.models.user import User


@pytest.fixture()
def app():
    application = main_app
    application.config["TESTING"] = True
    application.config["DEBUG"] = False
    application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://tests/db.db"
    yield application


@pytest.fixture()
def client(app):
    with app.test_client() as client:
        with app.app_context():
            db.create_all()

            names = ["Danila", "Test"]
            for name in names:
                new_user = User(
                    name=name
                )
                db.session.add(new_user)
            db.session.commit()
        yield client
        db.drop_all()
