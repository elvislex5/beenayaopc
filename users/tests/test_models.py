# users/tests/test_models.py
from django.test import TestCase
from users.models import User, Role


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user',
            email='test@example.com',
            password='testpassword123',
            first_name='Test',
            last_name='User',
            role=Role.CHEF_PROJET,
            entreprise='Test Entreprise'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'test_user')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.role, Role.CHEF_PROJET)
        self.assertEqual(self.user.entreprise, 'Test Entreprise')
        self.assertTrue(self.user.check_password('testpassword123'))

    def test_user_str_method(self):
        expected_str = "Test User (Chef de projet)"
        self.assertEqual(str(self.user), expected_str)