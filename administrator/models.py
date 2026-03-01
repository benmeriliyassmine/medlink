from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.models import User
from django.conf import settings
from django.contrib.auth.models import Group


#admin
class AdminProfile(models.Model):
        GENDER_CHOICES=[
        ("M","Masculin"),
        ("F","Feminin"),
        ]
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        nom=models.CharField(max_length=100,verbose_name="Nom")
        prenom=models.CharField(max_length=100,verbose_name="Prénom")
        date_naissance=models.DateField(verbose_name="Date de naissence")
        telephone=models.CharField(max_length=20,verbose_name="Numero de telephone")
        gender=models.CharField(max_length=1,choices=GENDER_CHOICES,verbose_name="Gender")
        nom_de_hopital=models.CharField(max_length=30,verbose_name="Nom de hopital")
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
    GENDER_CHOICES=[
    ("M","Masculin"),
    ("F","Feminin")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom=models.CharField(max_length=100,verbose_name="Nom")
    prenom=models.CharField(max_length=100,verbose_name="Prénom")
    date_naissance=models.DateField(verbose_name="Date de naissence")
    telephone=models.CharField(max_length=20,verbose_name="Numero de telephone")
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,verbose_name="Gender")
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    class Meta:
      verbose_name="Medecin"
      verbose_name_plural="Les medecins"
    
    role='MEDECIN'
    def __str__(self):
        return self.user.username
#infirmiere profile
class InfirmiereProfile(models.Model):
    GENDER_CHOICES=[
    ("M","Masculin"),
    ("F","Feminin")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom=models.CharField(max_length=100,verbose_name="Nom")
    prenom=models.CharField(max_length=100,verbose_name="Prénom")
    date_naissance=models.DateField(verbose_name="Date de naissence")
    telephone=models.CharField(max_length=20,verbose_name="Numero de telephone")
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,verbose_name="Gender")
    class Meta:
      verbose_name="Infirmiere"
      verbose_name_plural="Infirmieres"
    
    role='INFIRMIERE'
    def __str__(self):
        return self.user.username
#laborantin profile
class LaborantinProfile(models.Model):
    GENDER_CHOICES=[
    ("M","Masculin"),
    ("F","Feminin")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom=models.CharField(max_length=100,verbose_name="Nom")
    prenom=models.CharField(max_length=100,verbose_name="Prénom")
    date_naissance=models.DateField(verbose_name="Date de naissence")
    telephone=models.CharField(max_length=20,verbose_name="Numero de telephone")
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,verbose_name="Gender")
    class Meta:
      verbose_name="Laborantin"
      verbose_name_plural="Laborantins"
    
    role='LAB_TECH'
    def __str__(self):
        return self.user.username
#dosie de patient
class Patient(models.Model):
  GENDER_CHOICES=[
      ("M","Masculin"),
      ("F","Feminin")
  ]
  nom=models.CharField(max_length=100,verbose_name="Le nom")
  prenom=models.CharField(max_length=100,verbose_name="Le prénom")
  date_naissance=models.DateField(verbose_name="Date de naissence")
  telephone=models.CharField(max_length=20,verbose_name="telephone")
  address=models.TextField(verbose_name="L'address")
  gender=models.CharField(max_length=1,choices=GENDER_CHOICES,verbose_name="Gender")
  creat_at=models.DateField(auto_now_add=True,verbose_name="Il a ete cree en")
  medecin=models.ForeignKey(MedecinProfile,on_delete=models.CASCADE)
  service=models.ForeignKey(Service,on_delete=models.CASCADE)
  class Meta:
    verbose_name="Patient"
    verbose_name_plural="Patients"
  def __str__(self):
     return f"{self.nom} {self.prenom}"