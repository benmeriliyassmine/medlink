from django.db import models
from patients.models import Patient
from doctor.models import MedecinProfile
from administrator.models import Service
   
class Analyse(models.Model):
   Tub=[
      ('Tube_EDTA','Tube EDTA'),
      ('Tube_Citrate','Tube Citrate'),
      ('Tube_sec','Tube sec'),
      ('Tube_Héparine','Tube Héparine'),
      ('Tube_stérile','Tube stérile'),
      ('Écouvillons_stériles_dans_tubes','Écouvillons stériles dans tubes'),
      ('Tube_Fluorure','Tube Fluorure'),
      ("Flacons_hémoculture","Flacons d'hémoculture"),
      ('Flacon_stérile','Flacon stérile'),
      ('Pot_stérile','Pot stérile'),
      ('milieu_de_transport_bactérien','milieu de transport bactérien')
   ]
   Type=[
      ('Hématologie','Hématologie'),
      ('Biochimie','Biochimie'),
      ('Microbiologie','Microbiologie'),
      ('Parasitologie','Parasitologie'),
      ('Sérologie','Sérologie'),
      ('Hormonologie','Hormonologie'),
      ('Biologie_moléculaire','Biologie moléculaire')
   ]
   nom=models.CharField(max_length=100,verbose_name="Nom de l'analyse")
   type_analyse=models.CharField(max_length=40,choices=Type)
   tub=models.CharField(max_length=40,choices=Tub)
class Echantillon(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    service=models.OneToOneField(Service, on_delete=models.CASCADE,null=True,blank=True)
    medecin=models.OneToOneField(MedecinProfile, on_delete=models.CASCADE)
    analyses=models.OneToOneField(Analyse, on_delete=models.CASCADE)
    
    class Meta:
      verbose_name="Un echantillon"
      verbose_name_plural="Les echantillons"
    def __str__(self):
        return self.patient.user.username