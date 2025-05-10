# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrateur'
    CHEF_PROJET = 'CHEF_PROJET', 'Chef de projet'
    CONDUCTEUR_TRAVAUX = 'CONDUCTEUR_TRAVAUX', 'Conducteur de travaux'
    OPC = 'OPC', 'OPC'
    ARCHITECTE = 'ARCHITECTE', 'Architecte'
    ENTREPRENEUR = 'ENTREPRENEUR', 'Entrepreneur'


class User(AbstractUser):
    """Modèle utilisateur personnalisé pour l'application OPC"""
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.ENTREPRENEUR,
    )
    telephone = models.CharField(max_length=15, blank=True)
    entreprise = models.CharField(max_length=100, blank=True)
    photo_profil = models.ImageField(upload_to='profils/', blank=True, null=True)
    date_derniere_connexion = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"