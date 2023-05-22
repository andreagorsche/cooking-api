from django.contrib.auth.models import User
from .models import Recipe
from rest_framework import status
from rest_framework.test import APITestCase


class RecipeListViewTests(APITestCase):
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
        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_create_recipe(self):
        response = self.client.post('/recipes/', {'title': 'recipe title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class RecipeDetailViewTests(APITestCase):
    def setUp(self):
        andrea = User.objects.create_user(username='andrea', password='rookiecoder')
        carina = User.objects.create_user(username='carina', password='bambina')
        Recipe.objects.create(
            chef=andrea, title='a title', description='andrea description'
        )
        Recipe.objects.create(
            chef=carina, title='another title', description='carinas description'
        )

    def test_can_retrieve_recipe_using_valid_id(self):
        response = self.client.get('/recipes/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_recipe_using_invalid_id(self):
        response = self.client.get('/recipes/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_recipe(self):
        self.client.login(username='carina', password='bambina')
        response = self.client.put('/recipes/2/', {'title': 'another title'})
        recipe = Recipe.objects.filter(pk=1).first()
        self.assertEqual(response.data['title'], 'another title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_recipe(self):
        self.client.login(username='andrea', password='rookiecoder')
        response = self.client.put('/recipes/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  