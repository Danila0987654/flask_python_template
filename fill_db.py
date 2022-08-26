from app.models.user import User

from app import app, db


names = ["Danila", "Test"]

with app.app_context():
    for name in names:
        new_user = User(
            name=name
        )
        db.session.add(new_user)
    db.session.commit()