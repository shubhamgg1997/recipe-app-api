from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        '''Test creating a new user with email is succesful'''
        email="test@recipe.com"
        password='Testpass123'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailized(self):
        '''Test the email for a new user is normalized'''
        email="test@RECIPE.COM"
        user=get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())
    
    def test_new_user_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        user=get_user_model().objects.create_superuser(
            email='test@recipe.com',
            password='test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

