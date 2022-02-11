"""Seed file to make sample data for pets."""

from models import Pet,db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()



# Add pets
pet1=Pet(   pet_name="saddy", 
            species="Afador", 
            photo_url="https://www.dogtime.com/assets/uploads/2019/08/afador-mixed-dog-breed-pictures-1-1442x1328.jpg",
            age=1,
            notes="He is a bit sad",
            available=True)
pet2=Pet(   pet_name="feety", 
            species="Dachshund",
            photo_url="https://dogtime.com/assets/uploads/gallery/dachshund-dog-breed-pictures/side-5_680-453.jpg",
            age=2,
            notes="A cute girl",
            available=True)
pet3=Pet(   pet_name="jackie",
            species="Jackshund",
            photo_url="https://dogtime.com/assets/uploads/gallery/jackshund-mixed-dog-breed-pictures/jackshund-mixed-dog-breed-pictures-4.jpg",
            age=3,
            notes="Jakie likes to play",
            available=True 
)

db.session.add_all([pet1,pet2,pet3])
db.session.commit()