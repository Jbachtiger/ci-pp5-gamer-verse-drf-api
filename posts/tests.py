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


class PostDetailViewTests(APITestCase):
    '''
    Post detail view tests
    '''
    def setUp(self):
        john = User.objects.create_user(username='john', password='drf123')
        hannah = User.objects.create_user(username='hannah', password='drf123')
        Post.objects.create(
            owner=john, title='a title', description='johns content'
        )
        Post.objects.create(
            owner=hannah, title='another title', description='hannahs content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_fetch_a_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='john', password='drf123')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_cant_update_a_post_they_dont_own(self):
        self.client.login(username='hannah', password='drf123')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
