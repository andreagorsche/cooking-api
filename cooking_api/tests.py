from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from allauth.account.models import EmailAddress

class VerifyEmailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user (assuming you have a registration endpoint)
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        # Force email verification for the user
        email_address = EmailAddress.objects.create(user=self.user, email=self.user.email, verified=False, primary=True)
        self.verification_key = email_address.confirmation_key

    def test_verify_email_success(self):
        # Reverse URL resolution to get the URL for the verify-email endpoint
        url = reverse('account_confirm_email', kwargs={'key': self.verification_key})
        
        # Make a GET request to the endpoint
        response = self.client.get(url)
        
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the response contains the expected message or data
        self.assertEqual(response.data['detail'], 'Email address confirmed')
