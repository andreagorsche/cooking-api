from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from dj_rest_auth.registration.views import RegisterView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class CustomRegistrationView(RegisterView):
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.user

    # Send email confirmation with customized html mail
        email_subject = "Confirm your registration"
        email_recipient = request.data.get('email')  # Use request.data to access form data

        html_msg = render_to_string("templates/email.html")
        plain_msg = strip_tags(html_msg)

        msg = EmailMultiAlternatives(
            subject=email_subject,
            from_email=None,
            to=[email_recipient]
        )

        # Attach the plain text version of the email
        msg.attach_alternative(plain_msg, "text/plain")

        # Attach the HTML version of the email
        msg.attach(html_msg, "text/html")

        msg.send()


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