"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
user1 = User(first_name='Marley', last_name='Fischer', image_url='https://www.stockvault.net/data/2010/09/21/114948/preview16.jpg')
user2 = User(first_name='Alyssa', last_name='Keratin', image_url='https://www.stockvault.net/data/2011/04/12/121747/preview16.jpg')
user3 = User(first_name='Johnny', last_name='Harrington')

# Add new objects to session, so they'll persist
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

# Commit--otherwise, this never gets saved!
db.session.commit()
