from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    def setUp(self):
        user = User.objects.create(username='andrea')
        user.set_password('rookiecoder')
        user.save()
        self.user = user

    def test_can_list_profiles(self):
        Profile.objects.create(chef=self.user, bio='andreas bio')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        andrea = User.objects.create_user(username='andrea', password='rookiecoder')
        carina = User.objects.create_user(username='carina', password='bambina')
        Profile.objects.create(
            chef=andrea, bio='andreas bio'
        )
        Profile.objects.create(
            chef=carina, bio='carinas bio'
        )

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_profile(self):
        self.client.login(username='carina', password='bambina')
        response = self.client.put('/profiles/2/', {'bio': 'carinas bio'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(response.data['bio'], 'carinas bio')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_profile(self):
        self.client.login(username='andrea', password='rookiecoder')
        response = self.client.put('/profiles/2/', {'bio': 'carinas bio'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  

