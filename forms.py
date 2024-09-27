from flask_wtf import FlaskForm
from wtforms import StringField, URLField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange

# Choices for pet species in the dropdown
choices = [('cat', 'Cat'),('dog', 'Dog'),('porcupine','Porcupine')]

class AddPetForm(FlaskForm):
    """
    Form for adding or editing a pet's information.

    This form includes fields for the pet's name, species, photo URL,
    age, notes, and availability status.
    """
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Pet Species", choices=choices, validators=[InputRequired()])
    photo_url = URLField('Pet Photo URL', validators=[Optional()])
    age = IntegerField('Pet Age', validators=[Optional(), NumberRange(min=0, max=30, message='Pet age must be between 0 and 30')])
    notes = StringField("Notes")
    available = BooleanField("Available")


