from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('LAB_TECH', 'Laboratory Technician'),
        ('MEDECIN', 'medecin'),
        ('INFIRMIERE', 'Infirmiere'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default=None)
    def __str__(self):
        return self.username