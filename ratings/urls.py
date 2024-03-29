from django.urls import path
from . import views

urlpatterns = [
    path('ratings/', views.RatingList.as_view()),
    path('ratings/<int:pk>/', views.RatingDetail.as_view()),
]
