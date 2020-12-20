import unittest
from run import db
from app.users.models import User

class BaseTestClass(unittest.TestCase):

    def setUp(self):
        db.create_all()
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @staticmethod
    def create_user(id, username, image_url, type, link):
        user = User(id, username, image_url, type, link)
        user.save()
        return user