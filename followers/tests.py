from django.contrib.auth.models import User
from .models import Follower
from rest_framework import status
from rest_framework.test import APITestCase

class FollowerListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='andrea', password='rookiecoder')
        User.objects.create_user(username='carina', password='bambina')

    def test_can_list_followers(self):
        andrea = User.objects.get(username='andrea')
        Follower.objects.create(follower=andrea)
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logged_in_user_can_follow_another_user(self):
        self.client.login(username='andrea', password='rookiecoder')
        response = self.client.post('/followers/', {'followed_chef': 'carina'})
        count = Follower.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_follow_another_user(self):
        response = self.client.post('/followers/', {'followed_chef': 'carina'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
