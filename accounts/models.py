
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
    date_naissance=models.DateField(null=True,blank=True)
    telephone=models.CharField(max_length=20,null=True,blank=True)
    genre=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default='ADMIN')
    def __str__(self):
        return self.username

#admin
class AdminProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='admin_profile')
        first_name=models.CharField(max_length=100,verbose_name="Nom")
        last_name=models.CharField(max_length=100,verbose_name="Prénom")
        is_superuser=True
        role='ADMIN'
        def __str__(self):
            return self.user.username
#les service
class Service(models.Model):
    nom=models.CharField(max_length=100)
    class Meta:
        verbose_name="service"
        verbose_name_plural="services"
    def __str__(self):
         return self.nom
#medecin Profile
class MedecinProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='medecin_profile')
    first_name=models.CharField(max_length=100,verbose_name="Nom")
    last_name=models.CharField(max_length=100,verbose_name="Prénom")
    specialization = models.CharField(max_length=100)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    class Meta:
      verbose_name="Medecin"
      verbose_name_plural="Les medecins"
    
    role='MEDECIN'
    def __str__(self):
        return self.user.username
#infirmiere profile
class InfirmiereProfile(models.Model):
   
   
   
   
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Infirmiere_Profile')
    first_name=models.CharField(max_length=100,verbose_name="Nom")
    last_name=models.CharField(max_length=100,verbose_name="Prénom")
    
    

    class Meta:
      verbose_name="Infirmiere"
      verbose_name_plural="Infirmieres"
    
    role='INFIRMIERE'
    def __str__(self):
        return self.user.username
#laborantin profile
class LaborantinProfile(models.Model):
    
    
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Laborantin_profile')
    first_name=models.CharField(max_length=100,verbose_name="Nom")
    last_name=models.CharField(max_length=100,verbose_name="Prénom")
    
    
    role='LAB'
    class Meta:
      verbose_name="Laborantin"
      verbose_name_plural="Laborantins"
    
    
    def __str__(self):
        return self.user.username
#dosie de patient
class Patient(models.Model):
  
  
  
  
  nom=models.CharField(max_length=100,verbose_name="Le nom")
  prenom=models.CharField(max_length=100,verbose_name="Le prénom")
  date_naissance=models.DateField(verbose_name="Date de naissence")
  telephone=models.CharField(max_length=20,verbose_name="telephone")
  address=models.TextField(verbose_name="L'address")
  
  creat_at=models.DateField(auto_now_add=True,verbose_name="Il a ete cree en")
  medecin=models.ForeignKey(MedecinProfile,on_delete=models.CASCADE)
  service=models.ForeignKey(Service,on_delete=models.CASCADE)
  class Meta:
    verbose_name="Patient"
    verbose_name_plural="Patients"
  def __str__(self):
     return f"{self.nom} {self.prenom}"