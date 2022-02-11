"""Models for AdoptionAgency."""

from typing_extensions import Self
from flask_sqlalchemy import SQLAlchemy

#create SQLAlchemy instance and save into the variable db
db=SQLAlchemy()
def connect_db(app):
    db.app=app
    db.init_app(app)


class Pet(db.Model):
    __tablename__='pets'
    # def __repr__(self):
    #     p=self
    #     return f"< Pet id={p.id},pet_name={p.pet_name}, species={p.species}>"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    pet_name=db.Column(db.Text,nullable=False)
    species=db.Column(db.Text,nullable=True)
    photo_url=db.Column(db.String(200),nullable=True)
    age=db.Column(db.Integer, nullable=True)
    notes=db.Column(db.Text, nullable=True)
    available=db.Column(db.Boolean, nullable=False, default=True)
