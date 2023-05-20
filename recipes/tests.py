from django.contrib.auth.models import User
from .models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='andrea', password='rookiecoder')

    def test_can_list_posts(self):
        andrea = User.objects.get(username='andrea')
        Recipe.objects.create(chef=andrea, title='recipe title')
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    