
"""
    Base Test Class

    This class should be the parent class to each non-unit test.
    It allows for instantiation of the test client and the database,
    and makes sure that the database is a new, blank database each time.
"""

from unittest import TestCase
from RestAPI.app import app
from RestAPI.db import db

class BaseTest(TestCase):
    def setUp(self):
        # Make sure database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test client
        self.app = app.test_client
        self.app_context = app.app_context
    
    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()