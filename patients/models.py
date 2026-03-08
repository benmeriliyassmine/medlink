from django.db import models
from administrator.models import User,Service
class Patient(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='patient_profile')
  address=models.TextField(verbose_name="L'address")
  class Meta:
    verbose_name="Patient"
    verbose_name_plural="Patients"
  def __str__(self):
     return self.user.username