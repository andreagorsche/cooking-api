from rest_framework.decorators import api_view
from rest_framework.response import Response
from dj_rest_auth.registration.views import RegisterView
from allauth.account.utils import send_email_confirmation
from profiles.models import Profile
from django.conf import settings
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

User = get_user_model()

class CustomRegistrationView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Check if 'user' is present in the response data
        user_data = response.data.get('user', None)

        if user_data:
            # Retrieve the user instance
            user = User.objects.get(id=user_data['id'])

            # Create a profile for the user
            Profile.objects.create(owner=user)
            
            # Send email confirmation
            send_email_confirmation(request, user)

        return response



def verify_email(request, key):
    try:
        # Retrieve the user associated with the email address
        email_address = EmailAddress.objects.get(activation_key=key)
        user = email_address.user
        # Mark the email address as verified
        email_address.verified = True
        email_address.save()
        # Optionally, mark the user's email as primary
        user.email = email_address.email
        user.save()
        # Optionally, perform any additional actions (e.g., update user profile)
        # Redirect to a success page or any other page
        messages.success(request, "Email verified successfully.")
        return HttpResponseRedirect(reverse('email_verification_success'))
    except EmailAddress.DoesNotExist:
        messages.error(request, "Invalid activation key.")
        return HttpResponseRedirect(reverse('email_verification_failure'))


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
        key=settings.JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=settings.JWT_AUTH_SAMESITE,
        secure=settings.JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=settings.JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=settings.JWT_AUTH_SAMESITE,
        secure=settings.JWT_AUTH_SECURE,
    )
    return response