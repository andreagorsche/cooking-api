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

