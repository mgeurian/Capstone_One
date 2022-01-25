from flask_sqlalchemy import SQLAlchemy
from user_models import User
from flask_bcrypt import Bcrypt

fl_bcrypt = Bcrypt()

db = SQLAlchemy()

def connect_db(app):
    """ Connect to database. """

    db.app = app
    db.init_app(app)

class User(db.Model):
    """ USER. """

    __tablename__ = "users"

    username = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)

    password = db.Column(db.Text, nullable=False)

    email = db.Column(db.String(50), nullable=False, unique=True)

    first_name = db.Column(db.String(30), nullable=False)

    last_name = db.Column(db.String(30), nullable=False)

    users_currency = db.relationship("User_Currency", backref="user", cascade="all, delete")


    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        """ Register user w/hashed password $& return user. """

        hashed = fl_bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)


    @classmethod
    def authenticate(cls, username, pwd):
        """ Validate that user exists & password is correct.

        Return user if valid; else return false.
        """

        u = User.query.filter_by(username=username).first()

        if u and fl_bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False




class Currency(db.Model):
    """ CRYPTOCURRENCY. """

    __tablename__ = "currencies"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)

    symbol = db.Column(db.String, nullable=False)
    
    slug = db.Column(db.String, nullable=False)

    logo = db.Column(db.String)

    description = db.Column(db.String)

    price = db.Column(db.Float)


    def serialize_currency(self):
        return {
            'id': self.id,
            'name': self.name,
            'symbol': self.symbol,
            'slug': self.slug,
            'logo': self.logo,
            'description': self.description,
            'price': self.price
        }



class User_Currency(db.Model):
    """ USER_CURRENCY. """

    __tablename__ = "users_currencies"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String, db.ForeignKey('users.username'))

    currency_id = db.Column(db.Integer, db.ForeignKey('currencies.id'))
