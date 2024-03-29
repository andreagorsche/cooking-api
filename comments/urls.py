from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('inappropriate/<int:pk>/', views.MarkCommentInappropriate.as_view()),
   ]
