from rest_framework.decorators import api_view
from rest_framework.response import Response
from dj_rest_auth.registration.views import RegisterView
from allauth.account.utils import send_email_confirmation
from profiles.models import Profile
from django.conf import settings

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