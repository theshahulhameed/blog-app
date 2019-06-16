from django.test import TestCase
from django.urls import reverse


class SimpleTests(TestCase):
    def test_homepage_status_code(self):
        ''' Tests whether the homepage returns works. '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_status_by_url_name(self):
        """ Tests whether the homepage can be accessed by the URL name 'home' """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('home.html')

