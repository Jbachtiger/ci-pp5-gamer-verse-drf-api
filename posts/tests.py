from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    '''
    Post list view tests
    '''
    def setUp(self):
        User.objects.create_user(username='admin', password='drf123')

    def test_can_list_posts(self):
        admin = User.objects.get(username='admin')
        Post.objects.create(owner=admin, title='Hello World')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='admin', password='drf123')
        response = self.client.post('/posts/', {'title': 'Hello World'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_user_not_logged_in__cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'Hello World'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


