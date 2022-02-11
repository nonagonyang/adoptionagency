# Defining the Form Class
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import InputRequired, Optional, URL,NumberRange,AnyOf


class AddPetForm(FlaskForm):
    """
    Form for adding pets.
    Pet name
    Species
    Photo URL
    Age
    Notes
    """
    pet_name = StringField("Pet Name", validators=[InputRequired(message="Pet name is required")])
    species= StringField("Pet Species", validators=[AnyOf(["cat","dog","porcupine"],message="the species should be either “cat”, “dog”, or “porcupine”")])
    photo_URL=StringField("Photo_URL" ,validators=[Optional(), URL(message="Please type an URL")])
    age=IntegerField("Age", validators=[NumberRange(min=0, max=30, message="The age should be between 0 and 30")])
    notes=StringField("Notes")