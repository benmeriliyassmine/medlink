from django.contrib import admin

from .models import Patient
@admin.register(Patient)
class Patient(admin.ModelAdmin):
    list_display=("user__username",'user__first_name',"user__last_name",'user__genre')
    search_fields=("user__username",'user__first_name',"user__last_name")
