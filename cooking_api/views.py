from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from allauth.account.models import EmailConfirmation
from dj_rest_auth.registration.views import RegisterView
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CustomRegistrationView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.user

        # Generate email confirmation key
        email_confirmation = EmailConfirmationHMAC(user)
        key = email_confirmation.key

        # Build the activation link
        activation_link = f"{get_current_site(request).domain}/accounts/confirm-email/{key}/"

        # Prepare email content
        subject = "Confirm your registration"
        email_recipient = user.email
        html_msg = render_to_string("email.html", {'activation_link': activation_link})
        plain_msg = strip_tags(html_msg)

        # Send the email
        send_mail(
            subject,
            plain_msg,
            None,
            [email_recipient],
            html_message=html_msg,
        )


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my cooking API!"
    })


# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response