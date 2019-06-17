from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class PageTests(TestCase):
    def test_homepage_status_code(self):
        ''' 
        Tests whether the homepage returns works.
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_status_by_url_name(self):
        """ 
        Tests whether the homepage can be accessed by the URL name 'home'
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('home.html')


class JournalTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testemail@example.com',
            password='secret')
        Post.objects.create(
                            title='A test post', author=self.user,
                            body="It's just a sample post.")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        post_object_title = f'{post.title}'
        self.assertEqual(post_object_title, 'A test post')