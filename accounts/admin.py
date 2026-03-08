from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Service,MedecinProfile,InfirmiereProfile,Patient,AdminProfile,LaborantinProfile
from accounts.models import User
@admin.register(User)
class User(admin.ModelAdmin):
    
    list_display=("username",'first_name','last_name')
    
    search_fields=('first_name','last_name',"user")
admin.site.unregister(Group)
admin.site.register(Service)

@admin.register(Patient)
class Patient(admin.ModelAdmin):
    list_display=('nom','prenom',"creat_at","medecin")
    list_filter=("creat_at","medecin",)
    search_fields=('nom','prenom')
@admin.register(MedecinProfile)
class MedecinProfile(admin.ModelAdmin):
    list_display=("user",'first_name','last_name',"service")
    list_filter=("service",)
    search_fields=('first_name','last_name',"user")
@admin.register(InfirmiereProfile)
class InfirmiereProfile(admin.ModelAdmin):
    list_display=("user",'first_name','last_name')
    
    search_fields=('first_name','last_name',"user")
@admin.register(LaborantinProfile)
class LaborantinProfile(admin.ModelAdmin):
    list_display=("user",'first_name','last_name')
    
    search_fields=('first_name','last_name',"user")
@admin.register(AdminProfile)
class AdminProfile(admin.ModelAdmin):
    
    list_display=("user",'first_name','last_name')
    
    search_fields=('first_name','last_name',"user")
