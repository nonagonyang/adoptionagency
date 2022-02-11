"""AdoptionAgency application."""
from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRETMAOMI"
debug = DebugToolbarExtension(app)

connect_db(app)
 

@app.route("/")
def show_pets():
    """
    The homepage (at route`/`) should list the pets:
    name
    show photo, if present
    display “Available” in bold if the pet is available for adoption
    """
    pets=Pet.query.all()
    return render_template("homepage.html" ,pets=pets)


# Create a form for adding pets. This should use Flask-WTF, and should have the following fields:
# Pet name
# Species
# Photo URL
# Age
# Notes
# This should be at the URL path /add. Add a link to this from the homepage.

@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """show Pet add form; handle adding."""
    # create an instance of wtfform
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_URL=form.photo_URL.data
        age=form.age.data
        notes=form.notes.data
        new_pet=Pet(pet_name=name,species=species,photo_url=photo_URL,age=age,notes=notes)
        
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name} a species of {species}")
        return redirect("/")

    else:
        return render_template("pet_add_form.html", form=form)




@app.route("/<int:pet_id/edit", methods=["GET", "POST"])
def edit_user(pet_id):
    """
    Make a page that shows some information about the pet:
    Name
    Species
    Photo, if present
    Age, if present
    It should also show a form that allows us to edit this pet:
    Photo URL
    Notes
    Available
    This should be at the URL /[pet-id-number]. Make the homepage link to this.
    """

    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_URL = form.photo_URL.data
        pet.notes = form.notes.data
        pet.available=form.available.data
        db.session.commit()
        flash(f"Pet {Pet.name} updated!")
        return redirect(f"/{pet_id}/edit")

    else:
        return render_template("pet_edit_form.html", form=form)