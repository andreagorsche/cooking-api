from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='andrea', password='rookiecoder')

    def test_can_list_profiles(self):
        andrea = User.objects.get(username='andrea')
        Profile.objects.create(chef=andrea, bio='andreas bio')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logged_in_user_can_create_profile(self):
        self.client.login(username='andrea', password='rookiecoder')
        response = self.client.post('/profiles/', {'bio': 'andreas bio'})
        count = Profile.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_create_profile(self):
        response = self.client.post('/profiles/', {'bio': 'andreas bio'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

