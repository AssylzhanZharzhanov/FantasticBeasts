from django.test import TestCase
from .models import Beast
from django.urls import reverse
from django.contrib.auth.models import User


class AnimalTestCase(TestCase):
    def setUp(self):
        Beast.objects.create(name='Эльфы', type='Animal', description= 'elphs are good')
        Beast.objects.create(name='Авгурей', type='Bird')

    def test_type_of_animals(self):
        elphs = Beast.objects.get(name="Эльфы")
        birds = Beast.objects.get(name='Авгурей')
        self.assertEqual(elphs.type, 'Animal')
        self.assertEqual(birds.type, 'Bird')

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Homepage</h1>')


class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'mrx',
            'password': 'adminmrx'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)


