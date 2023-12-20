from django.test import TestCase
from django.core import mail
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress
from allauth.account.signals import user_signed_up

class RegistrationTestCase(TestCase):
    def test_send_registration_email(self):
        User = get_user_model()

        # Simulate user signup
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        EmailAddress.objects.create(user=user, email=user.email, primary=True, verified=True)

        # Trigger the signal
        user_signed_up.send(sender=user.__class__, request=None, user=user)

        # Check if the email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Welcome to Cook-Around-The-Clock")
        self.assertEqual(mail.outbox[0].to, [user.email])
