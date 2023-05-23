from django.contrib.auth.models import User
from .models import Like
from rest_framework import status
from rest_framework.test import APITestCase

"""
class LikeListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='andrea', password='rookiecoder')

    def test_can_list_likes(self):
        andrea = User.objects.get(username='andrea')
        Like.objects.create(chef=andrea, created_at: '2023-05-20T19:41:59.892809Z')
        response = self.client.get('/like/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logged_in_user_can_like_another_users_post(self):
        self.client.login(username='andrea', password='rookiecoder')
        response = self.client.post('/likes/', {created_at: '2023-05-20T19:41:59.892809Z'})
        count = Like.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_like_another_users_post(self):
        response = self.client.post('/likes/', {created_at: '2023-05-20T19:41:59.892809Z'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
"""