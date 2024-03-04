from rest_framework.decorators import api_view
from rest_framework.response import Response
from dj_rest_auth.registration.views import RegisterView
from allauth.account.utils import send_email_confirmation
from profiles.models import Profile
from django.conf import settings
from django.shortcuts import redirect
from allauth.account.views import ConfirmEmailView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework import status
from django.http import HttpResponse
from allauth.account.models import EmailConfirmation
from django.http import HttpRequest


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

        return response

def get_frontend_url(request: HttpRequest) -> str:
    if request.headers.get('X-Frontend-Environment') == 'development':
        return settings.DEV_FRONTEND_URL
    else:
        return settings.PROD_FRONTEND_URL
        

def confirm_email(request, key):
    # Use EmailConfirmation Model 
    try:
        email_confirmation = EmailConfirmation.objects.get(key=key)
    except EmailConfirmation.DoesNotExist:
        return HttpResponseBadRequest("Invalid activation link")

    # Mark the email as verified
    email_confirmation.confirm(request)

    # call the get frontend_url
    frontend_url = get_frontend_url(request)

     # Redirect to frontend after confirmation
    return redirect(frontend_url)

    return HttpResponse("Email verified successfully.")

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