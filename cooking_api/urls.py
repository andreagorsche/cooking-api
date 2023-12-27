from django.contrib import admin
from django.urls import path, include 
from .views import root_route, logout_route, CustomRegistrationView

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/logout/', logout_route), #logout route
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # Include custom registration view from dj-rest-auth
    path('dj-rest-auth/registration/', CustomRegistrationView.as_view(), name='dj-rest-auth-registration'),    
    path('accounts/', include('allauth.urls')),
    path('', include('profiles.urls')),
    path('', include('recipes.urls')),
    path('', include('comments.urls')),
    path('', include('followers.urls')),
    path('', include('ratings.urls')),

]
