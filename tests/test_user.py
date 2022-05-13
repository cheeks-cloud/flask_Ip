import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'password')

    def test__init(self,bio,id,username,email):
        self.assertEqual(self.new_user.id,)
        self.assertEqual(self.new_user.bio,)
        self.assertEqual(self.new_user.email,)
        self.assertEqual(self.new_user.username,)




    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('password'))