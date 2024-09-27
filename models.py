from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Model representing a pet in the database.
    
    Attributes:
        id (int): Unique identifier for each pet, automatically incremented.
        name (str): Name of the pet; cannot be null.
        species (str): Species of the pet; cannot be null.
        photo_url (str): URL for the pet's photo; can be null.
        age (int): Age of the pet; can be null.
        notes (str): Additional notes about the pet; can be null.
        available (bool): Availability status of the pet; defaults to True (available).
    """

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.String(50),
                     nullable=False)
    
    species = db.Column(db.String(50),
                     nullable=False)
    
    photo_url = db.Column(db.String)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False, default = True)

 