"""Models for Feedback app."""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    username = db.Column(db.Text, db.String(
        20), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.Text, db.String(30), nullable=False)
    last_name = db.Column(db.Text, db.String(30), nullable=False)

    # def to_dict(self):
    #     """Serialize user to a dict of user info."""

    #     return {
    #         "id": self.id,
    #         "username": self.username,
    #         "password": self.password,
    #         "email": self.email,
    #         "first_name": self.first_name,
    #         "last_name": self.last_name,
    #     }

    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")
        user = cls(
            username=username,
            password=hashed_utf8,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        # return instance of user w/username and hashed pwd
        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False


class Feedback(db.Model):
    """Feedback."""

    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(
        db.String(20),
        db.ForeignKey('users.username'),
        nullable=False,
    )
