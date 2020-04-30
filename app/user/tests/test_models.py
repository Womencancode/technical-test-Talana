from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user is successful"""
        email = 'user@talana.com'
        password = "test123"
        telephone = '+569 0000 0101'
        name = 'User X'
        last_name = 'Last name Y'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            telephone=telephone,
            name=name,
            last_name=last_name
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))  # Pass encrypted
        self.assertEqual(user.name, name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.telephone, telephone)
