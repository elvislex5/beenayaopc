# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'telephone', 'entreprise')


class CustomUserChangeForm(UserChangeForm):
    password = None  # Exclut le champ de mot de passe du formulaire

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'telephone', 'entreprise', 'photo_profil')
        widgets = {
            'photo_profil': forms.FileInput(),
        }