# users/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from users.models import User, Role


class UserViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('users:register')
        self.login_url = reverse('users:login')
        self.profile_url = reverse('users:profile')
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123',
            role=Role.CHEF_PROJET
        )

    def test_register_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_view_POST_valid(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
            'role': Role.ENTREPRENEUR
        })
        self.assertEqual(User.objects.count(), 2)
        self.assertRedirects(response, self.profile_url)

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

        # Test login avec identifiants valides
        login_response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertRedirects(login_response, reverse('users:profile'))

    def test_profile_view_access_protection(self):
        # Test accès non autorisé (non connecté)
        response = self.client.get(self.profile_url)
        self.assertRedirects(response, f'{self.login_url}?next={self.profile_url}')

        # Test accès autorisé (connecté)
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')