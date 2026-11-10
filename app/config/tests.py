from django.contrib.staticfiles import finders
import re

from django.test import SimpleTestCase
from django.urls import reverse


class HomeTests(SimpleTestCase):
    def test_home_renders_django_template(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Dashboard | Proyecto universitario 331')
        self.assertContains(response, '/static/staradmin/css/style.css')
        self.assertContains(response, 'id="sidebar"')
        self.assertContains(response, '<canvas')
        self.assertNotContains(response, 'href="pages/')
        self.assertNotContains(response, 'href="index.html"')

    def test_dashboard_resources_are_available(self):
        response = self.client.get(reverse('home'))
        resources = re.findall(r'(?:src|href)="/static/([^"?]+)', response.content.decode())

        self.assertTrue(resources)
        for resource in resources:
            with self.subTest(resource=resource):
                self.assertIsNotNone(finders.find(resource))

    def test_stylesheet_is_available(self):
        self.assertIsNotNone(finders.find('staradmin/css/style.css'))

    def test_health_check_is_preserved(self):
        response = self.client.get(reverse('health-check'))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'ok', 'service': 'backend'})
