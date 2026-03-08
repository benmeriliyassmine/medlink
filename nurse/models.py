from django.db import models
from administrator.models import User
class InfirmiereProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Infirmiere_Profile')
    class Meta:
      verbose_name="Infirmiere"
      verbose_name_plural="Infirmieres"
    
    role='INFIRMIERE'
    def __str__(self):
        return self.user.username