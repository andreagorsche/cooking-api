from django.contrib import admin
from django.urls import path, include 
from .views import root_route, logout_route, CustomRegistrationView
from django.conf.urls import url
from .views import confirm_email

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/logout/', logout_route), #logout route
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', CustomRegistrationView.as_view(), name='dj-rest-auth-registration'),
    #path('confirm-email/<str:key>/', CustomEmailConfirmationView.as_view(), name='custom_email_confirmation'),
    url(  # Use url() to include the specific pattern
        r'^verify-email/(?P<key>\w+)/$',  # Pattern for verify-email
        confirm_email,
        name="account_confirm_email"
    ),
    path('accounts/', include('allauth.urls')),   
    path('', include('profiles.urls')),
    path('', include('recipes.urls')),
    path('', include('comments.urls')),
    path('', include('followers.urls')),
    path('', include('ratings.urls')),

]
