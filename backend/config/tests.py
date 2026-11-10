from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import reverse


class HomeTests(SimpleTestCase):
    def test_home_renders_django_template(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Plantillas Django')
        self.assertContains(response, '/static/css/main.css')

    def test_stylesheet_is_available(self):
        self.assertIsNotNone(finders.find('css/main.css'))

    def test_health_check_is_preserved(self):
        response = self.client.get(reverse('health-check'))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'ok', 'service': 'backend'})
