from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Service,MedecinProfile,InfirmiereProfile,Patient,AdminProfile,LaborantinProfile
from accounts.models import User
admin.site.register(User)
admin.site.unregister(Group)
admin.site.register(Service)

@admin.register(Patient)
class Patient(admin.ModelAdmin):
    list_display=("gender",'nom','prenom',"date_naissance","creat_at","medecin")
    list_filter=("gender","creat_at","medecin",)
    search_fields=('nom','prenom')
@admin.register(MedecinProfile)
class MedecinProfile(admin.ModelAdmin):
    list_display=("user","gender",'nom','prenom',"date_naissance","service")
    list_filter=("gender","service",)
    search_fields=('nom','prenom',"user")
@admin.register(InfirmiereProfile)
class InfirmiereProfile(admin.ModelAdmin):
    list_display=("user","gender",'nom','prenom',"date_naissance")
    list_filter=("gender",)
    search_fields=('nom','prenom',"user")
@admin.register(LaborantinProfile)
class LaborantinProfile(admin.ModelAdmin):
    list_display=("user","gender",'nom','prenom',"date_naissance")
    list_filter=("gender",)
    search_fields=('nom','prenom',"user")
@admin.register(AdminProfile)
class AdminProfile(admin.ModelAdmin):
    list_display=("user","gender",'nom','prenom',"date_naissance")
    list_filter=("gender",)
    search_fields=('nom','prenom',"user")
