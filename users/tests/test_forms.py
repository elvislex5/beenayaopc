# users/tests/test_forms.py
from django.test import TestCase
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import User, Role


class UserFormsTest(TestCase):
    def test_user_creation_form_valid_data(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'role': Role.OPC,
            'telephone': '0123456789',
            'entreprise': 'Test Entreprise'
        })
        self.assertTrue(form.is_valid())

    def test_user_creation_form_invalid_data(self):
        # Test avec mots de passe différents
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'complexpassword123',
            'password2': 'differentpassword',
            'role': Role.OPC
        })
        self.assertFalse(form.is_valid())

    def test_user_change_form(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )

        form = CustomUserChangeForm(instance=user, data={
            'first_name': 'Updated',
            'last_name': 'Name',
            'email': 'updated@example.com',
            'telephone': '9876543210',
            'entreprise': 'Updated Company'
        })
        self.assertTrue(form.is_valid())