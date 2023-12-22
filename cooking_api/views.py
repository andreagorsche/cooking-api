from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)
from allauth.account.models import EmailConfirmation
from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.models import User

# New signal for handling email confirmation
@receiver(email_confirmed)
def email_confirmed_handler(request, email_address, **kwargs):
    user = email_address.user
    print("Email confirmed:", user.username)
    # Your custom logic for handling email confirmation

# Custom API view for handling email confirmation
@api_view(['GET'])
def confirm_email(request):
    # Extract confirmation key from the request query parameters
    key = request.GET.get('key', '')
    print("Confirmation Key:", key)  # Add this line for debugging

    try:
        # Perform the email confirmation using Allauth's utility function
        email_confirmation = EmailConfirmation.objects.get(key=key)
        email_confirmation.confirm()
        # Trigger your custom signal when email is confirmed
        email_confirmed.send(sender=request, email_address=email_confirmation.email_address)
        return Response({"message": "Email confirmed successfully"})
    except EmailConfirmation.DoesNotExist:
        print("Confirmation Key does not exist in the database")  # Add this line for debugging
        return Response({"message": "Email confirmation failed. Invalid key."}, status=400)


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