from django.contrib.staticfiles import finders
from django.templatetags.static import static
import re
from urllib.parse import unquote

from django.test import SimpleTestCase
from django.urls import reverse


class LoginTests(SimpleTestCase):
    def test_login_renders_django_template(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Iniciar sesión | Mundo Agropecuario CAM')
        self.assertContains(response, 'auth-form-light')
        self.assertContains(response, 'id="username"')
        self.assertContains(response, 'type="password"')
        self.assertContains(response, 'El inicio de sesión aún no está disponible.')
        self.assertContains(response, f'href="{reverse("home")}"')
        self.assertNotContains(response, 'href="pages/')
        self.assertNotContains(response, 'href="index.html"')

    def test_login_resources_are_available(self):
        response = self.client.get(reverse('login'))
        resources = re.findall(r'(?:src|href)="/static/([^"?]+)', response.content.decode())

        self.assertTrue(resources)
        for resource in resources:
            with self.subTest(resource=resource):
                self.assertIsNotNone(finders.find(unquote(resource)))

    def test_login_does_not_process_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'demo',
            'password': 'demo',
        })

        self.assertEqual(response.status_code, 405)


class HomeTests(SimpleTestCase):
    def test_home_renders_django_template(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Dashboard | Mundo Agropecuario CAM')
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
                self.assertIsNotNone(finders.find(unquote(resource)))

    def test_stylesheet_is_available(self):
        self.assertIsNotNone(finders.find('staradmin/css/style.css'))

    def test_health_check_is_preserved(self):
        response = self.client.get(reverse('health-check'))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'ok', 'service': 'backend'})


class BrandingTests(SimpleTestCase):
    def test_pages_share_cam_identity(self):
        for route in ('home', 'login'):
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertContains(response, static('branding/logo CAM.jpg.jpeg'))
                self.assertContains(response, static('css/branding.css'))
                self.assertContains(response, 'Inversiones Mundo Agropecuario CAM')
                self.assertNotContains(response, 'staradmin/images/logo.svg')
                self.assertNotContains(response, 'staradmin/images/logo-mini.svg')
                html = response.content.decode()
                self.assertLess(
                    html.index(static('staradmin/css/style.css')),
                    html.index(static('css/branding.css')),
                )
