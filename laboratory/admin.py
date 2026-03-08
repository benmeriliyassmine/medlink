from django.contrib import admin
from django.contrib.auth.models import Group
from .models import LaborantinProfile
from samples.models import Analyse,Echantillon
@admin.register(Analyse)
class Analyse(admin.ModelAdmin):
    list_display=("nom",'type_analyse',"tub")
    list_filter=('type_analyse',"tub",)
@admin.register(Echantillon)
class Echantillon(admin.ModelAdmin):
    list_display=("patient",'service',"medecin",'analyses')
@admin.register(LaborantinProfile)
class LaborantinProfile(admin.ModelAdmin):
    list_display=("user__username",'user__first_name',"user__last_name",'user__genre')
    search_fields=("user__username",'user__first_name',"user__last_name")