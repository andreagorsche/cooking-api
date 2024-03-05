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
from django.contrib import messages
from allauth.account.models import EmailAddress
from django.http import JsonResponse



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
    

def verify_email(request, key):
    try:
        email_address = EmailAddress.objects.get(confirmation_key=key)
        if not email_address.verified:
            email_address.verified = True
            email_address.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Email address already verified.'})
    except EmailAddress.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Invalid verification key.'})


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