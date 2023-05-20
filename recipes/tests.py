from django.contrib.auth.models import User
from .models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='andrea', password='rookiecoder')

    def test_can_list_recipes(self):
        andrea = User.objects.get(username='andrea')
        Recipe.objects.create(chef=andrea, title='recipe title')
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logged_in_user_can_create_recipe(self):
        self.client.login(username='andrea', password='rookiecoder')
        response = self.client.post('/recipes/', {'title': 'recipe title'})
        count = Recipe.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_create_recipe(self):
        response = self.client.post('/recipes/', {'title': 'recipe title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)