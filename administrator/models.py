from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('LAB', 'Laboratoire'),
        ('MEDECIN', 'medecin'),
        ('INFIRMIERE', 'Infirmiere'),
    )
    GENDER_CHOICES=[ 
     ("M","Male"),
     ("F","Female"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default='ADMIN')
    date_naissance=models.DateField(null=True,blank=True)
    telephone=models.CharField(max_length=20,null=True,blank=True)
    genre=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    def __str__(self):
        return self.username

class Service(models.Model):
    nom=models.CharField(max_length=100)
    class Meta:
        verbose_name="service"
        verbose_name_plural="services"
    def __str__(self):
         return self.nom
class AdminProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='admin_profile')
        
        
        is_superuser=True
        role='ADMIN'
        def __str__(self):
            return self.user.username

