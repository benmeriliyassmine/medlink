from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('LAB_TECH', 'Laboratory Technician'),
        ('DOCTOR', 'Doctor'),
        ('NURSE', 'Nurse'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='NURSE')
    phone = models.CharField(max_length=20, blank=True)
    employee_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    department = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"