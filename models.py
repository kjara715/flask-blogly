"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

#models go below
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
               
    first_name = db.Column(db.String(25),
                     nullable=False)

    last_name = db.Column(db.String(25),
                     nullable=False)
    image_url = db.Column(db.String, 
                    nullable=True)
    

    def greet(self):
        """Greet using name."""

        return f"Hi I am {self.name} the {self.species}"

    def feed(self, amt=20):
        """Nom nom nom. Update hunger based off amt"""

        self.hunger -= amt
        self.hunger = max(self.hunger, 0)