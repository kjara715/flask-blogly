from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test_users'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests for views for Pets."""

    def setUp(self):
        """Add sample user."""

        User.query.delete()

        user = User(first_name="Spongebob", last_name="SquarePants", image_url="https://i2-prod.mirror.co.uk/incoming/article4330476.ece/ALTERNATES/s1200b/Spongebob-Squarepants.jpg")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up anything in the session before next test."""

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

    def test_new_user_form(self):
        with app.test_client() as client:
            resp=client.get('/users/new')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Create New User</h1>', html)
    
    def test_new_details(self):
        with app.test_client() as client:
            resp=client.get(f'/users/{self.user_id}')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h2>Spongebob SquarePants</h2>', html)

    def test_edit_user(self):
        with app.test_client() as client:
            resp=client.get(f'/users/{self.user_id}/edit-user')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Edit User</h1>', html)

    # def test_show_pet(self):
    #     with app.test_client() as client:
    #         resp = client.get(f"/{self.pet_id}")
    #         html = resp.get_data(as_text=True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn('<h1>TestPet</h1>', html)

    # def test_add_pet(self):
    #     with app.test_client() as client:
    #         d = {"name": "TestPet2", "species": "cat", "hunger": 20}
    #         resp = client.post("/", data=d, follow_redirects=True)
    #         html = resp.get_data(as_text=True)

    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn("<h1>TestPet2</h1>", html)