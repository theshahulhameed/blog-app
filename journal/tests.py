from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testemail@example.com',
            password='secret')
        self.post = Post.objects.create(
                            title='A test post', author=self.user,
                            body="It's just a sample post.")

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        """
        Verifies whether the post's title, author and body are all as
        expected.
        """
        post = Post.objects.get(id=1)
        post_object_title = f'{post.title}'
        self.assertEqual(post_object_title, 'A test post')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', "It's just a sample post.")
    
    def test_post_list_view(self):
        """
        Verifies whether the homepage, where the posts
        are getting listed are working properly in terms of the
        templated used, content and proper HTTP response.
        """
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'A test post')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('home.html')
    
    def test_post_detail_view(self):
        """
        Verifies whether the detail lists page, where the posts
        are displayed is working properly in terms of the
        templated used, content and proper HTTP response.
        """
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A test post")
        self.assertTemplateUsed('post.html')

    def test_post_create_view(self):
        """
        Verifies whether the post creation view works
        as we expected in terms of succesfully
        creating a new post.
        """
        response = self.client.post(reverse('create_post'), {
            'title': 'New title',
            'body': 'Sample text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'Sample text')
