from django.contrib.auth.models import User
from .models import Comment
from rest_framework import status
from rest_framework.test import APITestCase


class CommentListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='andrea', password='rookiecoder')

    def test_can_list_comments(self):
        andrea = User.objects.get(username='andrea')
        Comment.objects.create(chef=andrea, content='andreas comment')
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logged_in_user_can_create_comment(self):
        self.client.login(username='andrea', password='rookiecoder')
        response = self.client.post('/comments/', {'content': 'andreas comment'})
        count = Comment.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in_cant_create_comment(self):
        response = self.client.post('/comments/', {'content': 'andreas comment'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

"""
class CommentDetailViewTests(APITestCase):
    def setUp(self):
        andrea = User.objects.create_user(username='andrea', password='rookiecoder')
        carina = User.objects.create_user(username='carina', password='bambina')
        Comment.objects.create(
            chef=andrea, content='andreas comment'
        )
        Comment.objects.create(
            chef=carina, content='carinas comment'
        )

    def test_can_retrieve_comment_using_valid_id(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['content'], 'andreas comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/comments/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_comment(self):
        self.client.login(username='carina', password='bambina')
        response = self.client.put('/comments/2/', {'content': 'carinas comment'})
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(response.data['content'], 'carinas comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_comment(self):
        self.client.login(username='andrea', password='rookiecoder')
        response = self.client.put('/comments/2/', {'content': 'carinas comment'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  
"""
