from ..database import database
from werkzeug.security import generate_password_hash, check_password_hash


class User(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(60), index=True, unique=True)
    username = database.Column(database.String(60), index=True, unique=True)
    first_name = database.Column(database.String(60), index=True)
    last_name = database.Column(database.String(60), index=True)
    password_hash = database.Column(database.String(128))
    is_admin = database.Column(database.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)
