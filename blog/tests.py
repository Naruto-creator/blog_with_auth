from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            text='Nice text',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'test_user')
        self.assertEqual(f'{self.post.text}', 'Nice text')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice text')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/blog/1/')
        no_response = self.client.get('/blog/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/blog/1/')

    def test_post_create_view(self):
        response = self.client.post( reverse('new_post'),
             {
                 'title': 'Test title',
                 'text': 'Test text',
                 'author': self.user,
             }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test title')
        self.assertContains(response, 'Test text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'),
            {
                'title': 'Test update title',
                'text': 'Test update text',
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)





















