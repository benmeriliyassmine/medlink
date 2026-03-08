from django.db import models
from administrator.models import User
class LaborantinProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Laborantin_profile')
    role='LAB'
    class Meta:
      verbose_name="Laborantin"
      verbose_name_plural="Laborantins"
    def __str__(self):
        return self.user.username