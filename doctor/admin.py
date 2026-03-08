from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import MedecinProfile
@admin.register(MedecinProfile)
class MedecinProfile(admin.ModelAdmin):
    
    list_display=("user__username",'user__first_name',"user__last_name",'user__genre',"service")
    list_filter=("service",)
    
