from django.contrib.staticfiles import finders
from django.templatetags.static import static
from django.template.loader import render_to_string
import re
from urllib.parse import unquote

from django.test import SimpleTestCase
from django.urls import reverse


class LoginTests(SimpleTestCase):
    def test_login_renders_django_template(self):
        response = self.client.get(reverse('login'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertContains(response, 'Iniciar sesión | Mundo Agropecuario CAM')
        self.assertContains(response, 'auth-form-light')
        self.assertContains(response, 'id="username"')
        self.assertContains(response, 'type="password"')
        self.assertContains(response, '<h1 class="h4">Iniciar sesión</h1>')
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
        self.assertTemplateUsed(response, 'dashboard/home.html')
        self.assertContains(response, 'Dashboard | Mundo Agropecuario CAM')
        self.assertContains(response, '/static/staradmin/css/style.css')
        self.assertContains(response, 'id="sidebar"')
        self.assertContains(response, f'href="{reverse("pet-register")}"')
        self.assertNotContains(response, '<canvas')
        self.assertNotContains(response, 'href="pages/')
        self.assertNotContains(response, 'href="index.html"')

    def test_dashboard_resources_are_available(self):
        response = self.client.get(reverse('home'))
        resources = re.findall(r'(?:src|href)="/static/([^"?]+)', response.content.decode())

        self.assertTrue(resources)
        for resource in resources:
            with self.subTest(resource=resource):
                self.assertIsNotNone(finders.find(unquote(resource)))

    def test_dashboard_shows_veterinary_and_store_sections_without_appointments(self):
        response = self.client.get(reverse('home'))

        for section in ('Mascotas registradas', 'Ventas del día',
                        'Productos con stock bajo', 'Medicamentos próximos a vencer',
                        'Alertas de inventario', 'Últimas mascotas registradas',
                        'Acceso rápido'):
            with self.subTest(section=section):
                self.assertContains(response, section)
        html = response.content.decode().lower()
        self.assertNotIn('citas', html)
        self.assertNotIn('agenda', html)

    def test_dashboard_labels_unavailable_data_without_fake_records(self):
        response = self.client.get(reverse('home'))

        self.assertContains(response, 'aria-label="Sin información"', count=4)
        self.assertContains(response, 'Sin información disponible.')
        self.assertContains(response, 'colspan="6"')

    def test_stylesheet_is_available(self):
        self.assertIsNotNone(finders.find('staradmin/css/style.css'))

    def test_health_check_is_preserved(self):
        response = self.client.get(reverse('health-check'))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'ok', 'service': 'backend'})


class BrandingTests(SimpleTestCase):
    def test_pages_share_cam_identity(self):
        for route in ('home', 'login', 'pet-register'):
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


class PetRegisterTests(SimpleTestCase):
    def test_registration_renders_all_animal_fields(self):
        response = self.client.get(reverse('pet-register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pets/register.html')
        self.assertTemplateUsed(response, 'base.html')
        for field in ('id_clientes', 'id_especie', 'id_raza',
                      'nombre_a', 'fecha_nacimiento', 'sexo', 'peso_inicial',
                      'color', 'observaciones'):
            with self.subTest(field=field):
                self.assertContains(response, f'id="{field}"')
        self.assertContains(response, 'type="button" disabled>Guardar mascota')
        self.assertContains(response, f'href="{reverse("home")}"')

    def test_registration_does_not_save_data(self):
        response = self.client.post(reverse('pet-register'), {'nombre_a': 'Luna'})
        self.assertEqual(response.status_code, 405)

    def test_registration_resources_are_available(self):
        response = self.client.get(reverse('pet-register'))
        resources = re.findall(r'(?:src|href)="/static/([^"?]+)', response.content.decode())
        self.assertTrue(resources)
        for resource in resources:
            with self.subTest(resource=resource):
                self.assertIsNotNone(finders.find(unquote(resource)))


class PresentationTests(SimpleTestCase):
    def test_pages_do_not_show_development_notes(self):
        for route in ('home', 'login', 'pet-register'):
            response = self.client.get(reverse(route))
            for text in ('demostración', 'Módulo pendiente', 'Prototipo',
                         'Solo vistas', '(ejemplo)', 'más adelante',
                         'Sin datos conectados'):
                with self.subTest(route=route, text=text):
                    self.assertNotContains(response, text)


class TemplateStructureTests(SimpleTestCase):
    def test_all_pages_share_base_and_brand(self):
        for route in ('home', 'login', 'pet-register'):
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertTemplateUsed(response, 'base.html')
                self.assertTemplateUsed(response, 'components/brand.html')
                self.assertContains(response, '<!doctype html>', count=1)
                self.assertContains(response, 'href="/static/css/branding.css"', count=1)

    def test_app_pages_share_navigation_and_active_link(self):
        for route in ('home', 'pet-register'):
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                for template in ('layouts/app.html', 'components/sidebar.html',
                                 'components/header.html', 'components/footer.html'):
                    self.assertTemplateUsed(response, template)
                self.assertContains(response, f'href="{reverse(route)}" aria-current="page"')
                self.assertContains(response, 'aria-current="page"', count=1)

    def test_login_uses_auth_layout_without_app_navigation(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'layouts/auth.html')
        self.assertTemplateNotUsed(response, 'components/sidebar.html')
        self.assertNotContains(response, 'id="sidebar"')

    def test_stat_card_accepts_values_and_escapes_content(self):
        html = render_to_string('components/stat_card.html', {
            'title': '<script>test</script>',
            'value': '12',
        })
        self.assertIn('&lt;script&gt;test&lt;/script&gt;', html)
        self.assertIn('>12</p>', html)
        self.assertNotIn('aria-label=', html)
