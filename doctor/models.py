
from django.db import models
from administrator.models import User,Service

#medecin Profile
class MedecinProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='medecin_profile')
    
    specialization = models.CharField(max_length=100)
    service=models.ForeignKey(Service,on_delete=models.CASCADE,null=True,blank=True)
    class Meta:
      verbose_name="Medecin"
      verbose_name_plural="Les medecins"
    
    role='MEDECIN'
    def __str__(self):
        return self.user.username
  
