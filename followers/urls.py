from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowerList.as_view()),
    path('followers/<int:pk>/', views.FollowerDetail.as_view()),
    path(
        'unfollow/<int:followed_id>/',
        views.UnfollowUserView.as_view(),
        name='unfollow_user'
    ),
]
