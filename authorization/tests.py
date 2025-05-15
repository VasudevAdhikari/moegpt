from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class UserAuthTests(TestCase):

    def setUp(self):
        # Create a user for testing
        self.username = 'testuser11'
        self.email = 'testuser11@example.com'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)

    def test_login_success(self):
        # Test successful login
        response = self.client.post(reverse('login'), {'mail': self.email, 'pwd': self.password})
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertRedirects(response, '/chatbot/')  # Check redirect URL
        self.assertTrue(response.wsgi_request.user.is_authenticated)  # Check if user is authenticated
        messages_list = list(get_messages(response.wsgi_request))
        self.assertIn('Login successful!', [str(msg) for msg in messages_list])  # Check for success message

    def test_login_invalid(self):
        # Test login with invalid credentials
        response = self.client.post(reverse('login'), {'mail': self.email, 'pwd': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # Check for successful rendering of login page
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # User should not be authenticated
        messages_list = list(get_messages(response.wsgi_request))
        self.assertIn('Invalid username or password.', [str(msg) for msg in messages_list])  # Check for error message

    def test_register_success(self):
        # Test successful registration
        response = self.client.post(reverse('register'), {'uname': 'newuser', 'mail': 'newuser@example.com', 'pwd': 'newpassword'})
        self.assertEqual(response.status_code, 302)  # Check for redirect
        self.assertRedirects(response, '/chatbot/')  # Check redirect URL
        self.assertTrue(response.wsgi_request.user.is_authenticated)  # Check if user is authenticated

    def test_register_existing_user(self):
        # Test registration with an existing username
        response = self.client.post(reverse('register'), {'uname': self.username, 'mail': self.email, 'pwd': 'newpassword'})
        self.assertEqual(response.status_code, 200)  # Check for successful rendering of register page
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # User should not be authenticated
        messages_list = list(get_messages(response.wsgi_request))
        self.assertIn('A user with that username already exists.', [str(msg) for msg in messages_list])  # Check for error message
