from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

# Application configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'oh-so-secret'

# Debug Toolbar
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# Database setup
connect_db(app)
db.create_all()

# Default photo URL in case user does not provide one
default_photo_url = "https://mir-s3-cdn-cf.behance.net/project_modules/disp/775c1b96352685.5eac4787ab295.jpg"


@app.route('/')
def home():
    """Display the homepage with a list of all pets."""
    pets = Pet.query.all()  # Fetch all pets from the database
    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    """Display the 'Add Pet' form and handle form submission.
       If the form is submitted and validated, adds a new pet to the database.
       Otherwise, re-renders the form for correction.
    """
    form = AddPetForm() # Instantiate the form for adding a pet

    # Extract and validate form data
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo_url.data if form.photo_url.data else default_photo_url
        age = form.age.data
        notes = form.notes.data

        # Create a new Pet instance and add it to the database
        pet = Pet(name=name, species=species, photo_url = photo, age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()

        flash("Pet added successfully!")
        return redirect("/")

    else:
        return render_template('add_pet_form.html', form = form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def pet_detail_page(pet_id):
    """
    Display the details of a specific pet and an edit form.
    
    If the form is submitted and validated, update the pet's details in the database.
    Otherwise, display the current pet details and the edit form.
    """
    pet = Pet.query.get_or_404(pet_id)

    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        # Update pet information based on form input
        pet.photo_url = form.photo_url.data if form.photo_url.data else default_photo_url
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit() # Commit changes to database
        flash("Pet information updated!")
        return redirect(f"/{pet_id}")
    else:
        # If the form is not validated or it's a GET request, render the pet detail page
        return render_template('pet_detail_page.html', pet=pet, form=form)






    

